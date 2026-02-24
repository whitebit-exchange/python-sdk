# Claude Auto-Generation Workflow

## ALWAYS CHECK
Check always generation FLOW and COMMANDS before working on the project.


## 🤖 Automatic Behavior

When I read this file or start working in this project, I MUST automatically:

1. **Check for API changes** in `./api` folder
2. **Run generation pipeline** if changes detected
3. **Validate** generated code
4. **Report** what was generated

## 🚀 Quick Commands

When user says **"go"** or **"generate"** or **"build"**:
```bash
make go
# OR (recommended - fully automated)
make build-sdk
# OR (manual steps)
make generate-all
```

**NEW: Fully Automated Pipeline**
```bash
make build-sdk
# Runs: scripts/generate_complete_sdk.py
```

This ONE command does EVERYTHING:
- ✅ Validates specs
- ✅ Generates WebSocket (models + handlers)
- ✅ Generates HTTP clients (OpenAPI Generator)
- ✅ Fixes ALL imports automatically
- ✅ Creates main client wrapper
- ✅ Creates package __init__.py
- ✅ Validates the SDK
- ✅ Ready to use!

This generates **EVERYTHING**:
- ✅ WebSocket SDK (AsyncAPI → Pydantic models + handlers)
- ✅ HTTP SDK (OpenAPI → typed API clients with all methods)
- ✅ Automatic import fixes
- ✅ Complete unified WhiteBitClient

**Note:** Requires Java 11+ for OpenAPI Generator (already installed)

## 🔄 Complete Auto-Generation Pipeline

### Phase 1: Validation ✅
```bash
python3 scripts/validate_specs.py
```
**Purpose**: Validate all YAML specifications (AsyncAPI + OpenAPI)
**Must pass**: Yes - exit if validation fails

### Phase 2: Generate WebSocket Models ✅
```bash
python3 scripts/generate_websocket_models.py
```
**Purpose**: Extract AsyncAPI schemas → Pydantic models
**Output**: `whitebit_sdk/models/websocket/__init__.py` (104 models)

### Phase 3: Generate WebSocket Handlers ✅
```bash
python3 scripts/generate_websocket_handlers.py
```
**Purpose**: Create channel handler classes
**Output**:
- `whitebit_sdk/websocket/private/*.py` (10 handlers)
- `whitebit_sdk/websocket/public/*.py` (8 handlers)

### Phase 4: Create SDK Infrastructure ✅
```bash
python3 scripts/create_sdk_structure.py
```
**Purpose**: Generate core SDK files
**Output**:
- `whitebit_sdk/websocket/base.py` - Base handler
- `whitebit_sdk/config.py` - Configuration
- `whitebit_sdk/exceptions.py` - Custom exceptions
- `whitebit_sdk/utils/signature.py` - HMAC signing
- `whitebit_sdk/utils/auth.py` - Authentication

### Phase 5: Generate HTTP Clients (OpenAPI Generator) ✅
```bash
./scripts/generate_http_openapi.sh
```

**Technology**: OpenAPI Generator 7.20.0 (Java-based)

**Features:**
- **Auto-discovery**: Automatically finds all OpenAPI specs in `api/*.yaml`
- **Full method generation**: Creates proper methods for EVERY endpoint
- **Type safety**: Generates Pydantic models for all requests/responses
- **Async support**: Uses aiohttp for async HTTP requests
- **Automatic fixes**: Fixes imports automatically after generation

**Output:** `whitebit_sdk/http/generated/{api_name}/`
- `main_api/` - 13 API classes, 115 models
- `public_api/` - 1 API class, 27 models
- `oauth2_api/` - 2 API classes, 11 models

**Generated APIs:**
```python
# Main API (13 API classes)
client.main_api.main_account      # MainAccountApi
client.main_api.fees              # FeesApi
client.main_api.transfer          # TransferApi
client.main_api.withdraw          # WithdrawApi
client.main_api.deposit           # DepositApi
client.main_api.codes             # CodesApi
client.main_api.credit_line       # CreditLineApi
client.main_api.jwt               # JWTApi
client.main_api.mining_pool       # MiningPoolApi
client.main_api.sub_account       # SubAccountApi
client.main_api.sub_account_api_keys  # SubAccountAPIKeysApi
client.main_api.crypto_lending_fixed  # CryptoLendingFixedApi
client.main_api.crypto_lending_flex   # CryptoLendingFlexApi

# Public API (1 API class)
client.public_api.public          # PublicAPIV4Api

# OAuth2 API (2 API classes)
client.oauth2.authentication      # AuthenticationApi
client.oauth2.account             # AccountEndpointsApi
```

