# main_api_generated.WithdrawApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_withdraw**](WithdrawApi.md#create_withdraw) | **POST** /api/v4/main-account/withdraw | Create withdraw request
[**create_withdraw_pay**](WithdrawApi.md#create_withdraw_pay) | **POST** /api/v4/main-account/withdraw-pay | Create withdraw request with specific withdraw amount (fee not included)


# **create_withdraw**
> List[object] create_withdraw(create_withdraw_request)

Create withdraw request

This endpoint creates withdraw for the specified ticker.

<Warning>
Rate limit: 1000 requests/10 sec.
</Warning>

<Note>
Response is cached for: NONE
</Note>

<Note>
Also, fiat currencies can't be withdrawn without KYC verification.
</Note>


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import main_api_generated
from main_api_generated.models.create_withdraw_request import CreateWithdrawRequest
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
    api_instance = main_api_generated.WithdrawApi(api_client)
    create_withdraw_request = {"ticker":"ETH","amount":"0.9","address":"0x0964A6B8F794A4B8d61b62652dB27ddC9844FB4c","uniqueId":"24529041","request":"{{request}}","nonce":"{{nonce}}"} # CreateWithdrawRequest | 

    try:
        # Create withdraw request
        api_response = await api_instance.create_withdraw(create_withdraw_request)
        print("The response of WithdrawApi->create_withdraw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WithdrawApi->create_withdraw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_withdraw_request** | [**CreateWithdrawRequest**](CreateWithdrawRequest.md)|  | 

### Return type

**List[object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Validation succeeded and withdraw creation process is started. Go to deposit/withdraw history and check your request status by uniqueId. |  -  |
**400** | Request validation failed  Response error codes: - 1 - currency is not withdrawable - 2 - specified address is invalid - 3 - amount is too small - 4 - amount is too small for the payment system - 5 - not enough balance - 6 - amount is less than or equals [fee](/glossary#fee) - 7 - amount should be integer (can happen for currencies with zero [precision](/glossary#precision) like Neo) - 8 - target withdraw amount without [fee](/glossary#fee) equals zero - 9 - address is unavailable (occurs for withdraws to own address)  |  -  |
**422** | Inner validation failed  Response error codes: - 1 - currency is not withdrawable - 2 - specified address is invalid - 3 - amount is too small - 4 - amount is too small for the payment system - 5 - not enough balance - 6 - amount is less than or equals [fee](/glossary#fee) - 7 - amount should be integer (can happen for currencies with zero [precision](/glossary#precision) like Neo) - 8 - target withdraw amount without [fee](/glossary#fee) equals zero - 9 - address is unavailable (occurs for withdraws to own address)  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_withdraw_pay**
> List[object] create_withdraw_pay(withdraw_request)

Create withdraw request with specific withdraw amount (fee not included)

This endpoint has the similar logic as /main-account/withdraw, but with the only difference: amount that is specified will not include [fee](/glossary#fee) (it will be calculated to make target withdraw amount equal to the specified amount).

**Example:**
- When you create base withdraw and set amount = 100 USD, receiver will receive 100 USD - [fee](/glossary#fee) amount, and your balance will decrease by 100 USD.
- When you use this endpoint and set amount = 100 USD, receiver will receive 100 USD, and your balance will decrease by 100 USD + [fee](/glossary#fee) amount.

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
from main_api_generated.models.withdraw_request import WithdrawRequest
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
    api_instance = main_api_generated.WithdrawApi(api_client)
    withdraw_request = main_api_generated.WithdrawRequest() # WithdrawRequest | 

    try:
        # Create withdraw request with specific withdraw amount (fee not included)
        api_response = await api_instance.create_withdraw_pay(withdraw_request)
        print("The response of WithdrawApi->create_withdraw_pay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WithdrawApi->create_withdraw_pay: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withdraw_request** | [**WithdrawRequest**](WithdrawRequest.md)|  | 

### Return type

**List[object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Validation succeeded and withdraw creation process is started. Go to deposit/withdraw history and check your request status by uniqueId. |  -  |
**400** | Request validation failed  Response error codes: - 1 - currency is not withdrawable - 2 - specified address is invalid - 3 - amount is too small - 4 - amount is too small for the payment system - 5 - not enough balance - 6 - amount is less than or equals [fee](/glossary#fee) - 7 - amount should be integer (can happen for currencies with zero [precision](/glossary#precision) like Neo) - 8 - target withdraw amount without [fee](/glossary#fee) equals zero - 9 - address is unavailable (occurs for withdraws to own address)  |  -  |
**422** | Inner validation failed  Response error codes: - 1 - currency is not withdrawable - 2 - specified address is invalid - 3 - amount is too small - 4 - amount is too small for the payment system - 5 - not enough balance - 6 - amount is less than or equals [fee](/glossary#fee) - 7 - amount should be integer (can happen for currencies with zero [precision](/glossary#precision) like Neo) - 8 - target withdraw amount without [fee](/glossary#fee) equals zero - 9 - address is unavailable (occurs for withdraws to own address)  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

