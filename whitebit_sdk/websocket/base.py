"""Base WebSocket handler."""

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

        message = {"id": request_id, "method": method, "params": params}

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
