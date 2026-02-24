# public_api_generated.PublicAPIV4Api

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v4_public_assets_get**](PublicAPIV4Api.md#api_v4_public_assets_get) | **GET** /api/v4/public/assets | Asset Status List
[**api_v4_public_collateral_markets_get**](PublicAPIV4Api.md#api_v4_public_collateral_markets_get) | **GET** /api/v4/public/collateral/markets | Collateral Markets List
[**api_v4_public_fee_get**](PublicAPIV4Api.md#api_v4_public_fee_get) | **GET** /api/v4/public/fee | Fee
[**api_v4_public_funding_history_market_get**](PublicAPIV4Api.md#api_v4_public_funding_history_market_get) | **GET** /api/v4/public/funding-history/{market} | Funding History
[**api_v4_public_futures_get**](PublicAPIV4Api.md#api_v4_public_futures_get) | **GET** /api/v4/public/futures | Available Futures Markets List
[**api_v4_public_markets_get**](PublicAPIV4Api.md#api_v4_public_markets_get) | **GET** /api/v4/public/markets | Market Info
[**api_v4_public_mining_pool_get**](PublicAPIV4Api.md#api_v4_public_mining_pool_get) | **GET** /api/v4/public/mining-pool | Mining Pool Overview
[**api_v4_public_orderbook_depth_market_get**](PublicAPIV4Api.md#api_v4_public_orderbook_depth_market_get) | **GET** /api/v4/public/orderbook/depth/{market} | Depth
[**api_v4_public_orderbook_market_get**](PublicAPIV4Api.md#api_v4_public_orderbook_market_get) | **GET** /api/v4/public/orderbook/{market} | Orderbook
[**api_v4_public_ping_get**](PublicAPIV4Api.md#api_v4_public_ping_get) | **GET** /api/v4/public/ping | Server Status
[**api_v4_public_platform_status_get**](PublicAPIV4Api.md#api_v4_public_platform_status_get) | **GET** /api/v4/public/platform/status | Maintenance status
[**api_v4_public_ticker_get**](PublicAPIV4Api.md#api_v4_public_ticker_get) | **GET** /api/v4/public/ticker | Market activity
[**api_v4_public_time_get**](PublicAPIV4Api.md#api_v4_public_time_get) | **GET** /api/v4/public/time | Server Time
[**api_v4_public_trades_market_get**](PublicAPIV4Api.md#api_v4_public_trades_market_get) | **GET** /api/v4/public/trades/{market} | Recent Trades


# **api_v4_public_assets_get**
> Dict[str, Asset] api_v4_public_assets_get()

Asset Status List

This endpoint retrieves the assets status.

<Note>
Response is cached for: 1 second
</Note>

<Warning>
Rate limit 2000 requests/10 sec.
</Warning>


### Example


```python
import public_api_generated
from public_api_generated.models.asset import Asset
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)

    try:
        # Asset Status List
        api_response = await api_instance.api_v4_public_assets_get()
        print("The response of PublicAPIV4Api->api_v4_public_assets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_assets_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dict[str, Asset]**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_public_collateral_markets_get**
> List[str] api_v4_public_collateral_markets_get()

Collateral Markets List

This endpoint returns the list of [markets](/glossary#market) that available for [collateral](/glossary#collateral) trading

<Note>
Response is cached for: 1 second
</Note>

<Warning>
Rate limit 2000 requests/10 sec.
</Warning>


### Example


```python
import public_api_generated
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)

    try:
        # Collateral Markets List
        api_response = await api_instance.api_v4_public_collateral_markets_get()
        print("The response of PublicAPIV4Api->api_v4_public_collateral_markets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_collateral_markets_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_public_fee_get**
> Dict[str, FeeInfo] api_v4_public_fee_get()

Fee

This endpoint retrieves the list of [fees](/glossary#fee) and min/max amount for deposits and withdraws

<Note>
Response is cached for: 1 second
</Note>

<Warning>
Rate limit 2000 requests/10 sec.
</Warning>


### Example


```python
import public_api_generated
from public_api_generated.models.fee_info import FeeInfo
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)

    try:
        # Fee
        api_response = await api_instance.api_v4_public_fee_get()
        print("The response of PublicAPIV4Api->api_v4_public_fee_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_fee_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dict[str, FeeInfo]**](FeeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_public_funding_history_market_get**
> List[ApiV4PublicFundingHistoryMarketGet200ResponseInner] api_v4_public_funding_history_market_get(market, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

Funding History

This endpoint returns the funding rate history for a specified futures market.

<Warning>
Rate limit 2000 requests/10 sec.
</Warning>


### Example


```python
import public_api_generated
from public_api_generated.models.api_v4_public_funding_history_market_get200_response_inner import ApiV4PublicFundingHistoryMarketGet200ResponseInner
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)
    market = 'BTC_PERP' # str | Market name (e.g., BTC_PERP)
    start_date = 1752480000 # int | Start timestamp in seconds (optional)
    end_date = 1752537600 # int | End timestamp in seconds (optional)
    limit = 100 # int | Number of records to return. Default: 100, Maximum: 1000 (optional) (default to 100)
    offset = 0 # int | Number of records to skip (optional) (default to 0)

    try:
        # Funding History
        api_response = await api_instance.api_v4_public_funding_history_market_get(market, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
        print("The response of PublicAPIV4Api->api_v4_public_funding_history_market_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_funding_history_market_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**| Market name (e.g., BTC_PERP) | 
 **start_date** | **int**| Start timestamp in seconds | [optional] 
 **end_date** | **int**| End timestamp in seconds | [optional] 
 **limit** | **int**| Number of records to return. Default: 100, Maximum: 1000 | [optional] [default to 100]
 **offset** | **int**| Number of records to skip | [optional] [default to 0]

### Return type

[**List[ApiV4PublicFundingHistoryMarketGet200ResponseInner]**](ApiV4PublicFundingHistoryMarketGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_public_futures_get**
> ApiV4PublicFuturesGet200Response api_v4_public_futures_get()

Available Futures Markets List

This endpoint returns the list of available futures markets.

<Note>
Response is cached for: 1 second
</Note>

<Warning>
Rate limit 2000 requests/10 sec.
</Warning>


### Example


```python
import public_api_generated
from public_api_generated.models.api_v4_public_futures_get200_response import ApiV4PublicFuturesGet200Response
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)

    try:
        # Available Futures Markets List
        api_response = await api_instance.api_v4_public_futures_get()
        print("The response of PublicAPIV4Api->api_v4_public_futures_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_futures_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV4PublicFuturesGet200Response**](ApiV4PublicFuturesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_public_markets_get**
> List[ApiV4PublicMarketsGet200ResponseInner] api_v4_public_markets_get()

Market Info

This endpoint retrieves all information about available spot and futures markets.

<Note>
Response is cached for: 1 second
</Note>

<Warning>
Rate limit 2000 requests/10 sec.
</Warning>


### Example


```python
import public_api_generated
from public_api_generated.models.api_v4_public_markets_get200_response_inner import ApiV4PublicMarketsGet200ResponseInner
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)

    try:
        # Market Info
        api_response = await api_instance.api_v4_public_markets_get()
        print("The response of PublicAPIV4Api->api_v4_public_markets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_markets_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiV4PublicMarketsGet200ResponseInner]**](ApiV4PublicMarketsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_public_mining_pool_get**
> ApiV4PublicMiningPoolGet200Response api_v4_public_mining_pool_get()

Mining Pool Overview

This endpoint returns an overall information about the current mining pool state.

HashRate info represents in the H units.

<Warning>
Rate limit 1000 requests/10 sec.
</Warning>


### Example


```python
import public_api_generated
from public_api_generated.models.api_v4_public_mining_pool_get200_response import ApiV4PublicMiningPoolGet200Response
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)

    try:
        # Mining Pool Overview
        api_response = await api_instance.api_v4_public_mining_pool_get()
        print("The response of PublicAPIV4Api->api_v4_public_mining_pool_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_mining_pool_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV4PublicMiningPoolGet200Response**](ApiV4PublicMiningPoolGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_public_orderbook_depth_market_get**
> OrderbookResponse api_v4_public_orderbook_depth_market_get(market)

Depth

This endpoint retrieves depth price levels within ±2% of the market last price.

<Note>
Response is cached for: 1 sec
</Note>

<Warning>
Rate limit 2000 requests/10 sec.
</Warning>


### Example


```python
import public_api_generated
from public_api_generated.models.orderbook_response import OrderbookResponse
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)
    market = 'BTC_USDT' # str | Market pair name

    try:
        # Depth
        api_response = await api_instance.api_v4_public_orderbook_depth_market_get(market)
        print("The response of PublicAPIV4Api->api_v4_public_orderbook_depth_market_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_orderbook_depth_market_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**| Market pair name | 

### Return type

[**OrderbookResponse**](OrderbookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_public_orderbook_market_get**
> OrderbookResponse api_v4_public_orderbook_market_get(market, limit=limit, level=level)

Orderbook

This endpoint retrieves the current [order book](/glossary#order-book) as two arrays ([bids](/glossary#bid) / [asks](/glossary#ask)) with additional parameters.

<Note>
Response is cached for: 100 ms
</Note>

<Warning>
Rate limit 600 requests/10 sec.
</Warning>


### Example


```python
import public_api_generated
from public_api_generated.models.orderbook_response import OrderbookResponse
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)
    market = 'BTC_USDT' # str | Market pair name
    limit = 100 # int | Orders depth quantity: 0 - 100. Not defined or 0 will return 100 entries. (optional) (default to 100)
    level = 2 # int | Optional parameter that allows API user to see different level of aggregation. Level 0 – default level, no aggregation. Starting from level 1 (lowest possible aggregation) and up to level 5 - different levels of aggregated orderbook. (optional)

    try:
        # Orderbook
        api_response = await api_instance.api_v4_public_orderbook_market_get(market, limit=limit, level=level)
        print("The response of PublicAPIV4Api->api_v4_public_orderbook_market_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_orderbook_market_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**| Market pair name | 
 **limit** | **int**| Orders depth quantity: 0 - 100. Not defined or 0 will return 100 entries. | [optional] [default to 100]
 **level** | **int**| Optional parameter that allows API user to see different level of aggregation. Level 0 – default level, no aggregation. Starting from level 1 (lowest possible aggregation) and up to level 5 - different levels of aggregated orderbook. | [optional] 

### Return type

[**OrderbookResponse**](OrderbookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_public_ping_get**
> List[str] api_v4_public_ping_get()

Server Status

This endpoint retrieves the current API life-state.

<Note>
Response is cached for: 1 second
</Note>

<Warning>
Rate limit 2000 requests/10 sec.
</Warning>


### Example


```python
import public_api_generated
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)

    try:
        # Server Status
        api_response = await api_instance.api_v4_public_ping_get()
        print("The response of PublicAPIV4Api->api_v4_public_ping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_ping_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_public_platform_status_get**
> ApiV4PublicPlatformStatusGet200Response api_v4_public_platform_status_get()

Maintenance status

This endpoint retrieves maintenance status

### Example


```python
import public_api_generated
from public_api_generated.models.api_v4_public_platform_status_get200_response import ApiV4PublicPlatformStatusGet200Response
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)

    try:
        # Maintenance status
        api_response = await api_instance.api_v4_public_platform_status_get()
        print("The response of PublicAPIV4Api->api_v4_public_platform_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_platform_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV4PublicPlatformStatusGet200Response**](ApiV4PublicPlatformStatusGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_public_ticker_get**
> Dict[str, ApiV4PublicTickerGet200ResponseValue] api_v4_public_ticker_get()

Market activity

This endpoint retrieves a 24-hour pricing and volume summary for each market pair available on the exchange.

<Note>
Response is cached for: 1 second
</Note>

<Warning>
Rate limit 2000 requests/10 sec.
</Warning>


### Example


```python
import public_api_generated
from public_api_generated.models.api_v4_public_ticker_get200_response_value import ApiV4PublicTickerGet200ResponseValue
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)

    try:
        # Market activity
        api_response = await api_instance.api_v4_public_ticker_get()
        print("The response of PublicAPIV4Api->api_v4_public_ticker_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_ticker_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dict[str, ApiV4PublicTickerGet200ResponseValue]**](ApiV4PublicTickerGet200ResponseValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_public_time_get**
> ApiV4PublicTimeGet200Response api_v4_public_time_get()

Server Time

This endpoint retrieves the current server time.

<Note>
Response is cached for: 1 second
</Note>

<Warning>
Rate limit 2000 requests/10 sec.
</Warning>


### Example


```python
import public_api_generated
from public_api_generated.models.api_v4_public_time_get200_response import ApiV4PublicTimeGet200Response
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)

    try:
        # Server Time
        api_response = await api_instance.api_v4_public_time_get()
        print("The response of PublicAPIV4Api->api_v4_public_time_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_time_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV4PublicTimeGet200Response**](ApiV4PublicTimeGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_public_trades_market_get**
> List[ApiV4PublicTradesMarketGet200ResponseInner] api_v4_public_trades_market_get(market, type=type)

Recent Trades

This endpoint retrieves the [trades](/glossary#deal-trade) that have been executed recently on the requested [market](/glossary#market).

<Note>
Response is cached for: 1 second
</Note>

<Warning>
Rate limit 2000 requests/10 sec.
</Warning>


### Example


```python
import public_api_generated
from public_api_generated.models.api_v4_public_trades_market_get200_response_inner import ApiV4PublicTradesMarketGet200ResponseInner
from public_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = public_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with public_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api_generated.PublicAPIV4Api(api_client)
    market = 'BTC_USDT' # str | Market pair name
    type = 'sell' # str | Can be buy or sell (optional)

    try:
        # Recent Trades
        api_response = await api_instance.api_v4_public_trades_market_get(market, type=type)
        print("The response of PublicAPIV4Api->api_v4_public_trades_market_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAPIV4Api->api_v4_public_trades_market_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**| Market pair name | 
 **type** | **str**| Can be buy or sell | [optional] 

### Return type

[**List[ApiV4PublicTradesMarketGet200ResponseInner]**](ApiV4PublicTradesMarketGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

