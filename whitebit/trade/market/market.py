'''Module that implements the Kraken Spot market client'''
import whitebit
from whitebit.client import Whitebit


class TradeMarketClient(Whitebit):
    __MARKETS_URL = "/api/v2/public/markets"
    __MARKET_ACTIVITY_URL = "/api/v2/public/ticker"
    __SINGLE_MARKET_ACTIVITY_URL = "/api/v1/public/ticker"
    __TICKER_URL = "/api/v4/public/ticker"
    __TICKERS_URL = "/api/v1/public/tickers"
    __SYMBOLS_URL = "/api/v1/public/symbols"
    __KLINE_URL = "/api/v1/public/kline"
    __TRADING_FEE_URL = "/api/v2/public/fee"
    __FEE_LIST_URL = "/api/v4/public/fee"
    __DEPTH_URL = "/api/v2/public/depth/"
    __ORDERBOOK_URL = "/api/v4/public/orderbook/"
    __DEALS_URL = "/api/v4/public/trades/"
    __TRADE_HISTORY_URL = "/api/v1/public/history"
    __ASSETS_URL = "/api/v4/public/assets"

    '''Class that implements the Kraken Spot market client'''

    def __init__(self, api_key: str = '', api_secret: str = ''):
        super().__init__(api_key, api_secret)

    def get_markets_info(self):
        return self._request(method='GET', uri=self.__MARKETS_URL, auth=False)

    def get_tickers(self):
        return self._request(method='GET', uri=self.__TICKERS_URL, auth=False)

    def get_available_tickers(self):
        return self._request(method='GET', uri=self.__TICKER_URL, auth=False)

    def get_market_activity(self):
        return self._request(method='GET', uri=self.__MARKET_ACTIVITY_URL, auth=False)

    def get_single_market_activity(self, market):
        params = {'market': market}
        return self._request(method='GET', uri=self.__SINGLE_MARKET_ACTIVITY_URL, params=params, auth=False)

    def get_symbols(self):
        return self._request(method='GET', uri=self.__SYMBOLS_URL, auth=False)

    def get_kline(self, market: str, start: str = None, end: str = None, interval: str = None, limit: str = None):
        params = {'market': market}
        if start is not None:
            params['start'] = start
        if end is not None:
            params['end'] = end
        if interval is not None:
            params['interval'] = interval
        if limit is not None:
            params['limit'] = limit

        return self._request(method='GET', uri=self.__KLINE_URL, params=params, auth=False)

    def get_trading_fee(self):
        return self._request(method='GET', uri=self.__TRADING_FEE_URL, auth=False)

    def get_fee_list(self):
        return self._request(method='GET', uri=self.__FEE_LIST_URL, auth=False)

    def get_order_book(self, market, limit: str = None, level: str = None):
        params = {}
        if limit is not None:
            params['limit'] = limit
        if level is not None:
            params['level'] = level
        return self._request(method='GET', uri=self.__ORDERBOOK_URL + market, params=params, auth=False)

    def get_depth(self, market):
        return self._request(method='GET', uri=self.__DEPTH_URL + market, auth=False)

    def get_trade_history(self, market, last_id, limit: str = None):
        params = {'market': market, 'lastId': last_id}
        if limit is not None:
            params['limit'] = limit
        return self._request(method='GET', uri=self.__TRADE_HISTORY_URL, params=params, auth=False)

    def get_deals(self, market):
        return self._request(method='GET', uri=self.__DEALS_URL + market, auth=False)

    def get_assets(self):
        return self._request(method='GET', uri=self.__ASSETS_URL, auth=False)
