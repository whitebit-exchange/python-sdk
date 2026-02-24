# WhiteBIT SDK for Python

Python SDK for WhiteBIT cryptocurrency exchange.

## Generation

To generate the SDK:

```bash
make go
```

This will generate:
- WebSocket API (AsyncAPI) - handlers and models
- HTTP API (OpenAPI) - typed clients with all methods
- Unified WhiteBitClient interface

## Requirements

- Python 3.8+
- Java 11+ (for OpenAPI Generator)

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

### Test All Endpoints (One Click)

```bash
# Test public endpoints (no credentials needed)
python3 example.py

# Test private endpoints (with credentials)
export WHITEBIT_API_KEY='your_key'
export WHITEBIT_API_SECRET='your_secret'
python3 example.py
```

The `example.py` script tests ALL available endpoints and shows complete API usage.

### Usage in Code

```python
from whitebit_sdk import WhiteBitClient

# Initialize client
client = WhiteBitClient(
    api_key="your_key",
    api_secret="your_secret"
)

async with client:
    # Public API (no authentication)
    markets = await client.public_api.public.api_v4_public_markets_get()
    ticker = await client.public_api.public.api_v4_public_ticker_get()

    # Main API (requires authentication)
    from whitebit_sdk.http.generated.main_api.main_api_generated.models.get_main_balance_request import GetMainBalanceRequest

    balance = await client.main_api.main_account.get_main_balance(
        GetMainBalanceRequest(request="/api/v4/main-account/balance")
    )

    # All 13 Main API classes available:
    # - client.main_api.main_account
    # - client.main_api.fees
    # - client.main_api.codes
    # - client.main_api.deposit
    # - client.main_api.withdraw
    # - client.main_api.transfer
    # - client.main_api.sub_account
    # - client.main_api.credit_line
    # - client.main_api.crypto_lending_flex
    # - client.main_api.crypto_lending_fixed
    # - client.main_api.jwt
    # - client.main_api.mining_pool
    # - client.main_api.sub_account_api_keys
```

## Testing

```bash
make test-import  # Quick import test
make test         # Full test suite
python3 example.py # Test all endpoints
```

## Technical Details

See `CLAUDE.md` for complete generation instructions and architecture details.
