import whitebit
from whitebit.client import Whitebit


class TradeAccountClient(Whitebit):
    __BALANCE_URL = "/api/v4/trade-account/balance"
    __ORDER_URL = "/api/v4/trade-account/order"
    __ORDER_HISTORY_URL = "/api/v4/trade-account/order/history"
    __ORDER_EXECUTED_HISTORY_URL = "/api/v4/trade-account/executed-history"
    __ORDERS_URL = "/api/v4/orders"

    def get_balance(self, ticker: str = ""):
        params = {}
        if ticker != "":
            params = {'ticker': ticker}
        return self._request(method='POST', uri=self.__BALANCE_URL, params=params, auth=True)

    def get_order_deals(self, order_id: int, offset: int = None, limit: int = None):
        params = {"orderId": order_id}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._request(method='POST', uri=self.__ORDER_URL, params=params, auth=True)

    def get_executed_history(self, market: str = None, client_order_id: str = None,
                             offset: int = None, limit: int = None):
        params = {}
        if market is not None:
            params["market"] = market
        if client_order_id is not None:
            params["clientOrderId"] = client_order_id
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._request(method='POST', uri=self.__ORDER_EXECUTED_HISTORY_URL, params=params, auth=True)

    def get_history(self, market: str = None, order_id: str = None, client_order_id: str = None,
                    offset: int = None, limit: int = None):
        params = {}
        if market is not None:
            params["market"] = market
        if order_id is not None:
            params["orderId"] = order_id
        if client_order_id is not None:
            params["clientOrderId"] = client_order_id
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._request(method='POST', uri=self.__ORDER_HISTORY_URL, params=params, auth=True)

    def get_unexecuted_orders(self, market, order_id: str = None, client_order_id: str = None,
                              offset: int = None, limit: int = None):
        params = {"market": market}
        if order_id is not None:
            params["orderId"] = order_id
        if client_order_id is not None:
            params["clientOrderId"] = client_order_id
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._request(method='POST', uri=self.__ORDERS_URL, params=params, auth=True)
