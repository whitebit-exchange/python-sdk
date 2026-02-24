"""
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

__version__ = "0.1.0"

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
