# main_api_generated.MainAccountApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deposit_withdraw_history**](MainAccountApi.md#get_deposit_withdraw_history) | **POST** /api/v4/main-account/history | Get deposit/withdraw history
[**get_main_balance**](MainAccountApi.md#get_main_balance) | **POST** /api/v4/main-account/balance | Get main balance


# **get_deposit_withdraw_history**
> GetDepositWithdrawHistory201Response get_deposit_withdraw_history(get_deposit_withdraw_history_request)

Get deposit/withdraw history

This endpoint retrieves the history of deposits and withdraws.

**Deposit status codes:**
- `Successful` - 3, 7
- `Canceled` - 4, 9
- `Unconfirmed by user` - 5
- `Frozen` - 21
- `Uncredited` - 22
- `Pending` - 15

**Travel Rule Deposit check status codes:**
- `Awaiting verification` - 27: The transaction has been frozen due to the lack of data required under the Travel Rule. The user is required to provide this data manually through the exchange interface.
- `Confirmation in progress` - 28: The Travel Rule data provided by the user is currently being verified by WhiteBIT.

⚠️ Due to regulatory requirements in Turkey and [EU](/glossary#eea), every inbound crypto deposit must be put on hold (frozen) until transaction's origin being confirmed. Must be provided certain details if the transaction is from another Virtual Asset Service Provider (VASP) or verify the address if it is from a self-hosted wallet. Only after successful verification can the deposited funds be credited to account.

**Withdraw status codes:**
- `Pending` - 1, 2, 6, 10, 11, 12, 13, 14, 15, 16, 17
- `Successful` - 3, 7
- `Canceled` - 4
- `Unconfirmed by user` - 5
- `Frozen` - 21
- `Partially successful` - 18

<Warning>
Rate limit: 200 requests/10 sec.
</Warning>

<Note>
Response is cached for: NONE
</Note>


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import main_api_generated
from main_api_generated.models.get_deposit_withdraw_history201_response import GetDepositWithdrawHistory201Response
from main_api_generated.models.get_deposit_withdraw_history_request import GetDepositWithdrawHistoryRequest
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
    api_instance = main_api_generated.MainAccountApi(api_client)
    get_deposit_withdraw_history_request = {"transactionMethod":1,"ticker":"BTC","offset":0,"limit":100,"status":[3,7],"request":"{{request}}","nonce":"{{nonce}}"} # GetDepositWithdrawHistoryRequest | 

    try:
        # Get deposit/withdraw history
        api_response = await api_instance.get_deposit_withdraw_history(get_deposit_withdraw_history_request)
        print("The response of MainAccountApi->get_deposit_withdraw_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainAccountApi->get_deposit_withdraw_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_deposit_withdraw_history_request** | [**GetDepositWithdrawHistoryRequest**](GetDepositWithdrawHistoryRequest.md)|  | 

### Return type

[**GetDepositWithdrawHistory201Response**](GetDepositWithdrawHistory201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | All validations succeeded and creating transaction is started |  -  |
**400** | Request validation failed |  -  |
**422** | Inner validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_main_balance**
> Dict[str, GetMainBalance200ResponseValue] get_main_balance(get_main_balance_request)

Get main balance

This endpoint retrieves the [main balance](/glossary#balance-main) by currency [ticker](/glossary#ticker) or all balances.

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
from main_api_generated.models.get_main_balance200_response_value import GetMainBalance200ResponseValue
from main_api_generated.models.get_main_balance_request import GetMainBalanceRequest
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
    api_instance = main_api_generated.MainAccountApi(api_client)
    get_main_balance_request = main_api_generated.GetMainBalanceRequest() # GetMainBalanceRequest | 

    try:
        # Get main balance
        api_response = await api_instance.get_main_balance(get_main_balance_request)
        print("The response of MainAccountApi->get_main_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainAccountApi->get_main_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_main_balance_request** | [**GetMainBalanceRequest**](GetMainBalanceRequest.md)|  | 

### Return type

[**Dict[str, GetMainBalance200ResponseValue]**](GetMainBalance200ResponseValue.md)

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

