# oauth2_api_generated.AuthenticationApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login_get**](AuthenticationApi.md#auth_login_get) | **GET** /auth/login | OAuth 2.0 Authorization
[**oauth2_refresh_token_post**](AuthenticationApi.md#oauth2_refresh_token_post) | **POST** /oauth2/refresh_token | Refresh Token
[**oauth2_token_post**](AuthenticationApi.md#oauth2_token_post) | **POST** /oauth2/token | Get Access Token


# **auth_login_get**
> auth_login_get(client_id, state=state)

OAuth 2.0 Authorization

This endpoint initiates the OAuth 2.0 authorization flow for user authentication and obtaining an authorization code.

**Using the State Parameter (Best Practice)**

The `state` parameter is crucial for security in OAuth flows:

- Generate a cryptographically secure random string
- Store it in the user's session before redirecting
- Validate it matches when handling the callback
- This prevents CSRF attacks
<Note>
**Note:** OAuth scopes are predefined during client application setup and cannot be modified during the authorization request. The access token will include all scopes that were approved during client creation.
</Note>


### Example


```python
import oauth2_api_generated
from oauth2_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = oauth2_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with oauth2_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oauth2_api_generated.AuthenticationApi(api_client)
    client_id = 'YOUR_CLIENT_ID' # str | Your application's client ID
    state = 'SECURE_RANDOM_STATE' # str | A secure random string used to maintain state between the request and callback and prevent CSRF attacks (Recommended) (optional)

    try:
        # OAuth 2.0 Authorization
        await api_instance.auth_login_get(client_id, state=state)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_login_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Your application&#39;s client ID | 
 **state** | **str**| A secure random string used to maintain state between the request and callback and prevent CSRF attacks (Recommended) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to authorization page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth2_refresh_token_post**
> Oauth2RefreshTokenPost200Response oauth2_refresh_token_post(client_id, client_secret, token)

Refresh Token

This endpoint creates a new access token using a refresh token.

**Request Headers:**
- Content-Type: application/x-www-form-urlencoded

<Warning>
**Important Notes:**

- Refresh token duration is 600 seconds
- Rate limit: 1 request per second
- The IP of the client must be added to WB Allowlist
</Warning>


### Example


```python
import oauth2_api_generated
from oauth2_api_generated.models.oauth2_refresh_token_post200_response import Oauth2RefreshTokenPost200Response
from oauth2_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = oauth2_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with oauth2_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oauth2_api_generated.AuthenticationApi(api_client)
    client_id = 'client_id_example' # str | Your application's client ID
    client_secret = 'client_secret_example' # str | Your application's client secret
    token = 'token_example' # str | The refresh token received from the token endpoint

    try:
        # Refresh Token
        api_response = await api_instance.oauth2_refresh_token_post(client_id, client_secret, token)
        print("The response of AuthenticationApi->oauth2_refresh_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->oauth2_refresh_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Your application&#39;s client ID | 
 **client_secret** | **str**| Your application&#39;s client secret | 
 **token** | **str**| The refresh token received from the token endpoint | 

### Return type

[**Oauth2RefreshTokenPost200Response**](Oauth2RefreshTokenPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful token refresh |  -  |
**400** | Invalid token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth2_token_post**
> Oauth2TokenPost200Response oauth2_token_post(client_id, client_secret, code)

Get Access Token

This endpoint activates an access token by exchanging an authorization code.

<Warning>
**Important Notes:**

- Access token duration is 300 seconds
- The IP of the client must be added to WB Allowlist
</Warning>

**Request Headers:**
- Content-Type: application/x-www-form-urlencoded


### Example


```python
import oauth2_api_generated
from oauth2_api_generated.models.oauth2_token_post200_response import Oauth2TokenPost200Response
from oauth2_api_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://whitebit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = oauth2_api_generated.Configuration(
    host = "https://whitebit.com"
)


# Enter a context with an instance of the API client
async with oauth2_api_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oauth2_api_generated.AuthenticationApi(api_client)
    client_id = 'client_id_example' # str | Your application's client ID
    client_secret = 'client_secret_example' # str | Your application's client secret
    code = 'code_example' # str | The authorization code received from the authorization endpoint

    try:
        # Get Access Token
        api_response = await api_instance.oauth2_token_post(client_id, client_secret, code)
        print("The response of AuthenticationApi->oauth2_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->oauth2_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Your application&#39;s client ID | 
 **client_secret** | **str**| Your application&#39;s client secret | 
 **code** | **str**| The authorization code received from the authorization endpoint | 

### Return type

[**Oauth2TokenPost200Response**](Oauth2TokenPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful token exchange |  -  |
**401** | Not authorized |  -  |
**422** | Validation errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

