import time
import logging.config

from whitebit.trade.market.market import TradeMarketClient
from whitebit.trade.account.account import TradeAccountClient
from whitebit.trade.order.order import TradeOrderClient

logging.basicConfig(
    format='%(asctime)s %(module)s,line: %(lineno)d %(levelname)8s | %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S',
    level=logging.INFO
)

logging.getLogger().setLevel(logging.INFO)
logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)


def market_examples() -> None:
    """Example usage of the Market client"""
    market = TradeMarketClient()

    print(market.get_tickers())
    print(market.get_markets_info())
    print(market.get_market_activity())
    print(market.get_single_market_activity("BTC_USDT"))
    print(market.get_symbols())
    print(market.get_kline("BTC_USDT"))
    print(market.get_trading_fee())
    print(market.get_fee_list())
    print(market.get_depth("BTC_USDT"))
    print(market.get_order_book(market="BTC_USDT", limit="10", level="0.1"))
    print(market.get_trade_history("BTC_USDT", 123))
    print(market.get_deals("BTC_USDT"))
    print(market.get_assets())
    time.sleep(2)


def account_examples():
    account = TradeAccountClient(api_key="",
                                 api_secret="")
    print(account.get_balance())
    print(account.get_history())
    print(account.get_order_deals(1))
    print(account.get_executed_history())
    print(account.get_unexecuted_orders("BTC_USDT"))
    print(account.get_ping())
    print(account.get_time())
    print(account.get_ws_token())


def order_examples():
    order = TradeOrderClient(api_key="",
                             api_secret="")
    print(order.put_limit("BTC_UzSDT", "sell", "0.1", "40000", True))
    print(order.put_market("BTC_USDT", "buy", "6"))
    print(order.put_market_stock("BTC_USDT", "sell", "0.1"))
    print(order.put_stop_limit("BTC_USDT", "sell", "0.1", "30000", "31000"))
    print(order.put_stop_market("BTC_USDT", "sell", "0.1", "30000"))
    print(order.cancel_order("BTC_USDT", 168935136388))

    bulk_orders = list()
    bulk_orders.append(order.build_limit_order("BTC_USDT", "buy", "0.000199", "20000"))
    bulk_orders.append(
       order.build_limit_order("ETH_USDT", "buy", "0.00428", "1400", post_only=True, ioc=False, client_order_id="myId")
    )
    print(order.limit_bulk(bulk_orders))
    print(order.put_kill_switch("BTC_USDT", "30", [order.ORDER_TYPE_SPOT]))
    print(order.get_kill_switch_status())


def main() -> None:
    market_examples()
    account_examples()
    order_examples()


if __name__ == '__main__':
    main()
