import time
import logging.config

from whitebit.main.account.account import MainAccountClient

logging.basicConfig(
    format='%(asctime)s %(module)s,line: %(lineno)d %(levelname)8s | %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S',
    level=logging.INFO
)

logging.getLogger().setLevel(logging.INFO)
logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)


def main_examples() -> None:
    """Example usage of the main account client"""
    account = MainAccountClient(api_key="",
                                api_secret="")

    print(account.get_my_codes())
    print(account.get_codes_history())
    print(account.get_fee())
    print(account.get_balance("USDT"))
    print(account.get_history())
    print(account.create_code("USDT", "10"))
    print(account.apply_code("WB5cb61d11-baa5-40a9-a9ad-ee81f50909f4USDT"))
    print(account.get_custom_fee())
    print(account.get_custom_fee_by_market("BTC_USDT"))

    time.sleep(2)


def main() -> None:
    main_examples()


if __name__ == '__main__':
    main()
