'''Module that implements the kraken Spot websocket clients'''
import logging
import json
import time
import asyncio
from enum import Enum
from random import random
import traceback
from typing import List
import websockets

try:
    from whitebit.trade.account.account import TradeAccountClient
except ModuleNotFoundError:
    print('USING LOCAL MODULE')
    import sys

    sys.path.append('/Users/Documents/repositories/Whitebit/python-sdk')
    from whitebit.trade.account.account import TradeAccountClient


class ConnectWebsocket:
    __TIME_REQUEST = "ping"
    __AUTHORIZE_REQUEST = "authorize"

    MAX_RECONNECT_NUM = 10

    def __init__(self, client, url: str, callback, token: str = ''):
        self.__client = client
        self.__ws_url = url
        self.__callback = callback

        self.__reconnect_num = 0
        self.__ws_conn_authed = None

        self._token = token

        self.__last_ping = None
        self.__socket = None
        self.__subscriptions = []

        asyncio.ensure_future(
            self.__run_forever(),
            loop=asyncio.get_running_loop()
        )

    @property
    def subscriptions(self) -> list:
        '''Returns the active subscriptions'''
        return self.__subscriptions

    async def __run(self, event: asyncio.Event):
        keep_alive = True
        self.__last_ping = time.time()

        async with websockets.connect(f'{self.__ws_url}', ping_interval=None) as socket:
            logging.info('Websocket connected!')
            self.__socket = socket

            if not event.is_set():
                await self.send_ping()
                event.set()
            self.__reconnect_num = 0

            while keep_alive:
                if time.time() - self.__last_ping > 10: await self.send_ping()
                try:
                    _msg = await asyncio.wait_for(self.__socket.recv(), timeout=15)
                except asyncio.TimeoutError:
                    await self.send_ping()
                except asyncio.CancelledError:
                    logging.exception('asyncio.CancelledError')
                    keep_alive = False
                    await self.__callback({'error': 'asyncio.CancelledError'})
                else:
                    try:
                        msg = json.loads(_msg)
                    except ValueError:
                        logging.warning(_msg)
                    else:
                        if 'result' in msg and msg["id"] == 0:
                            continue
                        await self.__callback(msg)

    async def __run_forever(self) -> None:
        try:
            while True: await self.__reconnect()
        except Exception("MaxReconnectError"):
            await self.__callback({'error': 'MaxReconnectError'})
        except Exception as execption:
            self.__callback({'error': f'{execption}: {traceback.format_exc()}'})
        finally:
            self.__client.exception_occur = True

    async def __reconnect(self):
        logging.info('Websocket start connect/reconnect ' + websockets.version.tag)

        self.__reconnect_num += 1
        if self.__reconnect_num >= self.MAX_RECONNECT_NUM:
            raise Exception("MaxReconnectError")

        reconnect_wait = self.__get_reconnect_wait(self.__reconnect_num)
        logging.debug(
            f'asyncio sleep reconnect_wait={reconnect_wait} s reconnect_num={self.__reconnect_num}'
        )
        await asyncio.sleep(reconnect_wait)
        logging.debug('asyncio sleep done')
        event = asyncio.Event()

        tasks = {
            asyncio.ensure_future(self.__recover_subscriptions(event)): self.__recover_subscriptions,
            asyncio.ensure_future(self.__run(event)): self.__run
        }

        while set(tasks.keys()):
            finished, pending = await asyncio.wait(tasks.keys(), return_when=asyncio.FIRST_EXCEPTION)
            exception_occur = False
            for task in finished:
                if task.exception():
                    exception_occur = True
                    traceback.print_stack()
                    message = f'{task} got an exception {task.exception()}\n {task.get_stack()}'
                    logging.warning(message)
                    for process in pending:
                        logging.warning(f'pending {process}')
                        try:
                            process.cancel()
                        except asyncio.CancelledError:
                            logging.exception('asyncio.CancelledError')
                        logging.warning('Cancel OK')
                    await self.__callback({'error': message})
            if exception_occur: break
        logging.warning('reconnect over')

    async def __recover_subscriptions(self, event):
        logging.info(
            f'Recover subscriptions {self.__subscriptions} waiting.'
        )
        await event.wait()

        await self.auth()
        time.sleep(1)

        for sub in self.__subscriptions:
            await self.send_message(sub)
            logging.info(f'{sub} OK')

        logging.info(
            f'Recovering subscriptions {self.__subscriptions} done.'
        )

    async def send_ping(self):
        msg = {
            'id': 0,
            'method': self.__TIME_REQUEST,
            'params': []
        }
        await self.__socket.send(json.dumps(msg))
        self.__last_ping = time.time()

    async def send_message(self, msg):
        while not self.__socket: await asyncio.sleep(.4)
        await self.__socket.send(json.dumps(msg))

    def append_subscription(self, sub_data: dict) -> None:
        self.remove_subscription(sub_data)  # remove from list, to avoid duplicates
        self.__subscriptions.append(sub_data)

    def remove_subscription(self, sub_data: dict) -> None:
        self.__subscriptions = [x for x in self.__subscriptions if x["method"] != sub_data["method"]]

    def __get_reconnect_wait(self, attempts: int) -> float:
        return round(random() * min(60 * 3, (2 ** attempts) - 1) + 1)

    @property
    def token(self):
        return self._token

    async def auth(self):
        msg = {
            'id': int(time.time() * 1000),
            'method': self.__AUTHORIZE_REQUEST,
            'params': [self.token, "python sdk"]
        }
        await self.send_message(msg)


