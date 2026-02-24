# main_api_generated.CryptoLendingFlexApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_flex_investment**](CryptoLendingFlexApi.md#close_flex_investment) | **POST** /api/v4/main-account/smart-flex/investments/close | Close Flex Investment
[**create_flex_investment**](CryptoLendingFlexApi.md#create_flex_investment) | **POST** /api/v4/main-account/smart-flex/investments/invest | Create Flex Investment
[**get_flex_investment_history**](CryptoLendingFlexApi.md#get_flex_investment_history) | **POST** /api/v4/main-account/smart-flex/investments/history | Get Flex Investment History
[**get_flex_payment_history**](CryptoLendingFlexApi.md#get_flex_payment_history) | **POST** /api/v4/main-account/smart-flex/investments/payment-history | Get Flex Payment History
[**get_flex_plans**](CryptoLendingFlexApi.md#get_flex_plans) | **POST** /api/v4/main-account/smart-flex/plans | Get Flex Plans
[**get_user_flex_investments**](CryptoLendingFlexApi.md#get_user_flex_investments) | **POST** /api/v4/main-account/smart-flex/investments | Get User Flex Investments
[**update_flex_auto_reinvestment**](CryptoLendingFlexApi.md#update_flex_auto_reinvestment) | **POST** /api/v4/main-account/smart-flex/investments/auto-invest | Update Flex Auto-Reinvestment
[**withdraw_from_flex_investment**](CryptoLendingFlexApi.md#withdraw_from_flex_investment) | **POST** /api/v4/main-account/smart-flex/investments/withdraw | Withdraw from Flex Investment


# **close_flex_investment**
> CloseFlexInvestment201Response close_flex_investment(close_flex_investment_request)

Close Flex Investment

Completely close investment and withdraw all funds.

**Validation Rules:**
- plan: required, string, UUID format, must exist
- Investment must be ACTIVE

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
from main_api_generated.models.close_flex_investment201_response import CloseFlexInvestment201Response
from main_api_generated.models.close_flex_investment_request import CloseFlexInvestmentRequest
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
    api_instance = main_api_generated.CryptoLendingFlexApi(api_client)
    close_flex_investment_request = {"plan":"8f2e9d3c-1a4b-4c2d-9e5f-6a7b8c9d0e1f","request":"{{request}}","nonce":"{{nonce}}"} # CloseFlexInvestmentRequest | 

    try:
        # Close Flex Investment
        api_response = await api_instance.close_flex_investment(close_flex_investment_request)
        print("The response of CryptoLendingFlexApi->close_flex_investment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLendingFlexApi->close_flex_investment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **close_flex_investment_request** | [**CloseFlexInvestmentRequest**](CloseFlexInvestmentRequest.md)|  | 

### Return type

[**CloseFlexInvestment201Response**](CloseFlexInvestment201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Investment closed successfully |  -  |
**400** | Validation failed |  -  |
**422** | Business logic error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_flex_investment**
> CreateFlexInvestment201Response create_flex_investment(create_flex_investment_request)

Create Flex Investment

Create new investment in a Flex plan.

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
from main_api_generated.models.create_flex_investment201_response import CreateFlexInvestment201Response
from main_api_generated.models.create_flex_investment_request import CreateFlexInvestmentRequest
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
    api_instance = main_api_generated.CryptoLendingFlexApi(api_client)
    create_flex_investment_request = {"plan":"8f2e9d3c-1a4b-4c2d-9e5f-6a7b8c9d0e1f","amount":"1000.500000","withReinvest":true,"request":"{{request}}","nonce":"{{nonce}}"} # CreateFlexInvestmentRequest | 

    try:
        # Create Flex Investment
        api_response = await api_instance.create_flex_investment(create_flex_investment_request)
        print("The response of CryptoLendingFlexApi->create_flex_investment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLendingFlexApi->create_flex_investment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_flex_investment_request** | [**CreateFlexInvestmentRequest**](CreateFlexInvestmentRequest.md)|  | 

### Return type

[**CreateFlexInvestment201Response**](CreateFlexInvestment201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Investment created successfully |  -  |
**400** | Validation failed |  -  |
**422** | Business logic error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flex_investment_history**
> GetFlexInvestmentHistory200Response get_flex_investment_history(get_flex_investment_history_request)

Get Flex Investment History

Retrieve complete investment operations history with advanced filtering.

**Available Action Types:**
- 1: INVEST - Investment creation
- 2: REINVEST - Automatic reinvestment
- 3: WITHDRAW_FROM_INVESTMENT - Partial withdrawal
- 4: DAILY_EARNING - Daily earnings
- 5: CLOSE_INVESTMENT - Investment closure
- 6: OPEN_INVESTMENT - Investment opening

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
from main_api_generated.models.get_flex_investment_history200_response import GetFlexInvestmentHistory200Response
from main_api_generated.models.get_flex_investment_history_request import GetFlexInvestmentHistoryRequest
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
    api_instance = main_api_generated.CryptoLendingFlexApi(api_client)
    get_flex_investment_history_request = {"limit":50,"offset":0,"plan":"8f2e9d3c-1a4b-4c2d-9e5f-6a7b8c9d0e1f","investment":"inv_123","transaction":"tx_456","dateFrom":1640995200,"dateTo":1641081600,"actionTypes":[1,2,4],"request":"{{request}}","nonce":"{{nonce}}"} # GetFlexInvestmentHistoryRequest | 

    try:
        # Get Flex Investment History
        api_response = await api_instance.get_flex_investment_history(get_flex_investment_history_request)
        print("The response of CryptoLendingFlexApi->get_flex_investment_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLendingFlexApi->get_flex_investment_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_flex_investment_history_request** | [**GetFlexInvestmentHistoryRequest**](GetFlexInvestmentHistoryRequest.md)|  | 

### Return type

[**GetFlexInvestmentHistory200Response**](GetFlexInvestmentHistory200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flex_payment_history**
> GetFlexInvestmentHistory200Response get_flex_payment_history(get_flex_payment_history_request)

Get Flex Payment History

Retrieve investment earnings history (ONLY DAILY_EARNING operations).

**Note:** This endpoint automatically filters to show ONLY DAILY_EARNING operations (type 4).

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
from main_api_generated.models.get_flex_investment_history200_response import GetFlexInvestmentHistory200Response
from main_api_generated.models.get_flex_payment_history_request import GetFlexPaymentHistoryRequest
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
    api_instance = main_api_generated.CryptoLendingFlexApi(api_client)
    get_flex_payment_history_request = {"limit":50,"offset":0,"plan":"8f2e9d3c-1a4b-4c2d-9e5f-6a7b8c9d0e1f","investment":"inv_123","transaction":"tx_456","dateFrom":1640995200,"dateTo":1641081600,"request":"{{request}}","nonce":"{{nonce}}"} # GetFlexPaymentHistoryRequest | 

    try:
        # Get Flex Payment History
        api_response = await api_instance.get_flex_payment_history(get_flex_payment_history_request)
        print("The response of CryptoLendingFlexApi->get_flex_payment_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLendingFlexApi->get_flex_payment_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_flex_payment_history_request** | [**GetFlexPaymentHistoryRequest**](GetFlexPaymentHistoryRequest.md)|  | 

### Return type

[**GetFlexInvestmentHistory200Response**](GetFlexInvestmentHistory200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flex_plans**
> List[FlexPlan] get_flex_plans(get_flex_plans_request)

Get Flex Plans

Retrieve list of active [Flex Plans](/glossary#crypto-lending).

Available after September 22, 2025.

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
from main_api_generated.models.flex_plan import FlexPlan
from main_api_generated.models.get_flex_plans_request import GetFlexPlansRequest
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
    api_instance = main_api_generated.CryptoLendingFlexApi(api_client)
    get_flex_plans_request = {"limit":50,"offset":0,"ticker":"USDT","request":"{{request}}","nonce":"{{nonce}}"} # GetFlexPlansRequest | 

    try:
        # Get Flex Plans
        api_response = await api_instance.get_flex_plans(get_flex_plans_request)
        print("The response of CryptoLendingFlexApi->get_flex_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLendingFlexApi->get_flex_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_flex_plans_request** | [**GetFlexPlansRequest**](GetFlexPlansRequest.md)|  | 

### Return type

[**List[FlexPlan]**](FlexPlan.md)

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

# **get_user_flex_investments**
> GetUserFlexInvestments200Response get_user_flex_investments(get_user_flex_investments_request)

Get User Flex Investments

Retrieve user's investment portfolio with optional filtering.

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
from main_api_generated.models.get_user_flex_investments200_response import GetUserFlexInvestments200Response
from main_api_generated.models.get_user_flex_investments_request import GetUserFlexInvestmentsRequest
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
    api_instance = main_api_generated.CryptoLendingFlexApi(api_client)
    get_user_flex_investments_request = {"limit":100,"offset":0,"ticker":"USDT","plan":"8f2e9d3c-1a4b-4c2d-9e5f-6a7b8c9d0e1f","investment":"invest_id_123","investmentStatus":1,"request":"{{request}}","nonce":"{{nonce}}"} # GetUserFlexInvestmentsRequest | 

    try:
        # Get User Flex Investments
        api_response = await api_instance.get_user_flex_investments(get_user_flex_investments_request)
        print("The response of CryptoLendingFlexApi->get_user_flex_investments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLendingFlexApi->get_user_flex_investments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_user_flex_investments_request** | [**GetUserFlexInvestmentsRequest**](GetUserFlexInvestmentsRequest.md)|  | 

### Return type

[**GetUserFlexInvestments200Response**](GetUserFlexInvestments200Response.md)

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

# **update_flex_auto_reinvestment**
> UpdateFlexAutoReinvestment200Response update_flex_auto_reinvestment(update_flex_auto_reinvestment_request)

Update Flex Auto-Reinvestment

Enable/disable automatic reinvestment for user's investment.

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
from main_api_generated.models.update_flex_auto_reinvestment200_response import UpdateFlexAutoReinvestment200Response
from main_api_generated.models.update_flex_auto_reinvestment_request import UpdateFlexAutoReinvestmentRequest
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
    api_instance = main_api_generated.CryptoLendingFlexApi(api_client)
    update_flex_auto_reinvestment_request = {"plan":"8f2e9d3c-1a4b-4c2d-9e5f-6a7b8c9d0e1f","enabled":true,"request":"{{request}}","nonce":"{{nonce}}"} # UpdateFlexAutoReinvestmentRequest | 

    try:
        # Update Flex Auto-Reinvestment
        api_response = await api_instance.update_flex_auto_reinvestment(update_flex_auto_reinvestment_request)
        print("The response of CryptoLendingFlexApi->update_flex_auto_reinvestment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLendingFlexApi->update_flex_auto_reinvestment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_flex_auto_reinvestment_request** | [**UpdateFlexAutoReinvestmentRequest**](UpdateFlexAutoReinvestmentRequest.md)|  | 

### Return type

[**UpdateFlexAutoReinvestment200Response**](UpdateFlexAutoReinvestment200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Auto-reinvestment updated successfully |  -  |
**400** | Validation failed |  -  |
**422** | Business logic error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_from_flex_investment**
> WithdrawFromFlexInvestment201Response withdraw_from_flex_investment(withdraw_from_flex_investment_request)

Withdraw from Flex Investment

Withdraw specified amount from user's investment.

**Note:** Plan must be active and accessible to user.

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
from main_api_generated.models.withdraw_from_flex_investment201_response import WithdrawFromFlexInvestment201Response
from main_api_generated.models.withdraw_from_flex_investment_request import WithdrawFromFlexInvestmentRequest
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
    api_instance = main_api_generated.CryptoLendingFlexApi(api_client)
    withdraw_from_flex_investment_request = {"plan":"8f2e9d3c-1a4b-4c2d-9e5f-6a7b8c9d0e1f","amount":"500.250000","request":"{{request}}","nonce":"{{nonce}}"} # WithdrawFromFlexInvestmentRequest | 

    try:
        # Withdraw from Flex Investment
        api_response = await api_instance.withdraw_from_flex_investment(withdraw_from_flex_investment_request)
        print("The response of CryptoLendingFlexApi->withdraw_from_flex_investment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoLendingFlexApi->withdraw_from_flex_investment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withdraw_from_flex_investment_request** | [**WithdrawFromFlexInvestmentRequest**](WithdrawFromFlexInvestmentRequest.md)|  | 

### Return type

[**WithdrawFromFlexInvestment201Response**](WithdrawFromFlexInvestment201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Withdrawal successful |  -  |
**400** | Validation failed |  -  |
**422** | Business logic error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

