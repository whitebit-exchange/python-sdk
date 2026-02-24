"""WebSocket handler for WhiteBit Orders Executed."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class OrdersexecutedHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Orders Executed WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Orders Executed"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Orders Executed."""
        method = "ordersExecuted_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Orders Executed updates."""
        method = "ordersExecuted_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("ordersExecuted_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Orders Executed."""
        method = "ordersExecuted_unsubscribe"
        await self.send_request(method, [])
