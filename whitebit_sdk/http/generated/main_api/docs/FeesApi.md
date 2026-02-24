# main_api_generated.FeesApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fees**](FeesApi.md#get_fees) | **POST** /api/v4/main-account/fee | Get fees


# **get_fees**
> List[FeeInfo] get_fees(get_web_socket_token_request)

Get fees

Returns an array of objects containing deposit/withdrawal [fees](/glossary#fee) for the corresponding currencies.
Zero value in amount fields means that the setting is disabled.

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
from main_api_generated.models.fee_info import FeeInfo
from main_api_generated.models.get_web_socket_token_request import GetWebSocketTokenRequest
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
    api_instance = main_api_generated.FeesApi(api_client)
    get_web_socket_token_request = main_api_generated.GetWebSocketTokenRequest() # GetWebSocketTokenRequest | 

    try:
        # Get fees
        api_response = await api_instance.get_fees(get_web_socket_token_request)
        print("The response of FeesApi->get_fees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeesApi->get_fees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_web_socket_token_request** | [**GetWebSocketTokenRequest**](GetWebSocketTokenRequest.md)|  | 

### Return type

[**List[FeeInfo]**](FeeInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

