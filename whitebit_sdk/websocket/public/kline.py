"""WebSocket handler for WhiteBit Kline Data."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class CandlesHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Kline Data WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Kline Data"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Kline Data."""
        method = "candles_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Kline Data updates."""
        method = "candles_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("candles_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Kline Data."""
        method = "candles_unsubscribe"
        await self.send_request(method, [])
