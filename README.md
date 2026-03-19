# WhiteBit Python SDK

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/whitebit-python-sdk.svg)](https://badge.fury.io/py/whitebit-python-sdk)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)

An unofficial Python SDK for the [WhiteBit](https://www.whitebit.com) cryptocurrency exchange API.

> Please read the [WhiteBit API documentation](https://docs.whitebit.com/) before using this SDK.

---

## Installation

```bash
pip install whitebit-python-sdk
```

Python 3.9 or higher is required.

---

## Quick Start

### Sync client

```python
from whitebit import WhitebitApi

client = WhitebitApi(txc_apikey="YOUR_API_KEY", token="YOUR_TOKEN")

# Market data (public)
print(client.public_api_v4.get_tickers())

# Spot trading
print(client.spot_trading.get_trade_account_balance(ticker="BTC"))
print(client.spot_trading.create_limit_order(market="BTC_USDT", side="buy", amount="0.001", price="30000"))

# Collateral
print(client.collateral_trading.get_open_positions(market="BTC_USDT"))
```

### Async client

```python
import asyncio
from whitebit import AsyncWhitebitApi

async def main():
    client = AsyncWhitebitApi(txc_apikey="YOUR_API_KEY", token="YOUR_TOKEN")

    # Market data (public)
    tickers = await client.public_api_v4.get_tickers()
    print(tickers)

    # Spot trading
    balance = await client.spot_trading.get_trade_account_balance(ticker="BTC")
    print(balance)

    order = await client.spot_trading.create_limit_order(
        market="BTC_USDT", side="buy", amount="0.001", price="30000"
    )
    print(order)

asyncio.run(main())
```

Get your API key from your [WhiteBit account settings](https://whitebit.com/settings/api).

---

> **Note:** The SDK client (`WhitebitApi` / `AsyncWhitebitApi`) is auto-generated from the WhiteBit API definition using [Fern](https://buildwithfern.com). To report issues or request new endpoints, open an issue — see [Contributing](CONTRIBUTING.md).

## Clients

The SDK exposes two top-level clients — `WhitebitApi` (sync) and `AsyncWhitebitApi` (async). Both share the same sub-client structure:

| Sub-client | Auth | Description |
|---|---|---|
| `client.public_api_v4` | No | Tickers, order books, klines, assets, trades |
| `client.spot_trading` | Yes | Place/cancel spot orders, balance, order history |
| `client.collateral_trading` | Yes | Margin/futures orders, positions, OCO |
| `client.main_account` | Yes | Main balance, deposit/withdraw history |
| `client.deposit` | Yes | Deposit addresses, fiat deposit URLs |
| `client.withdraw` | Yes | Withdrawals |
| `client.transfer` | Yes | Transfer between balances |
| `client.codes` | Yes | Transfer codes (create, apply, history) |
| `client.fees` | Yes | Fee information |
| `client.market_fee` | Yes | Market-specific fees |
| `client.jwt` | Yes | WebSocket JWT token |
| `client.authentication` | Yes | OAuth2 token management |
| `client.sub_account` | Yes | Sub-account management |
| `client.sub_account_api_keys` | Yes | Sub-account API key management |
| `client.crypto_lending_fixed` | Yes | Fixed crypto lending |
| `client.crypto_lending_flex` | Yes | Flex crypto lending |
| `client.credit_line` | Yes | Credit line |
| `client.mining_pool` | Yes | Mining pool stats and management |

---

## Examples

Full working examples are in the [`examples/`](examples/) directory:

### [trade_examples.py](examples/trade_examples.py)

Covers `TradeMarketClient`, `TradeAccountClient`, and `TradeOrderClient`:
- Get tickers, order books, klines, assets
- Get spot balance, order history, unexecuted orders
- Place limit, market, stop-limit, stop-market orders
- Bulk limit orders, kill switch

### [main_examples.py](examples/main_examples.py)

Covers `MainAccountClient`:
- Main account balance and fee info
- Transaction history
- Create and apply transfer codes

### [collateral_examples.py](examples/collateral_examples.py)

Covers `CollateralMarketClient`, `CollateralAccountClient`, `CollateralOrderClient`:
- Futures/collateral market info
- Margin balance, open positions, leverage
- Place and cancel collateral/OCO orders

### [ws_example.py](examples/ws_example.py)

Covers `WhitebitWsClient`:
- Extend the client and implement `on_message` for real-time events
- Subscribe to deals, prices, order book depth, balance, pending orders

---

## WebSocket Topics

| Method | Description |
|---|---|
| `subscribe_kline` / `get_kline` | Candlestick (OHLCV) data |
| `subscribe_last_price` / `get_last_price` | Last price updates |
| `subscribe_market_depth` / `get_market_depth` | Order book depth |
| `subscribe_market_stat` / `get_market_stat` | 24h market statistics |
| `subscribe_market_trades` / `get_market_trades` | Public trades stream |
| `subscribe_deals` / `get_deals` | Deals stream |
| `subscribe_spot_balance` / `get_spot_balance` | Spot account balance |
| `subscribe_margin_balance` / `get_margin_balance` | Margin account balance |
| `subscribe_pending_orders` / `get_pending_orders` | Open orders updates |
| `subscribe_orders_executed` / `get_orders_executed` | Executed orders |

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

The software is provided "as is" without warranty of any kind. Use at your own risk.
