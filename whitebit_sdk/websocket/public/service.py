"""WebSocket handler for WhiteBit Service Operations."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class TimeHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Service Operations WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Service Operations"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Service Operations."""
        method = "time_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Service Operations updates."""
        method = "time_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("time_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Service Operations."""
        method = "time_unsubscribe"
        await self.send_request(method, [])
