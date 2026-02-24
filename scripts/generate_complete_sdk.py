#!/usr/bin/env python3
"""
Complete SDK Generation Pipeline - One Command Solution

This script automates the entire SDK generation process:
1. Validates API specifications
2. Generates WebSocket models and handlers
3. Generates HTTP clients with OpenAPI Generator
4. Fixes all imports automatically
5. Creates main client wrapper
6. Creates package __init__.py
7. Validates the final SDK

Usage:
    python3 scripts/generate_complete_sdk.py

Or via Make:
    make build-sdk
"""

import os
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


def print_step(step: int, total: int, title: str):
    """Print formatted step header."""
    print(f"\n{'=' * 80}")
    print(f"  STEP {step}/{total}: {title}")
    print('=' * 80)


def run_command(cmd: List[str], description: str) -> Tuple[bool, str]:
    """
    Run a command and return success status.

    Args:
        cmd: Command to run as list
        description: Human-readable description

    Returns:
        Tuple of (success: bool, error_message: str)
    """
    print(f"  → {description}")
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        print(f"    ✓ Success")
        return True, ""
    except subprocess.CalledProcessError as e:
        error_msg = f"    ✗ Failed: {e.stderr}"
        print(error_msg)
        return False, error_msg


def run_python_script(script: str, description: str) -> Tuple[bool, str]:
    """Run a Python script."""
    return run_command(["python3", script], description)


