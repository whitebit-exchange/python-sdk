'''Module that implements the kraken Spot websocket clients'''
import sys
import logging
import json
import time
import asyncio
from random import random
import traceback
import copy
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
    '''
        This class is only called by the KrakenSpotWSClientCl class
        to establish and handle a websocket connection.

        ====== P A R A M E T E R S ======
        client: kraken.spot.client.KrakenSpotWSClient
            the websocket client
        endpoint: str
            endpoint/url to connect with
        callback: function [optional], default=None
            callback function to call when a message is received
        private: bool [optional], default=False
            if client is authenticated to send signed messages
            and get private feeds

    '''

    __Ping_Request = "ping"
    __Time_Request = "time"

    __Kline_Request = "candles_request"
    __Kline_Subscribe = "candles_subscribe"
    __Kline_Update = "candles_update"
    __Kline_Unsubscribe = "candles_unsubscribe"

    __Depth_Request = "depth_request"
    __Depth_Subscribe = "depth_subscribe"
    __Depth_Update = "depth_update"
    __Depth_Unsubscribe = "depth_unsubscribe"

    __Last_Price_Request = "lastprice_request"
    __Last_Price_Subscribe = "lastprice_subscribe"
    __Last_Price_Update = "lastprice_update"
    __Last_Price_Unsubscribe = "lastprice_unsubscribe"

    __Market_Stat_Request = "market_request"
    __Market_Stat_Subscribe = "market_subscribe"
    __Market_Stat_Update = "market_update"
    __Market_Stat_Unsubscribe = "market_unsubscribe"

    __Market_Stat_Today_Request = "marketToday_query"
    __Market_Stat_Today_Subscribe = "marketToday_subscribe"
    __Market_Stat_Today_Update = "marketToday_update"
    __Market_Stat_Today_Unsubscribe = "marketToday_unsubscribe"

    __Trades_Request = "trades_request"
    __Trades_Subscribe = "trades_subscribe"
    __Trades_Update = "trades_update"
    __Trades_Unsubscribe = "trades_unsubscribe"

    __Order_Pending_Request = "ordersPending_request"
    __Orders_Pending_Subscribe = "ordersPending_subscribe"
    __Orders_Pending_Update = "ordersPending_update"
    __Orders_Pending_Unsubscribe = "ordersPending_unsubscribe"

    __Deals_Request = "deals_request"
    __Deals_Subscribe = "deals_subscribe"
    __Deals_Update = "deals_update"
    __Deals_Unsubscribe = "deals_unsubscribe"

    __Spot_Balance_Request = "balanceSpot_request"
    __Spot_Balance_Subscribe = "balanceSpot_subscribe"
    __Spot_Balance_Update = "balanceSpot_update"
    __Spot_Balance_Unsubscribe = "balanceSpot_unsubscribe"

    __Orders_Executed_Request = "ordersExecuted_request"
    __Orders_Executed_Subscribe = "ordersExecuted_subscribe"
    __Orders_Executed_Update = "ordersExecuted_update"
    __Orders_Executed_Unsubscribe = "ordersExecuted_unsubscribe"

    __Margin_Balance_Request = "balanceMargin_request"
    __Margin_Balance_Subscribe = "balanceMargin_subscribe"
    __Margin_Balance_Update = "balanceMargin_update"
    __Margin_Balance_Unsubscribe = "balanceMargin_unsubscribe"

    MAX_RECONNECT_NUM = 10

    def __init__(self, client, url: str, callback, is_auth: bool=False):
        self.__client = client
        self.__ws_url = url
        self.__callback = callback

        self.__reconnect_num = 0
        self.__ws_conn_authed = None

        self.__is_auth = is_auth

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

    @property
    def is_auth(self) -> bool:
        '''Returns true if the connection can access privat endpoints'''
        return self.__is_auth

    async def __run(self, event: asyncio.Event):
        keep_alive = True
        self.__last_ping = time.time()
        self.__ws_conn_authed = None if not self.__is_auth else self.__client.get_ws_token()
        logging.debug(f'Websocket token: {self.__ws_conn_authed}')

        async with websockets.connect(f'wss://{self.__ws_url}', ping_interval=30) as socket:
            # logging.info('Websocket connected!')
            self.__socket = socket

            if not event.is_set():
                await self.send_ping()
                event.set()
            self.__reconnect_num = 0

            while keep_alive:
                if time.time() - self.__last_ping > 10: await self.send_ping()
                try:
                    _msg = await asyncio.wait_for(self.__socket.recv(), timeout=15)
                except asyncio.TimeoutError: # important
                    await self.send_ping()
                except asyncio.CancelledError:
                    logging.exception('asyncio.CancelledError')
                    keep_alive = False
                    await self.__callback({'error': 'asyncio.CancelledError'})
                else:
                    try: msg = json.loads(_msg)
                    except ValueError: logging.warning(_msg)
                    else:
                        await self.__callback(msg)

    async def __run_forever(self) -> None:
        try:
            while True: await self.__reconnect()
        except Exception("MaxReconnectError"):
            await self.__callback({'error': 'MaxReconnectError'})
        except Exception as execption:
            self.__callback({'error': f'{execption}: {traceback.format_exc()}'})
        finally: self.__client.exception_occur = True

    async def __reconnect(self):
        logging.info('Websocket start connect/reconnect')

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
                        try: process.cancel()
                        except asyncio.CancelledError: logging.exception('asyncio.CancelledError')
                        logging.warning('Cancel OK')
                    await self.__callback({ 'error': message })
            if exception_occur: break
        logging.warning('reconnect over')

    async def __recover_subscriptions(self, event):
        logging.info(
            f'Recover {"auth" if self.__is_auth else "public"} subscriptions {self.__subscriptions} waiting.'
        )
        await event.wait()

        for sub in self.__subscriptions:
            await self.send_message(sub, False)
            logging.info(f'{sub} OK')

        logging.info(
            f'Recovering {"auth" if self.__is_auth else "public"} subscriptions {self.__subscriptions} done.'
        )

    async def send_ping(self):
        msg = {
            'id':  int(time.time() * 1000),
            'method': self.__Ping_Request,
            'params': []
        }
        await self.__socket.send(json.dumps(msg))
        self.__last_ping = time.time()

    async def send_message(self, msg):
        await self.__socket.send(json.dumps(msg))

    def __append_subscription(self, msg: dict) -> None:
        self.__remove_subscription(msg) # remove from list, to avoid duplicates
        self.__subscriptions.append(msg)

    def __remove_subscription(self, msg: dict) -> None:
        self.__subscriptions = [x for x in self.__subscriptions if x != sub]

    def __get_reconnect_wait(self, attempts: int) -> float:
        return round(random() * min(60*3, (2 ** attempts) - 1) + 1)

