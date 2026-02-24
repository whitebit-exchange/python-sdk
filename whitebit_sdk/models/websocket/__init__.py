"""WebSocket API models generated from AsyncAPI specs."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel

__all__ = []


class AuthorizeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class AuthorizeResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class BalanceMarginRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class BalanceMarginResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class BalanceMarginSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class BalanceMarginUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class BalanceSpotRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class BalanceSpotResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class BalanceSpotSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class BalanceSpotUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class BorrowsSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class BorrowsUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: Dict[str, Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class BorrowsEventsSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class BorrowsEventsUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class DealsRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class DealsResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class DealsSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class DealsUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class MarginPositionsEventsSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class MarginPositionsEventsUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class OrdersExecutedRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class OrdersExecutedResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class OrdersExecutedSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class OrdersExecutedUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class ExecutedOrderObject(BaseModel):
    """Generated from AsyncAPI schema."""

    id: Optional[int] = None
    ctime: Optional[float] = None
    ftime: Optional[float] = None
    mtime: Optional[float] = None
    market: Optional[str] = None
    source: Optional[str] = None
    type: Optional[int] = None
    side: Optional[int] = None
    post_only: Optional[bool] = None
    ioc: Optional[bool] = None
    price: Optional[str] = None
    amount: Optional[str] = None
    left: Optional[str] = None
    deal_stock: Optional[str] = None
    deal_money: Optional[str] = None
    deal_fee: Optional[str] = None
    client_order_id: Optional[str] = None
    stp: Optional[str] = None
    status: Optional[str] = None
    position_side: Optional[str] = None
    rpi: Optional[bool] = None
    fee_asset: Optional[str] = None


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class OrdersPendingRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class OrdersPendingResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class OrdersPendingSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class OrdersPendingUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class OrderObject(BaseModel):
    """Generated from AsyncAPI schema."""

    id: Optional[int] = None
    market: Optional[str] = None
    type: Optional[int] = None
    side: Optional[int] = None
    post_only: Optional[bool] = None
    ioc: Optional[bool] = None
    ctime: Optional[float] = None
    mtime: Optional[float] = None
    price: Optional[str] = None
    amount: Optional[str] = None
    left: Optional[str] = None
    deal_stock: Optional[str] = None
    deal_money: Optional[str] = None
    deal_fee: Optional[str] = None
    client_order_id: Optional[str] = None
    stp: Optional[str] = None
    status: Optional[str] = None
    position_side: Optional[str] = None
    rpi: Optional[bool] = None


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class PositionsSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class PositionsUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: Dict[str, Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class BookTickerSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class BookTickerUpdateData(BaseModel):
    """Generated from AsyncAPI schema."""

    pass


class BookTickerUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class DepthLevel(BaseModel):
    """Generated from AsyncAPI schema."""

    pass


class OrderBook(BaseModel):
    """Generated from AsyncAPI schema."""

    timestamp: float
    asks: List[Any]
    bids: List[Any]


class DepthUpdateData(BaseModel):
    """Generated from AsyncAPI schema."""

    timestamp: float
    update_id: Optional[int] = None
    past_update_id: Optional[int] = None
    asks: List[Any]
    bids: List[Any]
    event_time: float


class DepthRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class DepthResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Any
    error: None


class DepthSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class DepthUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class Candle(BaseModel):
    """Generated from AsyncAPI schema."""

    pass


class CandlesRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class CandlesResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: List[Any]
    error: None


class CandlesSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class CandlesUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class LastpriceRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class LastpriceResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: str
    error: None


class LastpriceSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class LastpriceUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class MarketStatistics(BaseModel):
    """Generated from AsyncAPI schema."""

    period: int
    last: str
    open: str
    close: str
    high: str
    low: str
    volume: str
    deal: str


class MarketRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class MarketResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Any
    error: None


class MarketSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class MarketUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class MarketTodayStatistics(BaseModel):
    """Generated from AsyncAPI schema."""

    last: str
    open: str
    high: str
    low: str
    volume: str
    deal: str


class MarketTodayRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class MarketTodayResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Any
    error: None


class MarketTodaySubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class MarketTodayUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]


class BaseRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int


class BaseResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    error: None


class PingRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    pass


class PingResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    pass


class TimeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    pass


class TimeResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    pass


class Trade(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    time: float
    price: str
    amount: str
    type: str
    rpi: Optional[bool] = None


class TradesRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class TradesResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: List[Any]
    error: None


class TradesSubscribe(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: Any
    params: List[Any]


class SubscriptionResponse(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    result: Dict[str, Any]
    error: None


class TradesUpdate(BaseModel):
    """Generated from AsyncAPI schema."""

    id: None
    method: Any
    params: List[Any]


class UnsubscribeRequest(BaseModel):
    """Generated from AsyncAPI schema."""

    id: int
    method: str
    params: List[Any]
