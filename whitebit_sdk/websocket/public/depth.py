"""WebSocket handler for WhiteBit Order Book Depth."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class DepthHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Order Book Depth WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Order Book Depth"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Order Book Depth."""
        method = "depth_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Order Book Depth updates."""
        method = "depth_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("depth_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Order Book Depth."""
        method = "depth_unsubscribe"
        await self.send_request(method, [])
