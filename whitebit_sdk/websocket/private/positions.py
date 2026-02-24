"""WebSocket handler for WhiteBit Positions."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class PositionsHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Positions WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Positions"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Positions."""
        method = "positions_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Positions updates."""
        method = "positions_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("positions_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Positions."""
        method = "positions_unsubscribe"
        await self.send_request(method, [])
