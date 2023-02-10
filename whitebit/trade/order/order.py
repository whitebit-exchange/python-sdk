import whitebit
from whitebit.client import Whitebit


class TradeOrderClient(Whitebit):
    __ORDER_CANCEL_URL = "/api/v4/order/cancel"
    __LIMIT_URL = "/api/v4/order/new"
    __MARKET_URL = "/api/v4/order/market"
    __MARKET_STOCK_URL = "/api/v4/order/stock_market"
    __STOP_MARKET_URL = "/api/v4/order/stop_market"
    __STOP_LIMIT_URL = "/api/v4/order/stop_limit"

    def put_market(self, market: str, side: str, amount, client_order_id: str = ""):
        params = {
            "market": market,
            "side": side,
            "amount": amount,
        }
        if client_order_id != "":
            params['clientOrderId'] = client_order_id
        return self._request(method='POST', uri=self.__MARKET_URL, params=params, auth=True)

    def put_market_stock(self, market: str, side: str, amount, client_order_id: str = ""):
        params = {
            "market": market,
            "side": side,
            "amount": amount,
        }
        if client_order_id != "":
            params['clientOrderId'] = client_order_id
        return self._request(method='POST', uri=self.__MARKET_STOCK_URL, params=params, auth=True)

    def put_limit(self, market: str, side: str, amount, price, post_only: bool = False, client_order_id: str = ""):
        params = {
            "market": market,
            "side": side,
            "amount": amount,
            "price": price,
            "postOnly": post_only,
        }
        if client_order_id != "":
            params['clientOrderId'] = client_order_id
        return self._request(method='POST', uri=self.__LIMIT_URL, params=params, auth=True)

    def put_stop_limit(self, market: str, side: str, amount, price, activation_price, client_order_id: str = ""):
        params = {
            "market": market,
            "side": side,
            "amount": amount,
            "price": price,
            "activation_price": activation_price,
        }
        if client_order_id != "":
            params['clientOrderId'] = client_order_id
        return self._request(method='POST', uri=self.__STOP_LIMIT_URL, params=params, auth=True)

    def put_stop_market(self, market: str, side: str, amount, activation_price, client_order_id: str = ""):
        params = {
            "market": market,
            "side": side,
            "amount": amount,
            "activation_price": activation_price,
        }
        if client_order_id != "":
            params['clientOrderId'] = client_order_id
        return self._request(method='POST', uri=self.__STOP_MARKET_URL, params=params, auth=True)

    def cancel_order(self, market: str, order_id):
        params = {
            "market": market,
            "orderId": order_id,
        }
        return self._request(method='POST', uri=self.__ORDER_CANCEL_URL, params=params, auth=True)
