"""WebSocket handler for WhiteBit Margin Balance."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class BalancemarginHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Margin Balance WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Margin Balance"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Margin Balance."""
        method = "balanceMargin_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Margin Balance updates."""
        method = "balanceMargin_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("balanceMargin_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Margin Balance."""
        method = "balanceMargin_unsubscribe"
        await self.send_request(method, [])
