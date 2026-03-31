import json
import unittest

import requests
import responses
from whitebit.trade.market.market import TradeMarketClient
from whitebit.trade.account.account import TradeAccountClient
from whitebit.trade.order.order import TradeOrderClient

from whitebit.collateral.market.market import CollateralMarketClient
from whitebit.collateral.account.account import CollateralAccountClient
from whitebit.collateral.order.order import CollateralOrderClient

from whitebit.main.account.account import MainAccountClient


class MyTestCase(unittest.TestCase):
    @responses.activate
    def test_trade_private_query_without_api_key(self):
        account = TradeAccountClient()
        with self.assertRaises(ValueError):
            account.get_balance()

        order = TradeOrderClient()
        with self.assertRaises(ValueError):
            order.cancel_order("DBTC_DUSDT", 1)


    @responses.activate
    def test_trade_account_negative(self):
        responses.add(responses.POST, 'https://whitebit.com/api/v4/trade-account/balance',
                      json={'error': 'not found'}, status=404)

        account = TradeAccountClient("1a11c", "z1b0r1")

        with self.assertRaises(Exception):
            account.get_balance("B_T_C")

    @responses.activate
    def test_trade_account_positive(self):
        expected_response = {"BTC": {"main_balance": "1.1234"},
                             "ETH": {"main_balance": "0"},
                             "USD": {"main_balance": "0"}}
        responses.add(responses.POST,
                      'https://whitebit.com/api/v4/trade-account/balance',
                      json=expected_response,
                      status=200)

        account = TradeAccountClient("111", "111")

        response = account.get_balance("BTC")

        req = json.loads(responses.calls[0].request.body)
        req["nonce"] = 0
        expected_req = {'ticker': 'BTC', 'request': '/api/v4/trade-account/balance', 'nonce': 0, 'nonceWindow': True}

        assert responses.calls[0].request.url == 'https://whitebit.com/api/v4/trade-account/balance'
        assert req == expected_req
        assert responses.calls[0].request.method == "POST"

        assert response == expected_response

        assert len(responses.calls) == 1
        assert str(responses.calls[0].response.json()) == str(response)

    @responses.activate
    def test_trade_order_negative(self):
        responses.add(responses.POST, 'https://whitebit.com/api/v4/trade-account/balance',
                      json={'error': 'not found'}, status=404)

        account = TradeAccountClient("1a11c", "z1b0r1")

        with self.assertRaises(Exception):
            account.get_balance("B_T_C")

    @responses.activate
    def test_trade_order_positive(self):
        expected_response = {
            "orderId": 11,
            "clientOrderId": "customId11",
            "market": "DBTC_DUSDT",
            "side": "buy",
            "type": "stop market",
            "timestamp": 1595792396.165973,
            "dealMoney": "0",
            "dealStock": "0",
            "amount": "0.001",
            "takerFee": "0.001",
            "makerFee": "0.001",
            "left": "0.001",
            "dealFee": "0",
            "price": "40000",
            "activation_price": "40000"
        }
        responses.add(responses.POST,
                      'https://whitebit.com/api/v4/order/cancel',
                      json=expected_response,
                      status=200)

        order = TradeOrderClient("111", "111")

        response = order.cancel_order("DBTC_DUSDT", 11)

        req = json.loads(responses.calls[0].request.body)
        req["nonce"] = 0
        expected_req = {'market': 'DBTC_DUSDT', 'orderId': 11, 'request': '/api/v4/order/cancel', 'nonce': 0,
                        'nonceWindow': True}

        assert responses.calls[0].request.url == 'https://whitebit.com/api/v4/order/cancel'
        assert req == expected_req
        assert responses.calls[0].request.method == "POST"

        assert response == expected_response

        assert len(responses.calls) == 1
        assert str(responses.calls[0].response.json()) == str(response)


class MainAccountTestCase(unittest.TestCase):
    @responses.activate
    def test_main_account_no_api_key(self):
        client = MainAccountClient()
        with self.assertRaises(ValueError):
            client.get_balance("BTC")

    @responses.activate
    def test_main_account_balance_positive(self):
        expected_response = {"BTC": {"main_balance": "2.5"}}
        responses.add(
            responses.POST,
            'https://whitebit.com/api/v4/main-account/balance',
            json=expected_response,
            status=200,
        )

        client = MainAccountClient("key", "secret")
        response = client.get_balance("BTC")

        req = json.loads(responses.calls[0].request.body)
        assert req["ticker"] == "BTC"
        assert req["request"] == "/api/v4/main-account/balance"
        assert response == expected_response

    @responses.activate
    def test_main_account_balance_negative(self):
        responses.add(
            responses.POST,
            'https://whitebit.com/api/v4/main-account/balance',
            json={'error': 'unauthorized'},
            status=401,
        )

        client = MainAccountClient("bad_key", "bad_secret")
        with self.assertRaises(Exception):
            client.get_balance("BTC")

    @responses.activate
    def test_main_account_get_fee(self):
        expected_response = {"BTC": {"deposit": "0", "withdraw": "0.0004"}}
        responses.add(
            responses.POST,
            'https://whitebit.com/api/v4/main-account/fee',
            json=expected_response,
            status=200,
        )

        client = MainAccountClient("key", "secret")
        response = client.get_fee()

        assert response == expected_response
        assert responses.calls[0].request.method == "POST"


class CollateralOrderTestCase(unittest.TestCase):
    @responses.activate
    def test_collateral_no_api_key(self):
        client = CollateralOrderClient()
        with self.assertRaises(ValueError):
            client.cancel_order("BTC_USDT", 1)

    @responses.activate
    def test_collateral_limit_order_positive(self):
        expected_response = {
            "orderId": 99,
            "market": "BTC_USDT",
            "side": "buy",
            "type": "collateral limit",
            "amount": "0.001",
            "price": "30000",
        }
        responses.add(
            responses.POST,
            'https://whitebit.com/api/v4/order/collateral/limit',
            json=expected_response,
            status=200,
        )

        client = CollateralOrderClient("key", "secret")
        response = client.put_limit("BTC_USDT", "buy", "0.001", "30000")

        req = json.loads(responses.calls[0].request.body)
        assert req["market"] == "BTC_USDT"
        assert req["side"] == "buy"
        assert req["amount"] == "0.001"
        assert req["price"] == "30000"
        assert response == expected_response

    @responses.activate
    def test_collateral_cancel_order_positive(self):
        expected_response = {"orderId": 99, "market": "BTC_USDT"}
        responses.add(
            responses.POST,
            'https://whitebit.com/api/v4/order/cancel',
            json=expected_response,
            status=200,
        )

        client = CollateralOrderClient("key", "secret")
        response = client.cancel_order("BTC_USDT", 99)

        req = json.loads(responses.calls[0].request.body)
        assert req["market"] == "BTC_USDT"
        assert req["orderId"] == 99
        assert response == expected_response

    @responses.activate
    def test_collateral_cancel_order_negative(self):
        responses.add(
            responses.POST,
            'https://whitebit.com/api/v4/order/cancel',
            json={'error': 'order not found'},
            status=404,
        )

        client = CollateralOrderClient("key", "secret")
        with self.assertRaises(Exception):
            client.cancel_order("BTC_USDT", 0)


if __name__ == '__main__':
    unittest.main()
