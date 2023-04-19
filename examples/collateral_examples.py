import time
import logging.config

from whitebit.collateral.market.market import CollateralMarketClient
from whitebit.collateral.account.account import CollateralAccountClient
from whitebit.collateral.order.order import CollateralOrderClient

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
    market = CollateralMarketClient()

    print(market.get_markets_info())
    print(market.get_futures_markets())

    time.sleep(2)


def account_examples() -> None:
    account = CollateralAccountClient(api_key="",
                                api_secret="")

    print(account.get_balance())
    print(account.get_open_positions("BTC_USDT"))
    print(account.set_leverage("5"))
    print(account.get_summary())
    print(account.get_positions_history())
    print(account.get_oco_orders("BTC_USDT"))


def order_examples() ->None:
    margin_order = CollateralOrderClient(api_key="",
                        api_secret="")

    print(margin_order.put_limit("BTC_USDT", "sell", "0.1", "40000", True))
    print(margin_order.put_market("BTC_USDT", "sell", "6"))
    print(margin_order.put_oco("BTC_USDT", "sell", "0.1", "30000", "20000", "21000"))
    print(margin_order.put_stop_limit("BTC_USDT", "sell", "0.1", "30000", "31000"))
    print(margin_order.put_stop_market("BTC_USDT", "sell", "0.1", "30000"))
    print(margin_order.cancel_order("BTC_USDT", 168937230825))
    print(margin_order.cancel_oco("BTC_USDT", 168937233685))



def main() -> None:
    market_examples()
    account_examples()
    order_examples()


if __name__ == '__main__':
    main()
