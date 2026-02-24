"""WebSocket handler for WhiteBit Deals."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class DealsHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Deals WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Deals"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Deals."""
        method = "deals_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Deals updates."""
        method = "deals_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("deals_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Deals."""
        method = "deals_unsubscribe"
        await self.send_request(method, [])
