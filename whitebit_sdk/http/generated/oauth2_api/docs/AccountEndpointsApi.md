# oauth2_api_generated.AccountEndpointsApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v4_accounts_balances_main_post**](AccountEndpointsApi.md#api_v4_accounts_balances_main_post) | **POST** /api/v4/accounts/balances/main | Get Main Account Balance
[**api_v4_accounts_balances_spot_post**](AccountEndpointsApi.md#api_v4_accounts_balances_spot_post) | **POST** /api/v4/accounts/balances/spot | Get Spot Account Balance
[**api_v4_accounts_converts_post**](AccountEndpointsApi.md#api_v4_accounts_converts_post) | **POST** /api/v4/accounts/converts | Get Currency Conversions
[**api_v4_accounts_deals_post**](AccountEndpointsApi.md#api_v4_accounts_deals_post) | **POST** /api/v4/accounts/deals | Get Executed Deals
[**api_v4_accounts_orders_post**](AccountEndpointsApi.md#api_v4_accounts_orders_post) | **POST** /api/v4/accounts/orders | Get Orders History
[**api_v4_accounts_transactions_post**](AccountEndpointsApi.md#api_v4_accounts_transactions_post) | **POST** /api/v4/accounts/transactions | Get Account Transactions


# **api_v4_accounts_balances_main_post**
> object api_v4_accounts_balances_main_post(body)

Get Main Account Balance

This endpoint retrieves the main account balance information.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import oauth2_api_generated
from oauth2_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = oauth2_api_generated.Configuration(
    host = "https://whitebit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = oauth2_api_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with oauth2_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oauth2_api_generated.AccountEndpointsApi(api_client)
    body = None # object | 

    try:
        # Get Main Account Balance
        api_response = await api_instance.api_v4_accounts_balances_main_post(body)
        print("The response of AccountEndpointsApi->api_v4_accounts_balances_main_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountEndpointsApi->api_v4_accounts_balances_main_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_accounts_balances_spot_post**
> object api_v4_accounts_balances_spot_post(body)

Get Spot Account Balance

This endpoint retrieves the spot trading account balance information.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import oauth2_api_generated
from oauth2_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = oauth2_api_generated.Configuration(
    host = "https://whitebit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = oauth2_api_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with oauth2_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oauth2_api_generated.AccountEndpointsApi(api_client)
    body = None # object | 

    try:
        # Get Spot Account Balance
        api_response = await api_instance.api_v4_accounts_balances_spot_post(body)
        print("The response of AccountEndpointsApi->api_v4_accounts_balances_spot_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountEndpointsApi->api_v4_accounts_balances_spot_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_accounts_converts_post**
> object api_v4_accounts_converts_post(body)

Get Currency Conversions

This endpoint retrieves the history of currency conversions.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import oauth2_api_generated
from oauth2_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = oauth2_api_generated.Configuration(
    host = "https://whitebit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = oauth2_api_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with oauth2_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oauth2_api_generated.AccountEndpointsApi(api_client)
    body = None # object | 

    try:
        # Get Currency Conversions
        api_response = await api_instance.api_v4_accounts_converts_post(body)
        print("The response of AccountEndpointsApi->api_v4_accounts_converts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountEndpointsApi->api_v4_accounts_converts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_accounts_deals_post**
> object api_v4_accounts_deals_post(body)

Get Executed Deals

This endpoint retrieves the history of executed deals.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import oauth2_api_generated
from oauth2_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = oauth2_api_generated.Configuration(
    host = "https://whitebit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = oauth2_api_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with oauth2_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oauth2_api_generated.AccountEndpointsApi(api_client)
    body = None # object | 

    try:
        # Get Executed Deals
        api_response = await api_instance.api_v4_accounts_deals_post(body)
        print("The response of AccountEndpointsApi->api_v4_accounts_deals_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountEndpointsApi->api_v4_accounts_deals_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_accounts_orders_post**
> object api_v4_accounts_orders_post(body)

Get Orders History

This endpoint retrieves the history of trading orders.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import oauth2_api_generated
from oauth2_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = oauth2_api_generated.Configuration(
    host = "https://whitebit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = oauth2_api_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with oauth2_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oauth2_api_generated.AccountEndpointsApi(api_client)
    body = None # object | 

    try:
        # Get Orders History
        api_response = await api_instance.api_v4_accounts_orders_post(body)
        print("The response of AccountEndpointsApi->api_v4_accounts_orders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountEndpointsApi->api_v4_accounts_orders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v4_accounts_transactions_post**
> object api_v4_accounts_transactions_post(body)

Get Account Transactions

This endpoint retrieves a paginated list of account transactions.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import oauth2_api_generated
from oauth2_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = oauth2_api_generated.Configuration(
    host = "https://whitebit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = oauth2_api_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with oauth2_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oauth2_api_generated.AccountEndpointsApi(api_client)
    body = None # object | 

    try:
        # Get Account Transactions
        api_response = await api_instance.api_v4_accounts_transactions_post(body)
        print("The response of AccountEndpointsApi->api_v4_accounts_transactions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountEndpointsApi->api_v4_accounts_transactions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

