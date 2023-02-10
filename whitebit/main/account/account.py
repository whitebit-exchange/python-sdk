import whitebit
from whitebit.client import Whitebit


class MainAccountClient(Whitebit):

    __FEE_URL = "/api/v4/main-account/fee"
    __BALANCE_URL = "/api/v4/main-account/balance"
    __HISTORY_URL = "/api/v4/main-account/history"
    __TRANSFER_URL = "/api/v4/main-account/transfer"

    __CODES_URL = "/api/v4/main-account/codes"
    __CODES_APPLY_URL = "/api/v4/main-account/codes/apply"
    __CODES_MY_URL = "/api/v4/main-account/codes/my"
    __CODES_HISTORY_URL = "/api/v4/main-account/codes/history"

    def transfer(self, limit: int = None, offset: int = None):
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            offset['offset'] = offset
        return self._request(method='POST', uri=self.__TRANSFER_URL, params=params, auth=True)

    def get_fee(self):
        return self._request(method='POST', uri=self.__FEE_URL, auth=True)

    def get_history(self, transaction_method: str = None, ticker: str = None, addresses: [str] = None,
                    unique_id: str = None, status: [int] = None, offset: int = 0, limit: int = 100):
        params = {'offset': offset, 'limit': limit}
        if transaction_method is not None:
            params['transactionMethod'] = transaction_method
        if ticker is not None:
            params['ticker'] = ticker
        if addresses is not None and len(addresses) != 0:
            params['addresses'] = addresses
        if unique_id is not None:
            params['unique_id'] = unique_id
        if status is not None and len(status) != 0:
            params['status'] = status
        return self._request(method='POST', uri=self.__HISTORY_URL, params=params, auth=True)

    def get_balance(self, ticker: str = ""):
        params = {'ticker': ticker}
        return self._request(method='POST', uri=self.__BALANCE_URL, params=params, auth=True)

    def create_Whitebit_code(self, ticker: str, amount: str, passw: str = None, description: str = None):
        params = {'ticker': ticker, "amount": amount}
        if passw is not None:
            params['passphrase'] = passw
        if description is not None:
            params['description'] = description
        return self._request(method='POST', uri=self.__CODES_URL, params=params, auth=True)

    def apply_Whitebit_code(self, code: str, passw: str = None):
        params = {'code': code}
        if passw is not None:
            params['passphrase'] = passw
        return self._request(method='POST', uri=self.__CODES_APPLY_URL, params=params, auth=True)

    def get_my_Whitebit_codes(self, limit: int = None, offset: int = None):
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            offset['offset'] = offset
        return self._request(method='POST', uri=self.__CODES_MY_URL, params=params, auth=True)

    def get_Whitebit_codes_history(self, limit: int = None, offset: int = None):
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            offset['offset'] = offset
        return self._request(method='POST', uri=self.__CODES_HISTORY_URL, params=params, auth=True)
