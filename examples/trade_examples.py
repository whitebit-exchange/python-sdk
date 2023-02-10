import time
import logging.config

try:
    from whitebit.trade.market.market import MarketClient
    from whitebit.trade.account.account import TradeAccountClient
    from whitebit.trade.order.order import OrderClient

except ModuleNotFoundError:
    print('USING LOCAL MODULE')
    import sys

    sys.path.append('/Users/Documents/repositories/Whitebit/python-sdk')
    from whitebit.trade.market.market import MarketClient
    from whitebit.trade.account.account import TradeAccountClient
    from whitebit.trade.order.order import OrderClient

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
    market = MarketClient()

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
    account = TradeAccountClient(api_key="2132efca2330cdada2e357f19c0f5593",
                                 api_secret="e6c331d079a7a3e8e774151655190267")
    print(account.get_balance())
    print(account.get_history())
    print(account.get_order_deals(1))
    print(account.get_executed_history())
    print(account.get_unexecuted_orders("BTC_USDT"))


def order_examples():
    order = OrderClient(api_key="5d9183ae33b6dba84996054ba458fd28",
                        api_secret="2708ce93e75bfce1653a3ec4967967fd")

    print(order.put_limit("BTC_USDT", "sell", "0.1", "40000", True))
    print(order.put_market("BTC_USDT", "buy", "6"))
    print(order.put_market_stock("BTC_USDT", "sell", "0.1"))
    print(order.put_stop_limit("BTC_USDT", "sell", "0.1", "30000", "31000"))
    print(order.put_stop_market("BTC_USDT", "sell", "0.1", "30000"))
    print(order.cancel_order("BTC_USDT", 168935136388))


def main() -> None:
    market_examples()
    account_examples()
    order_examples()


if __name__ == '__main__':
    main()
