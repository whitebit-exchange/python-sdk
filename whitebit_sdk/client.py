"""WhiteBIT SDK main client."""

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
        markets = await client.public_api.public.get_markets()

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
