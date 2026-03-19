# WhiteBit Python SDK

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/python-whitebit-sdk.svg)](https://badge.fury.io/py/python-whitebit-sdk)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)

An unofficial Python SDK for the [WhiteBit](https://www.whitebit.com) cryptocurrency exchange API.

> Please read the [WhiteBit API documentation](https://whitebit-exchange.github.io/api-docs/) before using this SDK.

---

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [REST API](#rest-api)
  - [Trade Market (Public)](#trade-market-public)
  - [Trade Account (Private)](#trade-account-private)
  - [Trade Orders (Private)](#trade-orders-private)
  - [Main Account (Private)](#main-account-private)
  - [Collateral Trading (Private)](#collateral-trading-private)
- [WebSocket API](#websocket-api)
- [Examples](#examples)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

---

## Installation

```bash
pip install python-whitebit-sdk
```

Python 3.9 or higher is required.

---

## The Whitebit Base Client

All SDK clients inherit from the `Whitebit` base class located in `whitebit/client.py`. You do not instantiate it directly — instead use the specific clients listed below. It handles:

- **Authentication** — HMAC-SHA512 signature using `X-TXC-APIKEY`, `X-TXC-SIGNATURE`, and `X-TXC-PAYLOAD` headers
- **Nonce** — automatically adds `nonce` (Unix ms timestamp) and `nonceWindow: true` to every private request
- **HTTP transport** — wraps `requests.Session` with `User-Agent: python-whitebit-sdk`
- **Error handling** — raises `Exception` for any non-2xx response

```python
from whitebit.client import Whitebit

# Base class — used internally by all clients
class Whitebit:
    def __init__(self, api_key: str = '', api_secret: str = ''):
        ...

    def _request(self, method, uri, timeout=10, auth=True, params=None, return_raw=False) -> dict:
        ...
```

Private endpoints require credentials — passing empty strings raises `ValueError: Missing credentials.`

---

## Quick Start

```python
from whitebit import TradeMarketClient, TradeAccountClient, TradeOrderClient

# Public endpoints — no credentials required
market = TradeMarketClient()
print(market.get_tickers())

# Private endpoints — API key and secret required
account = TradeAccountClient(api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET")
print(account.get_balance("BTC"))

# Place a limit order
order = TradeOrderClient(api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET")
print(order.put_limit("BTC_USDT", "buy", "0.001", "30000"))
```

Get your API key and secret from your [WhiteBit account settings](https://whitebit.com/settings/api).

---

## REST API

### Trade Market (Public)

No authentication required.

```python
from whitebit import TradeMarketClient

client = TradeMarketClient()

client.get_markets_info()           # All markets info
client.get_tickers()                # All ticker data
client.get_available_tickers()      # Available tickers (v4)
client.get_market_activity()        # All market activity
client.get_single_market_activity("BTC_USDT")
client.get_symbols()                # Available trading symbols
client.get_kline("BTC_USDT", start=1609459200, end=1609545600, interval="1h", limit=100)
client.get_trading_fee()            # Global trading fees
client.get_fee_list()               # Fee list (v4)
client.get_order_book("BTC_USDT", limit=20, level=2)
client.get_depth("BTC_USDT")
client.get_trade_history("BTC_USDT", last_id=0, limit=100)
client.get_deals("BTC_USDT")
client.get_assets()                 # Asset information
```

### Trade Account (Private)

```python
from whitebit import TradeAccountClient

client = TradeAccountClient(api_key="YOUR_KEY", api_secret="YOUR_SECRET")

client.get_balance("BTC")           # Balance for specific ticker
client.get_balance()                # All balances
client.get_order_deals(order_id=12345, offset=0, limit=50)
client.get_executed_history(market="BTC_USDT", offset=0, limit=50)
client.get_history(market="BTC_USDT", offset=0, limit=50)
client.get_unexecuted_orders(market="BTC_USDT")
client.get_ping()
client.get_time()
client.get_ws_token()               # WebSocket authentication token
```

### Trade Orders (Private)

```python
from whitebit import TradeOrderClient

client = TradeOrderClient(api_key="YOUR_KEY", api_secret="YOUR_SECRET")

# Limit order
client.put_limit("BTC_USDT", "buy", "0.001", "30000")
client.put_limit("BTC_USDT", "sell", "0.001", "50000", post_only=True)

# Market order
client.put_market("BTC_USDT", "buy", "10")        # buy $10 worth
client.put_market_stock("BTC_USDT", "buy", "0.001")  # buy 0.001 BTC

# Stop orders
client.put_stop_limit("BTC_USDT", "sell", "0.001", "29000", activation_price="29500")
client.put_stop_market("BTC_USDT", "sell", "0.001", activation_price="29500")

# Cancel an order
client.cancel_order("BTC_USDT", order_id=12345)

# Bulk limit orders
orders = [
    client.build_limit_order("BTC_USDT", "buy", "0.001", "28000"),
    client.build_limit_order("BTC_USDT", "buy", "0.001", "27000"),
]
client.limit_bulk(orders)

# Kill switch — auto-cancel all orders after a timeout
client.put_kill_switch("BTC_USDT", timeout=60, types=["limit"])
client.get_kill_switch_status("BTC_USDT")
```

### Main Account (Private)

```python
from whitebit import MainAccountClient

client = MainAccountClient(api_key="YOUR_KEY", api_secret="YOUR_SECRET")

client.get_balance("BTC")
client.get_fee()
client.get_history(ticker="BTC", offset=0, limit=50)
client.transfer(limit=10, offset=0)

# Transfer codes
client.create_code("USDT", "100", passw="secret", description="Gift")
client.apply_code(code="WBT-...", passw="secret")
client.get_my_codes(limit=10, offset=0)
client.get_codes_history(limit=10, offset=0)

# Custom fees
client.get_custom_fee()
client.get_custom_fee_by_market("BTC_USDT")
```

### Collateral Trading (Private)

```python
from whitebit import CollateralMarketClient, CollateralAccountClient, CollateralOrderClient

# Market info (public)
market = CollateralMarketClient()
market.get_markets_info()
market.get_futures_markets()

# Account (private)
account = CollateralAccountClient(api_key="YOUR_KEY", api_secret="YOUR_SECRET")
account.get_balance("BTC")
account.get_summary()
account.set_leverage(leverage=10)
account.get_open_positions("BTC_USDT")
account.get_positions_history("BTC_USDT", limit=50, offset=0)
account.get_oco_orders("BTC_USDT", offset=0, limit=50)

# Orders (private)
order = CollateralOrderClient(api_key="YOUR_KEY", api_secret="YOUR_SECRET")
order.put_limit("BTC_USDT", "buy", "0.001", "30000")
order.put_market("BTC_USDT", "buy", "0.001")
order.put_stop_limit("BTC_USDT", "sell", "0.001", "29000", activation_price="29500")
order.put_stop_market("BTC_USDT", "sell", "0.001", activation_price="29500")
order.put_oco("BTC_USDT", "sell", "0.001", "31000", activation_price="29500", stop_limit_price="29000")
order.cancel_order("BTC_USDT", order_id=12345)
order.cancel_oco("BTC_USDT", order_id=12345)
```

---

## WebSocket API

Extend `WhitebitWsClient` and implement the `on_message` async callback to receive real-time updates.

```python
import asyncio
import logging
from whitebit import WhitebitWsClient


class Bot(WhitebitWsClient):
    def __init__(self):
        super().__init__(key="YOUR_KEY", secret="YOUR_SECRET")

    async def on_message(self, event) -> None:
        if "result" in event:
            if event["result"] == "pong":
                return
            logging.info("Result: %s", event["result"])
        else:
            method = event.get("method")
            params = event.get("params")
            logging.info("[%s] %s", method, params)


async def main() -> None:
    bot = Bot()

    # Public subscriptions
    await bot.subscribe_last_price(["BTC_USDT", "ETH_USDT"])
    await bot.subscribe_market_trades(["BTC_USDT"])
    await bot.subscribe_market_depth("BTC_USDT", limit=20, interval="0")
    await bot.subscribe_kline("BTC_USDT", interval=60)

    # Private subscriptions (require valid API credentials)
    await bot.subscribe_spot_balance()
    await bot.subscribe_pending_orders(["BTC_USDT"])
    await bot.subscribe_orders_executed(["BTC_USDT"])

    while not bot.exception_occur:
        await asyncio.sleep(10)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```

### Available WebSocket Topics

| Method | Description |
|---|---|
| `subscribe_kline` / `get_kline` | Candlestick (OHLCV) data |
| `subscribe_last_price` / `get_last_price` | Last price updates |
| `subscribe_market_depth` / `get_market_depth` | Order book depth |
| `subscribe_market_stat` / `get_market_stat` | 24h market statistics |
| `subscribe_market_stat_today` / `get_market_stat_today` | Today's market statistics |
| `subscribe_market_trades` / `get_market_trades` | Public trades stream |
| `subscribe_deals` / `get_deals` | Deals stream |
| `subscribe_spot_balance` / `get_spot_balance` | Spot account balance |
| `subscribe_margin_balance` / `get_margin_balance` | Margin account balance |
| `subscribe_pending_orders` / `get_pending_orders` | Open orders updates |
| `subscribe_orders_executed` / `get_orders_executed` | Executed orders |
| `send_ping` | Keep-alive ping |
| `get_time` | Server time |

---

## Examples

Full working examples are in the [`examples/`](examples/) directory:

| File | Description |
|---|---|
| `examples/trade_examples.py` | Spot market, account, and order endpoints |
| `examples/main_examples.py` | Main account endpoints |
| `examples/collateral_examples.py` | Collateral / futures trading |
| `examples/ws_example.py` | WebSocket real-time subscriptions |

---

## Running Tests

```bash
pip install -r requirements.txt
python -m pytest tests/ -v
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on reporting bugs, requesting features, and submitting pull requests.

---

## Disclaimer

The software is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. The author makes no representation that the use of the software will be uninterrupted or error-free. Use at your own risk.