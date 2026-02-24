"""WebSocket handler for WhiteBit Private API Authorization."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class AuthorizeHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Private API Authorization WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Private API Authorization"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Private API Authorization."""
        method = "authorize_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Private API Authorization updates."""
        method = "authorize_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("authorize_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Private API Authorization."""
        method = "authorize_unsubscribe"
        await self.send_request(method, [])