def create_client_file():
    """Create the main WhiteBitClient file."""
    print("  → Creating whitebit_sdk/client.py")

    client_content = '''"""WhiteBIT SDK main client."""

from typing import Optional
from .config import WhiteBitConfig
from .http.generated.main_api.main_api_generated.api_client import ApiClient as MainApiClient
from .http.generated.main_api.main_api_generated.configuration import Configuration as MainApiConfig
from .http.generated.public_api.public_api_generated.api_client import ApiClient as PublicApiClient
from .http.generated.public_api.public_api_generated.configuration import Configuration as PublicApiConfig
from .http.generated.oauth2_api.oauth2_api_generated.api_client import ApiClient as OAuth2ApiClient
from .http.generated.oauth2_api.oauth2_api_generated.configuration import Configuration as OAuth2ApiConfig

# Import API classes
from .http.generated.main_api.main_api_generated.api.main_account_api import MainAccountApi
from .http.generated.main_api.main_api_generated.api.fees_api import FeesApi
from .http.generated.main_api.main_api_generated.api.transfer_api import TransferApi
from .http.generated.main_api.main_api_generated.api.withdraw_api import WithdrawApi
from .http.generated.main_api.main_api_generated.api.deposit_api import DepositApi
from .http.generated.main_api.main_api_generated.api.codes_api import CodesApi
from .http.generated.main_api.main_api_generated.api.credit_line_api import CreditLineApi
from .http.generated.main_api.main_api_generated.api.jwt_api import JWTApi
from .http.generated.main_api.main_api_generated.api.mining_pool_api import MiningPoolApi
from .http.generated.main_api.main_api_generated.api.sub_account_api import SubAccountApi
from .http.generated.main_api.main_api_generated.api.sub_account_api_keys_api import SubAccountAPIKeysApi
from .http.generated.main_api.main_api_generated.api.crypto_lending_fixed_api import CryptoLendingFixedApi
from .http.generated.main_api.main_api_generated.api.crypto_lending_flex_api import CryptoLendingFlexApi

# Import Public API
from .http.generated.public_api.public_api_generated.api.public_apiv4_api import PublicAPIV4Api

# Import OAuth2 API
from .http.generated.oauth2_api.oauth2_api_generated.api.authentication_api import AuthenticationApi
from .http.generated.oauth2_api.oauth2_api_generated.api.account_endpoints_api import AccountEndpointsApi


class MainApiWrapper:
    """Wrapper for Main API endpoints."""

    def __init__(self, api_client: MainApiClient):
        self.main_account = MainAccountApi(api_client)
        self.fees = FeesApi(api_client)
        self.transfer = TransferApi(api_client)
        self.withdraw = WithdrawApi(api_client)
        self.deposit = DepositApi(api_client)
        self.codes = CodesApi(api_client)
        self.credit_line = CreditLineApi(api_client)
        self.jwt = JWTApi(api_client)
        self.mining_pool = MiningPoolApi(api_client)
        self.sub_account = SubAccountApi(api_client)
        self.sub_account_api_keys = SubAccountAPIKeysApi(api_client)
        self.crypto_lending_fixed = CryptoLendingFixedApi(api_client)
        self.crypto_lending_flex = CryptoLendingFlexApi(api_client)


class PublicApiWrapper:
    """Wrapper for Public API endpoints."""

    def __init__(self, api_client: PublicApiClient):
        self.public = PublicAPIV4Api(api_client)


class OAuth2Wrapper:
    """Wrapper for OAuth2 API endpoints."""

    def __init__(self, api_client: OAuth2ApiClient):
        self.authentication = AuthenticationApi(api_client)
        self.account = AccountEndpointsApi(api_client)


class WhiteBitClient:
    """
    Unified WhiteBIT SDK client.

    Provides access to all WhiteBIT API endpoints through a single interface.

    Usage:
        # Initialize with credentials
        client = WhiteBitClient(api_key="your_key", api_secret="your_secret")

        # Access Main API
        balance = await client.main_api.main_account.get_main_balance(...)

        # Access Public API
        markets = await client.public_api.public.api_v4_public_markets_get()

        # Access OAuth2 API
        token = await client.oauth2.authentication.token(...)
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        base_url: str = "https://whitebit.com",
        timeout: int = 30,
        verify_ssl: bool = True
    ):
        """
        Initialize WhiteBIT client.

        Args:
            api_key: WhiteBIT API key (required for private endpoints)
            api_secret: WhiteBIT API secret (required for private endpoints)
            base_url: Base URL for API requests
            timeout: Request timeout in seconds
            verify_ssl: Verify SSL certificates (set to False only for testing)
        """
        self.config = WhiteBitConfig(
            api_key=api_key,
            api_secret=api_secret,
            base_url=base_url,
            timeout=timeout
        )

        # Configure Main API
        main_config = MainApiConfig(host=base_url)
        main_config.verify_ssl = verify_ssl
        if api_key:
            main_config.api_key['APIKey'] = api_key
        if api_secret:
            main_config.api_key['SecretKey'] = api_secret
        self._main_api_client = MainApiClient(main_config)
        self.main_api = MainApiWrapper(self._main_api_client)

        # Configure Public API
        public_config = PublicApiConfig(host=base_url)
        public_config.verify_ssl = verify_ssl
        self._public_api_client = PublicApiClient(public_config)
        self.public_api = PublicApiWrapper(self._public_api_client)

        # Configure OAuth2 API
        oauth2_config = OAuth2ApiConfig(host=base_url)
        oauth2_config.verify_ssl = verify_ssl
        if api_key:
            oauth2_config.api_key['APIKey'] = api_key
        if api_secret:
            oauth2_config.api_key['SecretKey'] = api_secret
        self._oauth2_api_client = OAuth2ApiClient(oauth2_config)
        self.oauth2 = OAuth2Wrapper(self._oauth2_api_client)

    async def close(self):
        """Close all API client connections."""
        await self._main_api_client.close()
        await self._public_api_client.close()
        await self._oauth2_api_client.close()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()
'''

    client_path = Path("whitebit_sdk/client.py")
    client_path.write_text(client_content)
    print("    ✓ Created client.py")


def create_init_file():
    """Create the main __init__.py file."""
    print("  → Creating whitebit_sdk/__init__.py")

    init_content = '''"""
WhiteBIT SDK - Python SDK for WhiteBIT Exchange API.

Provides typed async clients for:
- Main API (private endpoints)
- Public API (market data)
- OAuth2 API (authentication)
- WebSocket API (real-time data)
"""

from .client import WhiteBitClient, MainApiWrapper, PublicApiWrapper, OAuth2Wrapper
from .config import WhiteBitConfig
from .exceptions import (
    WhiteBitAPIException,
    AuthenticationError,
    AuthorizationError,
    RateLimitError,
    ValidationError,
    NotFoundError,
    ServerError,
    WebSocketError,
    ConnectionError,
    SubscriptionError,
)

__version__ = "1.0.0"

__all__ = [
    # Main client
    "WhiteBitClient",
    # Config
    "WhiteBitConfig",
    # Wrappers
    "MainApiWrapper",
    "PublicApiWrapper",
    "OAuth2Wrapper",
    # Exceptions
    "WhiteBitAPIException",
    "AuthenticationError",
    "AuthorizationError",
    "RateLimitError",
    "ValidationError",
    "NotFoundError",
    "ServerError",
    "WebSocketError",
    "ConnectionError",
    "SubscriptionError",
]
'''

    init_path = Path("whitebit_sdk/__init__.py")
    init_path.write_text(init_content)
    print("    ✓ Created __init__.py")


