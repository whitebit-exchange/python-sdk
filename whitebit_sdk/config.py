"""SDK configuration management."""

from dataclasses import dataclass
from typing import Optional


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
