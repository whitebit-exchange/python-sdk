"""Custom exceptions for WhiteBIT SDK."""


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
