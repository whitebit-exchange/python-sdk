"""WebSocket handler for WhiteBit Market Trades."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class TradesHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Market Trades WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Market Trades"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Market Trades."""
        method = "trades_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Market Trades updates."""
        method = "trades_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("trades_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Market Trades."""
        method = "trades_unsubscribe"
        await self.send_request(method, [])
