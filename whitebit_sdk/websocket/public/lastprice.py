"""WebSocket handler for WhiteBit Last Price."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class LastpriceHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Last Price WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Last Price"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Last Price."""
        method = "lastprice_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Last Price updates."""
        method = "lastprice_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("lastprice_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Last Price."""
        method = "lastprice_unsubscribe"
        await self.send_request(method, [])
