# main_api_generated.JWTApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_web_socket_token**](JWTApi.md#get_web_socket_token) | **POST** /api/v4/profile/websocket_token | Get WebSocket Token
[**issue_jwt_token**](JWTApi.md#issue_jwt_token) | **POST** /api/v4/jwt | Issue JWT token


# **get_web_socket_token**
> GetWebSocketToken200Response get_web_socket_token(get_web_socket_token_request)

Get WebSocket Token

This V4 endpoint can be used to retrieve the WebSocket token for user.
The token is required to authorize WebSocket connections for private API access.

<Warning>
Rate limit: 10 requests/60 sec.
</Warning>

<Note>
Response is cached for: NONE
</Note>


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import main_api_generated
from main_api_generated.models.get_web_socket_token200_response import GetWebSocketToken200Response
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
    api_instance = main_api_generated.JWTApi(api_client)
    get_web_socket_token_request = {"request":"{{request}}","nonce":"{{nonce}}"} # GetWebSocketTokenRequest | 

    try:
        # Get WebSocket Token
        api_response = await api_instance.get_web_socket_token(get_web_socket_token_request)
        print("The response of JWTApi->get_web_socket_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JWTApi->get_web_socket_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_web_socket_token_request** | [**GetWebSocketTokenRequest**](GetWebSocketTokenRequest.md)|  | 

### Return type

[**GetWebSocketToken200Response**](GetWebSocketToken200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WebSocket token retrieved successfully |  -  |
**401** | Invalid API key, signature, or nonce |  -  |
**422** | Validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_jwt_token**
> IssueJwtToken201Response issue_jwt_token(issue_jwt_token_request)

Issue JWT token

This endpoint issues a JWT token for the Fiat Gateway service.
The token is used to authenticate requests to the Fiat Gateway API.

<Note>
Response is cached for: NONE
</Note>


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import main_api_generated
from main_api_generated.models.issue_jwt_token201_response import IssueJwtToken201Response
from main_api_generated.models.issue_jwt_token_request import IssueJwtTokenRequest
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
    api_instance = main_api_generated.JWTApi(api_client)
    issue_jwt_token_request = {"request":"{{request}}","nonceWindow":false,"nonce":"{{nonce}}"} # IssueJwtTokenRequest | 

    try:
        # Issue JWT token
        api_response = await api_instance.issue_jwt_token(issue_jwt_token_request)
        print("The response of JWTApi->issue_jwt_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JWTApi->issue_jwt_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_jwt_token_request** | [**IssueJwtTokenRequest**](IssueJwtTokenRequest.md)|  | 

### Return type

[**IssueJwtToken201Response**](IssueJwtToken201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Validation succeeded and JWT token is returned |  -  |
**400** | Missing required fields or invalid data |  -  |
**401** | Invalid API key, signature, or nonce |  -  |
**500** | Server configuration issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