class WhitebitWSClientCl(TradeAccountClient):
    PROD_ENV_URL = 'wss://api.whitebit.com/ws'

    def __init__(self, key: str='', secret: str='', callback=None):
        super().__init__(api_key=key, api_secret=secret)
        self.__callback = callback
        self.__is_auth = key and secret

        self.exception_occur = False
        self.conn = ConnectWebsocket(
            client=self,
            url=self.PROD_ENV_URL,
            is_auth=False,
            callback=self.on_message
        )

    async def on_message(self, msg: dict):
        ''' Calls the defined callback function (if defined)
            or overload this function

            ====== P A R A M E T E R S ======
            msg: dict
                message received from Kraken via the websocket connection

            ====== N O T E S ======
            Can be overloaded like in the documentation of this class.
        '''
        if self.__callback is not None: await self.__callback(msg)
        else:
            logging.warning('Received event but no callback is defined')
            print(msg)

    async def subscribe(self, subscription: dict, pair: List[str]=None) -> None:
        '''Subscribe to a channel
            https://docs.kraken.com/websockets-beta/#message-subscribe

            ====== P A R A M E T E R S ======
            subscription: dict
                the subscription to subscribe to
            pair: List[str]
                list of asset pairs or list of a single pair

            ====== E X A M P L E ======
            # ... initialize bot as documented on top of this class.
            await bot.subscribe(subscription={"name": ticker}, pair=["XBTUSD", "DOT/EUR"])

            ====== N O T E S ======
            Success or failures are sent over the websocket connection and can be
            received via the on_message callback function.
        '''

        if 'name' not in subscription: raise AttributeError('Subscription requires a "name" key."')
        private = bool(subscription['name'] in self.private_sub_names)

        payload = {
            'event': 'subscribe',
            'subscription': subscription
        }
        if pair is not None:
            if not isinstance(pair, list): raise ValueError('Parameter pair must be type of List[str] (e.g. pair=["XBTUSD"])')
            payload['pair'] = pair

        if private: # private == without pair
            if not self.__is_auth: raise ValueError('Cannot subscribe to private feeds without valid credentials!')
            if pair is not None: raise ValueError('Cannot subscribe to private endpoint with specific pair!')
            await self._priv_conn.send_message(payload, private=True)

        elif pair is not None: # public with pair
            for symbol in pair:
                sub = copy.deepcopy(payload)
                sub['pair'] = [symbol]
                await self._pub_conn.send_message(sub, private=False)

        else: await self._pub_conn.send_message(payload, private=False)

    async def unsubscribe(self, subscription: dict, pair: List[str]=None) -> None:
        '''Unsubscribe from a topic
            https://docs.kraken.com/websockets/#message-unsubscribe

            ====== P A R A M E T E R S ======
            subscription: dict
                the subscription to unsubscribe from
            pair: List[str]
                list of asset pairs or list of a single pair

            ====== E X A M P L E ======
            # ... initialize bot as documented on top of this class.
            bot.unsubscribe(subscription={"name": ticker}, pair=["XBTUSD", "DOT/EUR"])

            ====== N O T E S ======
            Success or failures are sent over the websocket connection and can be
            received via the on_message callback function.
        '''
        if 'name' not in subscription: raise AttributeError('Subscription requires a "name" key."')
        private = bool(subscription['name'] in self.private_sub_names)

        payload = {
            'event': 'unsubscribe',
            'subscription': subscription
        }
        if pair is not None:
            if not isinstance(pair, list): raise ValueError('Parameter pair must be type of List[str] (e.g. pair=["XBTUSD"])')
            payload['pair'] = pair

        if private: # private == without pair
            if not self.__is_auth: raise ValueError('Cannot unsubscribe from private feeds without valid credentials!')
            if pair is not None: raise ValueError('Cannot unsubscribe from private endpoint with specific pair!')
            await self._priv_conn.send_message(payload, private=True)

        elif pair is not None: # public with pair
            for symbol in pair:
                sub = copy.deepcopy(payload)
                sub['pair'] = [symbol]
                await self._pub_conn.send_message(sub, private=False)

        else: await self._pub_conn.send_message(payload, private=False)