### Phase 6: Post-Processing ✅
```bash
python3 scripts/post_process.py
```
**Purpose**: Format, type-check, cleanup
**Tools**: black, isort, mypy (if installed)

## 📋 Complete Command Sequences

### Full SDK (RECOMMENDED - WebSocket + HTTP):
```bash
make go
# OR
make generate-all

# Manually:
python3 scripts/validate_specs.py && \
python3 scripts/generate_websocket_models.py && \
python3 scripts/generate_websocket_handlers.py && \
python3 scripts/create_sdk_structure.py && \
./scripts/generate_http_openapi.sh && \
python3 scripts/post_process.py
```

### WebSocket Only:
```bash
make generate
```

### HTTP Only (re-generate HTTP clients):
```bash
make generate-http
```

## 🎯 What Gets Generated

### WebSocket Components (AsyncAPI)
- **104 Pydantic models** - All request/response/update models
- **18 Handler classes** - One per AsyncAPI channel
  - 10 private handlers (require auth)
  - 8 public handlers
- **Base infrastructure** - WebSocket base handler, auth, config

### HTTP Components (OpenAPI Generator)
**Generation method:** OpenAPI Generator 7.20.0 (Java + aiohttp)

**Auto-generated for each OpenAPI spec:**
- Main API Client (`main_api_v4.yaml`)
  - 13 API classes with typed methods
  - 115 Pydantic models
  - Example: `client.main_api.main_account.get_main_balance(...)`

- Public API Client (`http-v4.yaml`)
  - 1 API class for public endpoints
  - 27 Pydantic models
  - Example: `client.public_api.public.get_markets()`

- OAuth2 Client (`oauth2.yaml`)
  - 2 API classes
  - 11 Pydantic models
  - Example: `client.oauth2.authentication.token(...)`

**Key Features:**
- ✅ Typed methods for every endpoint
- ✅ IDE autocomplete
- ✅ Request/response validation
- ✅ Async/await support
- ✅ Proper error handling

### Core SDK Files
- `whitebit_sdk/client.py` - Main WhiteBitClient (unified interface)
- `whitebit_sdk/config.py` - WhiteBitConfig
- `whitebit_sdk/exceptions.py` - All custom exceptions
- `whitebit_sdk/http/main_api_wrapper.py` - Main API wrapper
- `whitebit_sdk/http/public_api_wrapper.py` - Public API wrapper
- `whitebit_sdk/http/oauth2_wrapper.py` - OAuth2 wrapper
- `whitebit_sdk/utils/` - Auth & signature utilities

## 🔍 Trigger Conditions

Run generation when:
- User explicitly says "go", "generate", or "build"
- User asks to work with API endpoints
- API specs in `./api` have changed (detected)
- Starting new session and specs modified

## ✅ Validation Checks

After generation:
1. Check all Python files have no syntax errors
2. Verify imports work: `make test-import`
3. Confirm models generated: check `models/websocket/__init__.py`
4. Confirm handlers generated: check `websocket/private/` and `websocket/public/`
5. Confirm HTTP clients: check `http/generated/`
6. Test unified client: `python3 -c "from whitebit_sdk import WhiteBitClient; WhiteBitClient()"`

## 🚫 What NOT to Generate

- **Tests** - Manual creation preferred (but update existing tests)
- **Documentation** - Update after reviewing generated code
- **Examples** - Update with new typed methods

## 📦 Dependencies

**Required:**
- `pyyaml` - YAML parsing
- `pydantic>=2.0.0` - Data models
- `httpx>=0.27.0` OR `aiohttp` - Async HTTP client
- `websockets` - WebSocket support
- `java` (runtime) - For OpenAPI Generator
- `openapi-generator-cli` - HTTP client generation

**Optional (for formatting):**
- `black` - Code formatting
- `isort` - Import sorting
- `mypy` - Type checking

## 🛠️ Technology Stack

- **HTTP Client**: aiohttp (via OpenAPI Generator asyncio library)
- **WebSocket**: Native asyncio + websockets
- **Models**: Pydantic v2
- **Async**: async/await everywhere
- **Auth**: HMAC-SHA512 signatures
- **Generation**: OpenAPI Generator 7.20.0 + Custom Python scripts

