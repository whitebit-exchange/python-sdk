"""WebSocket handler for WhiteBit Borrows."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class BorrowsHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Borrows WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Borrows"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Borrows."""
        method = "borrows_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Borrows updates."""
        method = "borrows_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("borrows_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Borrows."""
        method = "borrows_unsubscribe"
        await self.send_request(method, [])
