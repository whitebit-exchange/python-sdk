"""WebSocket handler for WhiteBit Market Today Statistics."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class MarkettodayHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Market Today Statistics WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Market Today Statistics"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Market Today Statistics."""
        method = "marketToday_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Market Today Statistics updates."""
        method = "marketToday_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("marketToday_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Market Today Statistics."""
        method = "marketToday_unsubscribe"
        await self.send_request(method, [])