## 📖 Key References

- `REGENERATION_SUCCESS.md` - Quick start guide for new system
- `docs/REGENERATION_COMPLETE.md` - Detailed regeneration docs
- `docs/OPENAPI_GENERATOR_SETUP.md` - OpenAPI Generator setup
- `apistructure.md` - Complete API documentation
- `SDK_GENERATION.md` - Detailed generation guide
- `./api/` - Source of truth (OpenAPI & AsyncAPI specs)

## 🔄 Typical Workflow

1. User says "go" or "generate"
2. I run validation: `python3 scripts/validate_specs.py`
3. If valid, I run all generation phases:
   - WebSocket models (from AsyncAPI specs)
   - WebSocket handlers (channel classes)
   - SDK infrastructure (config, exceptions, utils)
   - **HTTP clients (OpenAPI Generator - with all methods)**
   - Post-processing (format, type-check)
4. I verify SDK imports correctly
5. I report what was generated
6. Ready to use!

## 💡 Status Check Commands

```bash
# Check what's been generated
ls -la whitebit_sdk/models/websocket/__init__.py
ls -la whitebit_sdk/websocket/private/
ls -la whitebit_sdk/websocket/public/
ls -la whitebit_sdk/http/generated/

# Test imports
make test-import

# Check generated models
python3 -c "from whitebit_sdk.models import websocket; print('✓ Models OK')"

# Check HTTP APIs
python3 -c "from whitebit_sdk import WhiteBitClient; c = WhiteBitClient(); print(f'Main API: {c.main_api.main_account}')"
```

## 📝 Important Notes

### HTTP Client Generation
- Generation is **automatic** using OpenAPI Generator
- Creates **typed methods** for every endpoint
- Includes **Pydantic models** for validation
- **Imports are fixed automatically** after generation
- Safe to regenerate - wrappers are separate

### WebSocket Generation
- Generation is **idempotent** - safe to run multiple times
- Generated files are **overwritten** on each run
- Manual edits to generated files will be **lost**
- Custom code goes in separate modules, not in generated files

### Usage Example

**Before (old stubs):**
```python
response = await client.request("POST", "/api/v4/main-account/balance")
```

**After (typed methods):**
```python
from whitebit_sdk.http.generated.main_api.main_api_generated.models.get_main_balance_request import GetMainBalanceRequest

balance = await client.main_api.main_account.get_main_balance(
    GetMainBalanceRequest(request="/api/v4/main-account/balance")
)
```

## Test
After generation, always run:
```bash
make test-import  # Quick import test
make test         # Full test suite
```

Assert that:
- ✅ SDK imports correctly
- ✅ Models are generated
- ✅ HTTP clients have typed methods
- ✅ WebSocket handlers work
- ✅ Everything works correctly

---

## 🔄 Automated Generation Pipeline (NEW)

**IMPORTANT**: Use the automated pipeline for all generations:

```bash
make build-sdk  # ONE COMMAND - Does everything!
```

This automated script (`scripts/generate_complete_sdk.py`) performs ALL steps:
1. ✅ Validates API specs
2. ✅ Generates WebSocket (models + handlers)
3. ✅ Generates HTTP clients (OpenAPI Generator)
4. ✅ **Automatically fixes all imports**
5. ✅ **Automatically creates client.py**
6. ✅ **Automatically creates __init__.py**
7. ✅ **Automatically validates the SDK**

**Benefits:**
- One command instead of 7+ manual steps
- No manual import fixing needed
- No manual client creation needed
- Consistent results every time
- Automatic validation

**Documentation:**
- `AUTOMATED_GENERATION.md` - Full pipeline docs
- `SDK_BUILD_SUMMARY.md` - Problem analysis & solution
- `GENERATION_ISSUES.md` - Issues encountered & fixes

## ⚠️ Documentation Policy

**DO NOT create user-facing documentation yet**

- Keep only generation-critical files (CLAUDE.md, README.md)
- Do not create:
  - User guides
  - API reference documents
  - Tutorial files
  - Example documentation
- Documentation will be created later when explicitly requested

---

**Auto-generation enabled**: YES
**Automated Pipeline**: YES (scripts/generate_complete_sdk.py)
**OpenAPI Generator**: ENABLED (Java-based)
**Last updated**: 2026-02-18
**Version**: 2.1.0 (Automated Pipeline)