def validate_sdk():
    """Validate the generated SDK."""
    print("  → Validating SDK import")

    try:
        result = subprocess.run(
            ["python3", "-c", "from whitebit_sdk import WhiteBitClient; WhiteBitClient()"],
            capture_output=True,
            text=True,
            check=True
        )
        print("    ✓ SDK imports successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"    ✗ Import failed: {e.stderr}")
        return False


def main():
    """Main generation pipeline."""
    print("\n" + "=" * 80)
    print("  COMPLETE SDK GENERATION PIPELINE")
    print("=" * 80)
    print("\nThis will generate the complete WhiteBIT SDK from API specifications.\n")

    total_steps = 8

    # Step 1: Validate specifications
    print_step(1, total_steps, "Validate API Specifications")
    success, error = run_python_script(
        "scripts/validate_specs.py",
        "Validating YAML specifications"
    )
    if not success:
        print("\n❌ Generation failed at step 1")
        return False

    # Step 2: Generate WebSocket models
    print_step(2, total_steps, "Generate WebSocket Models")
    success, error = run_python_script(
        "scripts/generate_websocket_models.py",
        "Generating Pydantic models from AsyncAPI"
    )
    if not success:
        print("\n❌ Generation failed at step 2")
        return False

    # Step 3: Generate WebSocket handlers
    print_step(3, total_steps, "Generate WebSocket Handlers")
    success, error = run_python_script(
        "scripts/generate_websocket_handlers.py",
        "Generating WebSocket channel handlers"
    )
    if not success:
        print("\n❌ Generation failed at step 3")
        return False

    # Step 4: Create SDK infrastructure
    print_step(4, total_steps, "Create SDK Infrastructure")
    success, error = run_python_script(
        "scripts/create_sdk_structure.py",
        "Creating base classes and utilities"
    )
    if not success:
        print("\n❌ Generation failed at step 4")
        return False

    # Step 5: Generate HTTP clients
    print_step(5, total_steps, "Generate HTTP API Clients")
    success, error = run_command(
        ["./scripts/generate_http_openapi.sh"],
        "Running OpenAPI Generator for HTTP clients"
    )
    if not success:
        print("\n❌ Generation failed at step 5")
        return False

    # Step 6: Fix all imports
    print_step(6, total_steps, "Fix Generated Imports")
    success, error = run_python_script(
        "scripts/fix_generated_imports.py",
        "Converting absolute imports to relative imports"
    )
    if not success:
        print("\n❌ Generation failed at step 6")
        return False

    # Step 7: Create main client files
    print_step(7, total_steps, "Create Main Client Wrapper")
    try:
        create_client_file()
        create_init_file()
    except Exception as e:
        print(f"    ✗ Failed: {e}")
        print("\n❌ Generation failed at step 7")
        return False

    # Step 8: Validate SDK
    print_step(8, total_steps, "Validate Generated SDK")
    if not validate_sdk():
        print("\n❌ Generation failed at step 8")
        return False

    # Success!
    print("\n" + "=" * 80)
    print("  ✅ SDK GENERATION COMPLETE!")
    print("=" * 80)
    print("\n📦 Generated:")
    print("   • WebSocket: 104 models + 18 handlers")
    print("   • HTTP APIs: 3 clients (Main, Public, OAuth2)")
    print("   • Main client: WhiteBitClient with all APIs")
    print("\n🧪 Test it:")
    print("   python3 run.py")
    print("   python3 test.py")
    print("   make test-import")
    print("\n✨ Ready to use!")
    print()

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
