"""WebSocket handler for WhiteBit Orders Pending."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class OrderspendingHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Orders Pending WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Orders Pending"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Orders Pending."""
        method = "ordersPending_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Orders Pending updates."""
        method = "ordersPending_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("ordersPending_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Orders Pending."""
        method = "ordersPending_unsubscribe"
        await self.send_request(method, [])
