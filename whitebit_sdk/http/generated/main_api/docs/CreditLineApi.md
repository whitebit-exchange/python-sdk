# main_api_generated.CreditLineApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_credit_line_info**](CreditLineApi.md#get_credit_line_info) | **POST** /api/v4/credit-line/loans/info | List Credit Lines


# **get_credit_line_info**
> CreditLine get_credit_line_info(get_web_socket_token_request)

List Credit Lines

This endpoint returns an active loan.
This endpoint works on demand - contact WhiteBIT support to get access.

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
from main_api_generated.models.credit_line import CreditLine
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
    api_instance = main_api_generated.CreditLineApi(api_client)
    get_web_socket_token_request = main_api_generated.GetWebSocketTokenRequest() # GetWebSocketTokenRequest | 

    try:
        # List Credit Lines
        api_response = await api_instance.get_credit_line_info(get_web_socket_token_request)
        print("The response of CreditLineApi->get_credit_line_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditLineApi->get_credit_line_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_web_socket_token_request** | [**GetWebSocketTokenRequest**](GetWebSocketTokenRequest.md)|  | 

### Return type

[**CreditLine**](CreditLine.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | No active loan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

