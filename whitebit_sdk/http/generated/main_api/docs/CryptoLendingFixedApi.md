# main_api_generated.CryptoLendingFixedApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_fixed_investment**](CryptoLendingFixedApi.md#close_fixed_investment) | **POST** /api/v4/main-account/smart/investment/close | Close investment
[**create_fixed_investment**](CryptoLendingFixedApi.md#create_fixed_investment) | **POST** /api/v4/main-account/smart/investment | Invest
[**get_fixed_investments_history**](CryptoLendingFixedApi.md#get_fixed_investments_history) | **POST** /api/v4/main-account/smart/investments | Get investments history
[**get_fixed_plans**](CryptoLendingFixedApi.md#get_fixed_plans) | **POST** /api/v4/main-account/smart/plans | Get plans
[**get_interest_payment_history**](CryptoLendingFixedApi.md#get_interest_payment_history) | **POST** /api/v4/main-account/smart/interest-payment-history | Get interest payments history


# **close_fixed_investment**
> object close_fixed_investment(close_fixed_investment_request)

Close investment

This endpoint closes active investment.

<Warning>
Rate limit: 1000 requests/10 sec.
</Warning>

<Note>
Response is cached for: NONE
</Note>


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import main_api_generated
from main_api_generated.models.close_fixed_investment_request import CloseFixedInvestmentRequest
from main_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = main_api_generated.Configuration(
    host = "https://whitebit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with main_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = main_api_generated.CryptoLendingFixedApi(api_client)
    close_fixed_investment_request = {"id":"0d7b66ff-1909-4938-ab7a-d16d9a64dcd5","request":"{{request}}","nonce":"{{nonce}}"} # CloseFixedInvestmentRequest | 

    try:
        # Close investment
        api_response = await api_instance.close_fixed_investment(close_fixed_investment_request)
        print("The response of CryptoLendingFixedApi->close_fixed_investment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLendingFixedApi->close_fixed_investment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **close_fixed_investment_request** | [**CloseFixedInvestmentRequest**](CloseFixedInvestmentRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Investment closed successfully |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fixed_investment**
> CreateFixedInvestment201Response create_fixed_investment(create_fixed_investment_request)

Invest

This endpoint creates a new investment to the specified [invest plan](/glossary#crypto-lending).

<Warning>
Rate limit: 1000 requests/10 sec.
</Warning>

<Note>
Response is cached for: NONE
</Note>


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import main_api_generated
from main_api_generated.models.create_fixed_investment201_response import CreateFixedInvestment201Response
from main_api_generated.models.create_fixed_investment_request import CreateFixedInvestmentRequest
from main_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = main_api_generated.Configuration(
    host = "https://whitebit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with main_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = main_api_generated.CryptoLendingFixedApi(api_client)
    create_fixed_investment_request = {"planId":"8e667b4a-0b71-4988-8af5-9474dbfaeb51","amount":"100","request":"{{request}}","nonce":"{{nonce}}"} # CreateFixedInvestmentRequest | 

    try:
        # Invest
        api_response = await api_instance.create_fixed_investment(create_fixed_investment_request)
        print("The response of CryptoLendingFixedApi->create_fixed_investment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLendingFixedApi->create_fixed_investment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_fixed_investment_request** | [**CreateFixedInvestmentRequest**](CreateFixedInvestmentRequest.md)|  | 

### Return type

[**CreateFixedInvestment201Response**](CreateFixedInvestment201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Investment created successfully |  -  |
**400** | Request validation failed |  -  |
**422** | Inner validation failed  Response error codes: - 1 - Investment already exists (when you don&#39;t have permissions to create multiple investments by plan) - 2 - Amount is less than min investment amount - 3 - Amount is greater than max investment amount - 4 - Not enough balance to create investment - 5 - No funds in plan to cover target interest amount  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fixed_investments_history**
> GetFixedInvestmentsHistory200Response get_fixed_investments_history(get_fixed_investments_history_request)

Get investments history

This endpoint retrieves an investments history.

<Warning>
Rate limit: 1000 requests/10 sec.
</Warning>

<Note>
Response is cached for: NONE
</Note>


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import main_api_generated
from main_api_generated.models.get_fixed_investments_history200_response import GetFixedInvestmentsHistory200Response
from main_api_generated.models.get_fixed_investments_history_request import GetFixedInvestmentsHistoryRequest
from main_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = main_api_generated.Configuration(
    host = "https://whitebit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with main_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = main_api_generated.CryptoLendingFixedApi(api_client)
    get_fixed_investments_history_request = {"id":"0d7b66ff-1909-4938-ab7a-d16d9a64dcd5","ticker":"USDT","status":1,"request":"{{request}}","nonce":"{{nonce}}"} # GetFixedInvestmentsHistoryRequest | 

    try:
        # Get investments history
        api_response = await api_instance.get_fixed_investments_history(get_fixed_investments_history_request)
        print("The response of CryptoLendingFixedApi->get_fixed_investments_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLendingFixedApi->get_fixed_investments_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_fixed_investments_history_request** | [**GetFixedInvestmentsHistoryRequest**](GetFixedInvestmentsHistoryRequest.md)|  | 

### Return type

[**GetFixedInvestmentsHistory200Response**](GetFixedInvestmentsHistory200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fixed_plans**
> List[FixedPlan] get_fixed_plans(get_fixed_plans_request)

Get plans

This endpoint retrieves all active [plans](/glossary#crypto-lending).

<Note>
These endpoints are available only for B2B partner services. You need to fill the institutional services form in order to get permissions to use these endpoints.
</Note>

**Note:** When target currency is different from source currency, interest amount in target currency will be calculated using `interestRatio` value.

**Examples:**
- When source currency = USDT, target currency = BTC and interest ratio = 40000, it means that you will receive interest in BTC that equals interest amount in USDT divided by interest ratio (in this case 0.000025 BTC per each 1 USDT of interest amount).
- When source currency equals target currency, interest ratio equals 1.

<Warning>
Rate limit: 1000 requests/10 sec.
</Warning>

<Note>
Response is cached for: NONE
</Note>


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import main_api_generated
from main_api_generated.models.fixed_plan import FixedPlan
from main_api_generated.models.get_fixed_plans_request import GetFixedPlansRequest
from main_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = main_api_generated.Configuration(
    host = "https://whitebit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with main_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = main_api_generated.CryptoLendingFixedApi(api_client)
    get_fixed_plans_request = {"ticker":"USDT","request":"{{request}}","nonce":"{{nonce}}"} # GetFixedPlansRequest | 

    try:
        # Get plans
        api_response = await api_instance.get_fixed_plans(get_fixed_plans_request)
        print("The response of CryptoLendingFixedApi->get_fixed_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLendingFixedApi->get_fixed_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_fixed_plans_request** | [**GetFixedPlansRequest**](GetFixedPlansRequest.md)|  | 

### Return type

[**List[FixedPlan]**](FixedPlan.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interest_payment_history**
> GetInterestPaymentHistory200Response get_interest_payment_history(get_interest_payment_history_request)

Get interest payments history

This endpoint retrieves the history of interest payments.

<Warning>
Rate limit: 1000 requests/10 sec.
</Warning>

<Note>
Response is cached for: NONE
</Note>


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import main_api_generated
from main_api_generated.models.get_interest_payment_history200_response import GetInterestPaymentHistory200Response
from main_api_generated.models.get_interest_payment_history_request import GetInterestPaymentHistoryRequest
from main_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = main_api_generated.Configuration(
    host = "https://whitebit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with main_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = main_api_generated.CryptoLendingFixedApi(api_client)
    get_interest_payment_history_request = {"planId":"8e667b4a-0b71-4988-8af5-9474dbfaeb51","ticker":"USDT","request":"{{request}}","nonce":"{{nonce}}"} # GetInterestPaymentHistoryRequest | 

    try:
        # Get interest payments history
        api_response = await api_instance.get_interest_payment_history(get_interest_payment_history_request)
        print("The response of CryptoLendingFixedApi->get_interest_payment_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLendingFixedApi->get_interest_payment_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_interest_payment_history_request** | [**GetInterestPaymentHistoryRequest**](GetInterestPaymentHistoryRequest.md)|  | 

### Return type

[**GetInterestPaymentHistory200Response**](GetInterestPaymentHistory200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

