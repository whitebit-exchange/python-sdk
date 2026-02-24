"""WebSocket handler for WhiteBit Borrows Events."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class BorrowsEventsHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Borrows Events WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Borrows Events"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Borrows Events."""
        method = "borrows_events_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Borrows Events updates."""
        method = "borrows_events_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("borrows_events_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Borrows Events."""
        method = "borrows_events_unsubscribe"
        await self.send_request(method, [])
