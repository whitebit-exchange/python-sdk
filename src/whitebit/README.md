<h1 align="center">WhiteBit Python SDK</h1>

<p align="center">
  <strong>Official Python SDK for the WhiteBit API — trade, query, and manage your crypto portfolio programmatically.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-≥ 3.9-3776AB?style=flat-square&logo=python" alt="Python ≥ 3.9" />
  <img src="https://img.shields.io/badge/license-Apache_2.0-green?style=flat-square" alt="Apache 2.0 license" />
</p>

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| **Python ≥ 3.9** | Required runtime |
| **WhiteBit account** | Sign up at [whitebit.com](https://whitebit.com) |
| **WhiteBit API key** | Profile → API keys → Create key (Read and/or Trade permissions) |

---

## Installation

```bash
pip install whitebit-python-sdk
```

---

## Quick Start

### 1. Get your API credentials

1. Log in to [whitebit.com](https://whitebit.com) → **Profile → API keys**
2. Create a new key — choose **Read** and/or **Trade** permissions as needed
3. Copy your **API Key** and **Token**

> Public endpoints (market data, tickers, order book) work without credentials. Private endpoints (account, trading) require both.

### 2. Initialize the client

```python
from whitebit import WhitebitApi

client = WhitebitApi(
    txc_apikey="YOUR_API_KEY",
    token="YOUR_TOKEN",
)
```

---

## Usage Examples

```python
# Market data (no credentials required)
tickers = client.public_api_v4.get_market_activity()
depth   = client.public_api_v4.get_orderbook(market="BTC_USDT")

# Account
balance = client.account_endpoints.get_trading_balance()

# Spot trading
order   = client.spot_trading.create_limit_order(
    market="BTC_USDT", side="buy", amount="0.01", price="95000"
)
client.spot_trading.cancel_order(market="BTC_USDT", order_id=order.order_id)

# Main account — transfer & withdraw
client.transfer.transfer(from_="main", to="spot", ticker="USDT", amount="100")
client.withdraw.create_withdraw(ticker="USDT", amount="500", address="0x...")
```

---

## Available Modules

| Module | Description |
|--------|-------------|
| `public_api_v4` | Tickers, order book, trade history, klines, assets |
| `spot_trading` | Limit, market, stop-limit, stop-market, bulk orders |
| `collateral_trading` | Collateral orders, OCO, positions |
| `account_endpoints` | Trading balance, open orders, order history |
| `main_account` | Main balances, deposit addresses, fee info |
| `transfer` | Transfer between main and trade accounts |
| `withdraw` | Withdrawal requests |
| `codes` | WhiteBit codes — create, apply, history |
| `crypto_lending_fixed` | Fixed lending plans |
| `crypto_lending_flex` | Flex lending plans |
| `fees` | Trading fees |
| `sub_account` | Sub-account management |
| `mining_pool` | Hashrate and rewards |

---

## Resources

| | |
|---|---|
| [WhiteBIT API Documentation](https://docs.whitebit.com) | Official API reference |
| [API Platform Overview](https://docs.whitebit.com/private/http-trade-v4/) | REST, WebSocket, authentication, rate limits |
| [Use with AI](https://github.com/whitebit-exchange/whitebit-mcp) | Use API docs with Claude, Cursor, VS Code via MCP |
| [GitHub Repository](https://github.com/whitebit-exchange/python-sdk) | Source code |
| [Releases](https://github.com/whitebit-exchange/python-sdk/releases) | Binaries and changelog |
| [Contributing](CONTRIBUTING.md) | Development setup and contribution guide |
| [Report an Issue](https://github.com/whitebit-exchange/python-sdk/issues) | Bug reports and feature requests |
| [WhiteBIT Exchange](https://whitebit.com) | The exchange |

---

## License

[Apache 2.0](LICENSE.md)