class WhitebitWsClient(TradeAccountClient):
    PROD_ENV_URL = 'wss://api.whitebit.com/ws'

    __AUTHORIZE_REQUEST = "authorize"
    __TIME_REQUEST = "time"
    __PING_REQUEST = "ping"
    __KLINE_REQUEST = "candles_request"
    __KLINE_SUBSCRIBE = "candles_subscribe"
    KLINE_UPDATE = "candles_update"
    __KLINE_UNSUBSCRIBE = "candles_unsubscribe"

    __DEPTH_REQUEST = "depth_request"
    __DEPTH_SUBSCRIBE = "depth_subscribe"
    DEPTH_UPDATE = "depth_update"
    __DEPTH_UNSUBSCRIBE = "depth_unsubscribe"

    __LAST_PRICE_REQUEST = "lastprice_request"
    __LAST_PRICE_SUBSCRIBE = "lastprice_subscribe"
    LAST_PRICE_UPDATE = "lastprice_update"
    __LAST_PRICE_UNSUBSCRIBE = "lastprice_unsubscribe"

    __MARKET_STAT_REQUEST = "market_request"
    __MARKET_STAT_SUBSCRIBE = "market_subscribe"
    MARKET_STAT_UPDATE = "market_update"
    __MARKET_STAT_UNSUBSCRIBE = "market_unsubscribe"

    __MARKET_STAT_TODAY_REQUEST = "marketToday_query"
    __MARKET_STAT_TODAY_SUBSCRIBE = "marketToday_subscribe"
    MARKET_STAT_TODAY_UPDATE = "marketToday_update"
    __MARKET_STAT_TODAY_UNSUBSCRIBE = "marketToday_unsubscribe"

    __TRADES_REQUEST = "trades_request"
    __TRADES_SUBSCRIBE = "trades_subscribe"
    TRADES_UPDATE = "trades_update"
    __TRADES_UNSUBSCRIBE = "trades_unsubscribe"

    __ORDER_PENDING_REQUEST = "ordersPending_request"
    __ORDERS_PENDING_SUBSCRIBE = "ordersPending_subscribe"
    ORDERS_PENDING_UPDATE = "ordersPending_update"
    __ORDERS_PENDING_UNSUBSCRIBE = "ordersPending_unsubscribe"

    __DEALS_REQUEST = "deals_request"
    __DEALS_SUBSCRIBE = "deals_subscribe"
    DEALS_UPDATE = "deals_update"
    __DEALS_UNSUBSCRIBE = "deals_unsubscribe"

    __SPOT_BALANCE_REQUEST = "balanceSpot_request"
    __SPOT_BALANCE_SUBSCRIBE = "balanceSpot_subscribe"
    SPOT_BALANCE_UPDATE = "balanceSpot_update"
    __SPOT_BALANCE_UNSUBSCRIBE = "balanceSpot_unsubscribe"

    __ORDERS_EXECUTED_REQUEST = "ordersExecuted_request"
    __ORDERS_EXECUTED_SUBSCRIBE = "ordersExecuted_subscribe"
    ORDERS_EXECUTED_UPDATE = "ordersExecuted_update"
    __ORDERS_EXECUTED_UNSUBSCRIBE = "ordersExecuted_unsubscribe"

    __MARGIN_BALANCE_REQUEST = "balanceMargin_request"
    __MARGIN_BALANCE_SUBSCRIBE = "balanceMargin_subscribe"
    MARGIN_BALANCE_UPDATE = "balanceMargin_update"
    __MARGIN_BALANCE_UNSUBSCRIBE = "balanceMargin_unsubscribe"

    def __init__(self, key: str = '', secret: str = '',
                 callback=None):
        super().__init__(api_key=key, api_secret=secret)
        self.__callback = callback
        token = self.get_ws_token()
        self.exception_occur = False
        self._conn = ConnectWebsocket(
            client=self,
            url=self.PROD_ENV_URL,
            token=token["websocket_token"],
            callback=self.on_message
        )

    async def on_message(self, msg: dict):
        if self.__callback is not None:
            await self.__callback(msg)
        else:
            logging.warning('Received event but no callback is defined')
            print(msg)

    async def __subscribe(self, subscription: dict) -> None:
        self._conn.append_subscription(subscription)
        await self._conn.send_message(subscription)

    async def __unsubscribe(self, subscription: dict) -> None:
        self._conn.remove_subscription(subscription)
        await self._conn.send_message(subscription)

    async def get_authorize(self, token: str, com_id=int(time.time() * 1000)):
        await self._conn.send_message(
            {'id': com_id,
             'method': self.__AUTHORIZE_REQUEST,
             'params': [token, 'python-sdk']})

    async def get_spot_balance(self, assets: List[str], com_id=int(time.time() * 1000)):
        assets_as_interface = [i for i in assets]
        await self._conn.send_message(
            {'id': com_id,
             'method': self.__SPOT_BALANCE_REQUEST,
             'params': assets_as_interface})

    async def subscribe_spot_balance(self, assets: List[str], com_id=int(time.time() * 1000)):
        assets_as_interface = [i for i in assets]
        await self.__subscribe(
            {'id': com_id,
             'method': self.__SPOT_BALANCE_SUBSCRIBE,
             'params': assets_as_interface})

    async def unsubscribe_spot_balance(self, com_id=int(time.time() * 1000)):
        await self.__unsubscribe(
            {'id': com_id,
             'method': self.__SPOT_BALANCE_UNSUBSCRIBE,
             'params': []})

    async def get_margin_balance(self, assets: List[str], com_id=int(time.time() * 1000)):
        assets_as_interface = [asset for asset in assets]
        await self._conn.send_message(
            {'id': com_id,
             'method': self.__MARGIN_BALANCE_REQUEST,
             'params': assets_as_interface})

    async def subscribe_margin_balance(self, assets: List[str], com_id=int(time.time() * 1000)):
        assets_as_interface = [asset for asset in assets]
        await self.__subscribe(
            {'id': com_id,
             'method': self.__MARGIN_BALANCE_SUBSCRIBE,
             'params': assets_as_interface})

    async def unsubscribe_margin_balance(self, com_id=int(time.time() * 1000)):
        await self.__unsubscribe(
            {'id': com_id,
             'method': self.__MARGIN_BALANCE_UNSUBSCRIBE,
             'params': []})

    async def get_pending_orders(self, market: str, offset: int = 0, limit: int = 100, com_id=int(time.time() * 1000)):
        await self._conn.send_message({
            'id': com_id,
            'method': self.__ORDER_PENDING_REQUEST,
            'params': [market, offset, limit]})

    async def subscribe_pending_orders(self, markets: List[str], com_id=int(time.time() * 1000)):
        markets_as_interface = [market for market in markets]
        await self.__subscribe(
            {'id': com_id,
             'method': self.__ORDERS_PENDING_SUBSCRIBE,
             'params': markets_as_interface})

    async def unsubscribe_pending_orders(self, com_id=int(time.time() * 1000)):
        await self.__unsubscribe(
            {'id': com_id,
             'method': self.__ORDERS_PENDING_UNSUBSCRIBE,
             'params': []})

    class GetOrdersExecFilter(Enum):
        LIMIT = 1
        MARKET = 2
        MARKET_STOCK = 202
        STOP_LIMIT = 3
        STOP_MARKET = 4
        MARGIN_LIMIT = 7
        MARGIN_MARKET = 8
        MARGIN_STOP_LIMIT = 9
        MARGIN_TRIGGER_STOP_MARKET = 10
        MARGIN_NORMALIZATION = 14

    async def get_orders_executed(self, market: str, order_types: List[int], offset: int = 0, limit: int = 100,
                                  com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__ORDERS_EXECUTED_REQUEST,
            'params': [
                {
                    'market': market,
                    'order_types': order_types
                },
                offset,
                limit
            ]
        }
        await self._conn.send_message(msg)

    class OrdersSubscribeExecFilter(Enum):
        ALL = 0
        LIMIT = 1
        MARKET = 2

    async def subscribe_orders_executed(self, markets: List[str], order_filter: OrdersSubscribeExecFilter,
                                        com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__ORDERS_EXECUTED_SUBSCRIBE,
            'params': [markets, order_filter]
        }
        await self.__subscribe(msg)

    async def unsubscribe_orders_executed(self, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__ORDERS_EXECUTED_UNSUBSCRIBE,
            'params': []
        }
        await self.__unsubscribe(msg)

    async def get_deals(self, market: str, offset: int = 0, limit: int = 100, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__DEALS_REQUEST,
            'params': [market, offset, limit],
        }
        await self._conn.send_message(msg)

    async def subscribe_deals(self, markets: List[str], com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__DEALS_SUBSCRIBE,
            'params': [markets]
        }
        await self.__subscribe(msg)

    async def unsubscribe_deals(self, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__DEALS_UNSUBSCRIBE,
            'params': []
        }
        await self.__unsubscribe(msg)

    async def send_ping(self, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__PING_REQUEST,
            'params': []
        }
        await self._conn.send_message(msg)

    async def get_time(self, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__TIME_REQUEST,
            'params': []
        }
        await self._conn.send_message(msg)

    async def get_kline(self, market: str, start_time: int, end_time: int, interval: int,
                        com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__KLINE_REQUEST,
            'params': [market, start_time, end_time, interval]
        }
        await self._conn.send_message(msg)

    async def subscribe_kline(self, market: str, interval: int, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__KLINE_SUBSCRIBE,
            'params': [market, interval]
        }
        await self.__subscribe(msg)

    async def unsubscribe_kline(self, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__KLINE_UNSUBSCRIBE,
            'params': []
        }
        await self.__unsubscribe(msg)

    async def get_last_price(self, market: str, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__LAST_PRICE_REQUEST,
            'params': [market]
        }
        await self._conn.send_message(msg)

    async def subscribe_last_price(self, market: List[str], com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__LAST_PRICE_SUBSCRIBE,
            'params': market
        }
        await self.__subscribe(msg)

    async def unsubscribe_last_price(self, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__LAST_PRICE_UNSUBSCRIBE,
            'params': []
        }
        await self.__unsubscribe(msg)

    async def get_market_stat(self, market: str, period: int, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__MARKET_STAT_REQUEST,
            'params': [market, period]
        }
        await self._conn.send_message(msg)

    async def subscribe_market_stat(self, market: List[str], com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__MARKET_STAT_SUBSCRIBE,
            'params': market
        }
        await self.__subscribe(msg)

    async def unsubscribe_market_stat(self, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__MARKET_STAT_UNSUBSCRIBE,
            'params': []
        }
        await self.__unsubscribe(msg)

    async def get_market_stat_today(self, market: str, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__MARKET_STAT_TODAY_REQUEST,
            'params': [market]
        }
        await self._conn.send_message(msg)

    async def subscribe_market_stat_today(self, market: List[str], com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__MARKET_STAT_TODAY_SUBSCRIBE,
            'params': market
        }
        await self.__subscribe(msg)

    async def unsubscribe_market_stat_today(self, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__MARKET_STAT_TODAY_UNSUBSCRIBE,
            'params': []
        }
        await self.__unsubscribe(msg)

    async def get_market_trades(self, market: str, limit: int = 0, start_trade_id: int = 0,
                                com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__TRADES_REQUEST,
            'params': [market, limit, start_trade_id]
        }
        await self._conn.send_message(msg)

    async def subscribe_market_trades(self, market: List[str], com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__TRADES_SUBSCRIBE,
            'params': market
        }
        await self.__subscribe(msg)

    async def unsubscribe_market_trades(self, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__TRADES_UNSUBSCRIBE,
            'params': []
        }
        await self.__unsubscribe(msg)

    async def get_market_depth(self, market: str, price_interval: str = "0", limit: int = 100,
                               com_id=int(time.time() * 1000)):
        """Support price intervals ["0.00000001", "0.0000001", "0.000001", "0.00001", "0.0001", "0.001", "0.01",
                                        "0.1", "0"] """
        market_depth_filter_variants = ["0.00000001", "0.0000001", "0.000001", "0.00001", "0.0001", "0.001", "0.01",
                                        "0.1", "0"]
        if price_interval not in market_depth_filter_variants:
            logging.warning("You should use only this interval variants = " + str(market_depth_filter_variants))
            return
        msg = {
            'id': com_id,
            'method': self.__DEPTH_REQUEST,
            'params': [market, limit, price_interval]
        }
        await self._conn.send_message(msg)

    async def subscribe_market_depth(self, market: str, price_interval: str = "0", limit: int = 100,
                                     multiple_sub: bool = False, com_id=int(time.time() * 1000)):
        """Support price intervals ["0.00000001", "0.0000001", "0.000001", "0.00001", "0.0001", "0.001", "0.01",
                                        "0.1", "0"] """
        market_depth_filter_variants = ["0.00000001", "0.0000001", "0.000001", "0.00001", "0.0001", "0.001", "0.01",
                                        "0.1", "0"]
        if price_interval not in market_depth_filter_variants:
            logging.warning("You should use only this interval variants = " + str(market_depth_filter_variants))
            return
        msg = {
            'id': com_id,
            'method': self.__DEPTH_SUBSCRIBE,
            'params': [market, limit, price_interval, multiple_sub]
        }
        await self.__subscribe(msg)

    async def unsubscribe_market_depth(self, com_id=int(time.time() * 1000)):
        msg = {
            'id': com_id,
            'method': self.__DEPTH_UNSUBSCRIBE,
            'params': []
        }
        await self.__unsubscribe(msg)
