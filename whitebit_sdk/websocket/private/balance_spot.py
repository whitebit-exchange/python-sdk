"""WebSocket handler for WhiteBit Spot Balance."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class BalancespotHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Spot Balance WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Spot Balance"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Spot Balance."""
        method = "balanceSpot_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Spot Balance updates."""
        method = "balanceSpot_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("balanceSpot_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Spot Balance."""
        method = "balanceSpot_unsubscribe"
        await self.send_request(method, [])
