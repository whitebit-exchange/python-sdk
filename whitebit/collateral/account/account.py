import whitebit
from whitebit.client import Whitebit


class CollateralAccountClient(Whitebit):
    __BALANCE_URL = "/api/v4/collateral-account/balance"
    __LEVERAGE_URL = "/api/v4/collateral-account/leverage"
    __POSITION_HISTORY_URL = "/api/v4/collateral-account/positions/history"
    __OPEN_POSITIONS_URL = "/api/v4/collateral-account/positions/open"
    __SUMMARY_URL = "/api/v4/collateral-account/summary"
    __OCO_ORDERS_URL = "/api/v4/oco-orders"

    def get_balance(self, ticker: str = ""):
        params = {}
        if ticker != "":
            params = {'ticker': ticker}
        return self._request(method='POST', uri=self.__BALANCE_URL, params=params, auth=True)

    def get_summary(self):
        return self._request(method='POST', uri=self.__SUMMARY_URL, auth=True)

    def set_leverage(self, leverage):
        params = {'leverage': leverage}
        return self._request(method='POST', uri=self.__LEVERAGE_URL, params=params, auth=True)

    def get_open_positions(self, market):
        params = {'market': market}
        return self._request(method='POST', uri=self.__OPEN_POSITIONS_URL, params=params, auth=True)

    def get_positions_history(self, market: str = None, position_id: int = None, start_date: int = None,
                              end_date: int = None, limit: str = None, offset: str = None):
        params = {}
        if market is not None:
            params['market'] = market
        if position_id is not None:
            params['positionId'] = position_id
        if start_date is not None:
            params['startDate'] = start_date
        if end_date is not None:
            params['endDate'] = end_date
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        return self._request(method='POST', uri=self.__OPEN_POSITIONS_URL, params=params, auth=True)

    def get_oco_orders(self, market: str, offset: int = None, limit: int = None):
        params = {'market': market}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._request(method='POST', uri=self.__OPEN_POSITIONS_URL, params=params, auth=True)
