#!/usr/bin/env python3
"""Create core SDK infrastructure files."""

import sys
from pathlib import Path

# Base WebSocket Handler
BASE_WS_HANDLER = '''"""Base WebSocket handler."""

import asyncio
from typing import Any, Callable, Dict, Optional

class BaseWebSocketHandler:
    """Base class for all WebSocket handlers."""

    def __init__(self, ws_client):
        self.ws_client = ws_client
        self._update_handlers: Dict[str, Callable] = {}
        self._request_id = 0

    def _get_next_id(self) -> int:
        """Get next request ID."""
        self._request_id += 1
        return self._request_id

    async def send_request(self, method: str, params: list) -> Any:
        """Send request to WebSocket."""
        if not self.ws_client.is_connected:
            raise ConnectionError("WebSocket not connected")

        request_id = self._get_next_id()

        message = {
            "id": request_id,
            "method": method,
            "params": params
        }

        # Send and wait for response
        return await self.ws_client.send_and_wait(message, request_id)

    def register_update_handler(self, method: str, handler: Callable) -> None:
        """Register handler for update messages."""
        self._update_handlers[method] = handler

    async def handle_update(self, message: dict) -> None:
        """Handle update message."""
        method = message.get("method")
        if method in self._update_handlers:
            handler = self._update_handlers[method]
            await handler(message.get("params"))
'''

# Config module
CONFIG_MODULE = '''"""SDK configuration management."""

from typing import Optional
from dataclasses import dataclass

@dataclass
class WhiteBitConfig:
    """WhiteBIT SDK configuration."""

    api_key: Optional[str] = None
    api_secret: Optional[str] = None
    base_url: str = "https://whitebit.com"
    websocket_url: str = "wss://api.whitebit.com/ws"
    timeout: int = 30
    max_retries: int = 3

    @property
    def has_credentials(self) -> bool:
        """Check if API credentials are configured."""
        return bool(self.api_key and self.api_secret)
'''

# Exceptions module
EXCEPTIONS_MODULE = '''"""Custom exceptions for WhiteBIT SDK."""

class WhiteBitAPIException(Exception):
    """Base exception for WhiteBIT API."""
    pass

class AuthenticationError(WhiteBitAPIException):
    """Authentication failed."""
    pass

class AuthorizationError(WhiteBitAPIException):
    """Authorization/permission error."""
    pass

class RateLimitError(WhiteBitAPIException):
    """Rate limit exceeded."""
    pass

class ValidationError(WhiteBitAPIException):
    """Request validation error."""
    pass

class NotFoundError(WhiteBitAPIException):
    """Resource not found."""
    pass

class ServerError(WhiteBitAPIException):
    """Server error (5xx)."""
    pass

class WebSocketError(WhiteBitAPIException):
    """WebSocket connection error."""
    pass

class ConnectionError(WebSocketError):
    """WebSocket connection failed."""
    pass

class SubscriptionError(WebSocketError):
    """WebSocket subscription error."""
    pass
'''

# Signature utility
SIGNATURE_MODULE = '''"""Signature generation utilities."""

import hmac
import hashlib
import base64
import json
from typing import Any, Dict

def generate_signature(payload: str, secret: str) -> str:
    """Generate HMAC-SHA512 signature."""
    signature = hmac.new(
        secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha512
    ).hexdigest()
    return signature

def create_signed_payload(data: Dict[str, Any], secret: str) -> tuple[str, str]:
    """Create signed payload for API request."""
    payload_str = json.dumps(data, separators=(',', ':'))
    payload_b64 = base64.b64encode(payload_str.encode('utf-8')).decode('utf-8')
    signature = generate_signature(payload_b64, secret)
    return payload_b64, signature
'''

# Auth utility
AUTH_MODULE = '''"""Authentication utilities."""

import time
from typing import Dict, Any
from .signature import create_signed_payload

def generate_nonce() -> str:
    """Generate nonce for API request."""
    return str(int(time.time() * 1000))

def create_auth_headers(api_key: str, payload: str, signature: str) -> Dict[str, str]:
    """Create authentication headers."""
    return {
        'X-TXC-APIKEY': api_key,
        'X-TXC-PAYLOAD': payload,
        'X-TXC-SIGNATURE': signature,
        'Content-Type': 'application/json'
    }

def prepare_private_request(endpoint: str, data: Dict[str, Any], api_key: str, api_secret: str) -> tuple[Dict[str, str], str]:
    """Prepare private API request with signature."""
    nonce = generate_nonce()

    request_data = {
        'request': endpoint,
        'nonce': nonce,
        **data
    }

    payload, signature = create_signed_payload(request_data, api_secret)
    headers = create_auth_headers(api_key, payload, signature)

    return headers, payload
'''

def main():
    """Create SDK infrastructure files."""
    print("=" * 50)
    print("Creating SDK Infrastructure")
    print("=" * 50)

    sdk_dir = Path(__file__).parent.parent / "whitebit_sdk"

    files_to_create = [
        (sdk_dir / "websocket" / "base.py", BASE_WS_HANDLER),
        (sdk_dir / "config.py", CONFIG_MODULE),
        (sdk_dir / "exceptions.py", EXCEPTIONS_MODULE),
        (sdk_dir / "utils" / "signature.py", SIGNATURE_MODULE),
        (sdk_dir / "utils" / "auth.py", AUTH_MODULE),
    ]

    print()
    for file_path, content in files_to_create:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created {file_path.relative_to(sdk_dir.parent)}")

    print("\n✓ SDK infrastructure created")
    print("=" * 50)

if __name__ == "__main__":
    main()
