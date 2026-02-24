"""WebSocket handler for WhiteBit Margin Positions Events."""

import asyncio
from typing import Any, Callable, Optional

from ..base import BaseWebSocketHandler


class MarginPositionsEventsHandler(BaseWebSocketHandler):
    """Handler for WhiteBit Margin Positions Events WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "WhiteBit Margin Positions Events"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to WhiteBit Margin Positions Events."""
        method = "margin_positions_events_request"
        return await self.send_request(method, list(args))

    async def subscribe(
        self, *args, on_update: Optional[Callable] = None, **kwargs
    ) -> None:
        """Subscribe to WhiteBit Margin Positions Events updates."""
        method = "margin_positions_events_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("margin_positions_events_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from WhiteBit Margin Positions Events."""
        method = "margin_positions_events_unsubscribe"
        await self.send_request(method, [])
