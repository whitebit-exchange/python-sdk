import math
import time
import requests
import base64
import hashlib
import hmac
import json


def _create_uri(params) -> str:
    data = ''
    strl = []
    for key in sorted(params):
        strl.append(f'{key}={params[key]}')
    data += '&'.join(strl)
    return f'?{data}'.replace(' ', '%20')


class Whitebit:
    def __init__(self, api_key: str = '', api_secret: str = ''):
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.__url = "http://whitebit.com"
        self.__session = requests.Session()
        self.__session.headers.update({'User-Agent': 'python-whitebit-sdk'})

    def _request(self,
                 method: str = "GET",
                 uri: str = '',
                 timeout: int = 10,
                 auth: bool = True,
                 params: dict = None,
                 return_raw: bool = False
                 ) -> dict:
        if params is None:
            params = {}

        headers = {'Content-Type': 'application/json'}

        if auth:
            self.__create_authed_request(params, headers, uri)
            return self.__check_response_data(
                self.__session.request(method=method, url=self.__url + uri, headers=headers, json=params,
                                       timeout=timeout),
                return_raw
            )

        if params:
            uri += _create_uri(params)
        url = f'{self.__url}{uri}'

        return self.__check_response_data(
            self.__session.request(method=method, url=url, headers=headers, timeout=timeout),
            return_raw
        )

    def __create_authed_request(self, params, headers, uri):
        if not self.__api_key or self.__api_key == '' or not self.__api_secret or self.__api_secret == '': raise ValueError(
            'Missing credentials.')
        params['request'] = uri
        params['nonce'] = int(time.time() * 1000)
        params['nonceWindow'] = True
        headers.update({
            'X-TXC-APIKEY': self.__api_key,
            'X-TXC-SIGNATURE': self.__get_signature(params),
            'X-TXC-PAYLOAD': self.__payload.decode('ascii'),
        })

    def __get_signature(self, data: dict) -> str:
        data_json = json.dumps(data, separators=(',', ':'))  # use separators param for deleting spaces
        self.__payload = base64.b64encode(data_json.encode('ascii'))
        return hmac.new(self.__api_secret.encode('ascii'), self.__payload, hashlib.sha512).hexdigest()

    def __check_response_data(self, response_data, return_raw: bool = False) -> dict:
        if response_data.status_code in ['200', 200, '201', 201]:
            if return_raw:
                return response_data
            try:
                data = response_data.json()
            except ValueError as exc:
                raise ValueError(response_data.content) from exc
            else:
                return data
        raise Exception(f'{response_data.status_code} - {response_data.text}')

    def _to_str_list(self, value) -> str:
        if isinstance(value, str): return value
        if isinstance(value, list): return ','.join(value)
        raise ValueError('a must be type of str or list of strings')
