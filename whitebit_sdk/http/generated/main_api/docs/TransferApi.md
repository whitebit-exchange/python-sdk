# main_api_generated.TransferApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfer_between_balances**](TransferApi.md#transfer_between_balances) | **POST** /api/v4/main-account/transfer | Transfer between balances


# **transfer_between_balances**
> List[object] transfer_between_balances(transfer_between_balances_request)

Transfer between balances

This endpoint transfers the specified amount between [main](/glossary#balance-main), [trade](/glossary#balance-spotbalance-trade) and [collateral](/glossary#balance-collateral) balances.

<Warning>
Rate limit: 1000 requests/10 sec.
</Warning>

<Note>
Response is cached for: NONE
</Note>

<Note>
Also, fiat currencies can't be transferred without KYC verification.
</Note>


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import main_api_generated
from main_api_generated.models.transfer_between_balances_request import TransferBetweenBalancesRequest
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
    api_instance = main_api_generated.TransferApi(api_client)
    transfer_between_balances_request = {"ticker":"XLM","amount":"0.9","method":"deposit","request":"{{request}}","nonce":"{{nonce}}"} # TransferBetweenBalancesRequest | 

    try:
        # Transfer between balances
        api_response = await api_instance.transfer_between_balances(transfer_between_balances_request)
        print("The response of TransferApi->transfer_between_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferApi->transfer_between_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_between_balances_request** | [**TransferBetweenBalancesRequest**](TransferBetweenBalancesRequest.md)|  | 

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
**201** | All validations succeeded and creating transaction is started |  -  |
**400** | Request validation failed |  -  |
**422** | Inner validation failed  Response error codes: - 1 - transfers from [trade](/glossary#balance-spotbalance-trade) to [main](/glossary#balance-main) are disabled - 2 - transfers from [main](/glossary#balance-main) to [trade](/glossary#balance-spotbalance-trade) are disabled - 3 - not enough balance  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

