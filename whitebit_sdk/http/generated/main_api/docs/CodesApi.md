# main_api_generated.CodesApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_code**](CodesApi.md#apply_code) | **POST** /api/v4/main-account/codes/apply | Apply code
[**create_code**](CodesApi.md#create_code) | **POST** /api/v4/main-account/codes | Create code
[**get_codes_history**](CodesApi.md#get_codes_history) | **POST** /api/v4/main-account/codes/history | Get codes history
[**get_my_codes**](CodesApi.md#get_my_codes) | **POST** /api/v4/main-account/codes/my | Get my codes


# **apply_code**
> ApplyCode201Response apply_code(apply_code_request)

Apply code

This endpoint applies [WhiteBIT code](/glossary#whitebit-codes).

<Warning>
Rate limit: 60 requests/1 sec.
</Warning>

<Note>
Response is cached for: NONE
</Note>


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import main_api_generated
from main_api_generated.models.apply_code201_response import ApplyCode201Response
from main_api_generated.models.apply_code_request import ApplyCodeRequest
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
    api_instance = main_api_generated.CodesApi(api_client)
    apply_code_request = {"code":"WBe11f4fce-2a53-4edc-b195-66b693bd77e3ETH","passphrase":"some passphrase","request":"{{request}}","nonce":"{{nonce}}"} # ApplyCodeRequest | 

    try:
        # Apply code
        api_response = await api_instance.apply_code(apply_code_request)
        print("The response of CodesApi->apply_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodesApi->apply_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apply_code_request** | [**ApplyCodeRequest**](ApplyCodeRequest.md)|  | 

### Return type

[**ApplyCode201Response**](ApplyCode201Response.md)

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

# **create_code**
> CreateCode201Response create_code(create_code_request)

Create code

This endpoint creates [WhiteBIT code](/glossary#whitebit-codes).

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
from main_api_generated.models.create_code201_response import CreateCode201Response
from main_api_generated.models.create_code_request import CreateCodeRequest
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
    api_instance = main_api_generated.CodesApi(api_client)
    create_code_request = {"ticker":"ETH","amount":"0.002","passphrase":"some passphrase","description":"some description","request":"{{request}}","nonce":"{{nonce}}"} # CreateCodeRequest | 

    try:
        # Create code
        api_response = await api_instance.create_code(create_code_request)
        print("The response of CodesApi->create_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodesApi->create_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_code_request** | [**CreateCodeRequest**](CreateCodeRequest.md)|  | 

### Return type

[**CreateCode201Response**](CreateCode201Response.md)

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
**422** | Inner validation failed  Response error codes: - 0 - Fiat are available on the front-end only - 1 - currency is not withdrawable - 2 - specified address is invalid - 3 - amount is too small - 4 - amount is too small for the payment system - 5 - not enough balance - 6 - amount is less than or equals [fee](/glossary#fee)  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_codes_history**
> GetCodesHistory201Response get_codes_history(get_my_codes_request)

Get codes history

This endpoint retrieves the whole [codes](/glossary#whitebit-codes) history on your account.

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
from main_api_generated.models.get_codes_history201_response import GetCodesHistory201Response
from main_api_generated.models.get_my_codes_request import GetMyCodesRequest
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
    api_instance = main_api_generated.CodesApi(api_client)
    get_my_codes_request = {"request":"{{request}}","nonce":"{{nonce}}"} # GetMyCodesRequest | 

    try:
        # Get codes history
        api_response = await api_instance.get_codes_history(get_my_codes_request)
        print("The response of CodesApi->get_codes_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodesApi->get_codes_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_my_codes_request** | [**GetMyCodesRequest**](GetMyCodesRequest.md)|  | 

### Return type

[**GetCodesHistory201Response**](GetCodesHistory201Response.md)

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

# **get_my_codes**
> GetMyCodes201Response get_my_codes(get_my_codes_request)

Get my codes

This endpoint retrieves the list of [WhiteBIT codes](/glossary#whitebit-codes) created by my account.

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
from main_api_generated.models.get_my_codes201_response import GetMyCodes201Response
from main_api_generated.models.get_my_codes_request import GetMyCodesRequest
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
    api_instance = main_api_generated.CodesApi(api_client)
    get_my_codes_request = {"request":"{{request}}","nonce":"{{nonce}}"} # GetMyCodesRequest | 

    try:
        # Get my codes
        api_response = await api_instance.get_my_codes(get_my_codes_request)
        print("The response of CodesApi->get_my_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodesApi->get_my_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_my_codes_request** | [**GetMyCodesRequest**](GetMyCodesRequest.md)|  | 

### Return type

[**GetMyCodes201Response**](GetMyCodes201Response.md)

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

