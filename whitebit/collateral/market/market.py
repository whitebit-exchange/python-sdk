import whitebit
from whitebit.client import Whitebit


class CollateralMarketClient(Whitebit):
    __COLLATERAL_MARKETS_ENDPOINT = "/api/v4/public/collateral/markets"
    __FUTURES_MARKETS_ENDPOINT = "/api/v4/public/futures"

    def get_markets_info(self):
        return self._request(method='GET', uri=self.__COLLATERAL_MARKETS_ENDPOINT, auth=False)

    def get_futures_markets(self):
        return self._request(method='GET', uri=self.__FUTURES_MARKETS_ENDPOINT, auth=False)
