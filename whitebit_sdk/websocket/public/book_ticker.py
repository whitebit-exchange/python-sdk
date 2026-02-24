"""WebSocket handler for WhiteBit Book Ticker."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class BookTickerHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Book Ticker WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Book Ticker"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Book Ticker."""
        method = "book_ticker_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Book Ticker updates."""
        method = "book_ticker_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("book_ticker_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Book Ticker."""
        method = "book_ticker_unsubscribe"
        await self.send_request(method, [])
