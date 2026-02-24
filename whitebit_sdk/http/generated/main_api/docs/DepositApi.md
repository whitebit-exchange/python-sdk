# main_api_generated.DepositApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_address**](DepositApi.md#create_new_address) | **POST** /api/v4/main-account/create-new-address | Create new address for deposit
[**get_deposit_address**](DepositApi.md#get_deposit_address) | **POST** /api/v4/main-account/address | Get cryptocurrency deposit address
[**get_fiat_deposit_url**](DepositApi.md#get_fiat_deposit_url) | **POST** /api/v4/main-account/fiat-deposit-url | Get fiat deposit address
[**issue_card_token**](DepositApi.md#issue_card_token) | **POST** /api/card-token | Issue card token


# **create_new_address**
> CreateNewAddress201Response create_new_address(create_new_address_request)

Create new address for deposit

This endpoint creates a new address even when the last created address is not used. This endpoint is not available by default, you need to contact support@whitebit.com in order to get permissions to use this endpoint.

**Address types:**

| Currency | Types               | Default |
|----------|---------------------|---------|
| BTC      | p2sh-segwit, bech32 | bech32  |
| LTC      | p2sh-segwit, bech32 | bech32  |

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
from main_api_generated.models.create_new_address201_response import CreateNewAddress201Response
from main_api_generated.models.create_new_address_request import CreateNewAddressRequest
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
    api_instance = main_api_generated.DepositApi(api_client)
    create_new_address_request = {"ticker":"XLM","request":"{{request}}","nonce":"{{nonce}}"} # CreateNewAddressRequest | 

    try:
        # Create new address for deposit
        api_response = await api_instance.create_new_address(create_new_address_request)
        print("The response of DepositApi->create_new_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepositApi->create_new_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_new_address_request** | [**CreateNewAddressRequest**](CreateNewAddressRequest.md)|  | 

### Return type

[**CreateNewAddress201Response**](CreateNewAddress201Response.md)

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

# **get_deposit_address**
> GetDepositAddress200Response get_deposit_address(get_deposit_address_request)

Get cryptocurrency deposit address

This endpoint retrieves a deposit address of the cryptocurrency.

<Accordion title="Errors">
```json
{
  "code": 0,
  "message": "Validation failed",
  "errors": {
    "ticker": ["The selected ticker is invalid."]
  }
}
```

```json
{
  "code": 0,
  "message": "Validation failed",
  "errors": {
    "network": ["The selected network is invalid."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "ticker": ["Currency is not depositable"]
  }
}
```
</Accordion>

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
from main_api_generated.models.get_deposit_address200_response import GetDepositAddress200Response
from main_api_generated.models.get_deposit_address_request import GetDepositAddressRequest
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
    api_instance = main_api_generated.DepositApi(api_client)
    get_deposit_address_request = main_api_generated.GetDepositAddressRequest() # GetDepositAddressRequest | 

    try:
        # Get cryptocurrency deposit address
        api_response = await api_instance.get_deposit_address(get_deposit_address_request)
        print("The response of DepositApi->get_deposit_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepositApi->get_deposit_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_deposit_address_request** | [**GetDepositAddressRequest**](GetDepositAddressRequest.md)|  | 

### Return type

[**GetDepositAddress200Response**](GetDepositAddress200Response.md)

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
**503** | Service temporary unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiat_deposit_url**
> GetFiatDepositUrl200Response get_fiat_deposit_url(get_fiat_deposit_url_request)

Get fiat deposit address

This endpoint retrieves a deposit url of the [fiat](/glossary#fiat) invoice.

Please, pay attention that this endpoint works on demand. It means that you need to contact WhiteBIT support and provide your API key to get access to this functionality.

<Accordion title="Errors">
```json
{
  "code": 0,
  "message": "Validation failed",
  "errors": {
    "ticker": ["The ticker field is required."],
    "provider": ["The provider field is required."]
  }
}
```

```json
{
  "code": 0,
  "message": "Validation failed",
  "errors": {
    "amount": ["Current limit exceeded"]
  }
}
```
</Accordion>

<Warning>
If you have used VISAMASTER as [provider](/glossary#provider), you must pass [referer header](https://developer.mozilla.org/ru/docs/Web/HTTP/Headers/Referer) when you go to the invoice link (for example, pass referer header when you go to https://someaddress.com). Otherwise if there is no header (for example, you go to https://someaddress.com from Telegram message) you will be redirected to the WhiteBIT homepage
</Warning>

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
from main_api_generated.models.get_fiat_deposit_url200_response import GetFiatDepositUrl200Response
from main_api_generated.models.get_fiat_deposit_url_request import GetFiatDepositUrlRequest
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
    api_instance = main_api_generated.DepositApi(api_client)
    get_fiat_deposit_url_request = {"ticker":"UAH","provider":"VISAMASTER","amount":"100","uniqueId":"{{generateID}}","request":"{{request}}","nonce":"{{nonce}}"} # GetFiatDepositUrlRequest | 

    try:
        # Get fiat deposit address
        api_response = await api_instance.get_fiat_deposit_url(get_fiat_deposit_url_request)
        print("The response of DepositApi->get_fiat_deposit_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepositApi->get_fiat_deposit_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_fiat_deposit_url_request** | [**GetFiatDepositUrlRequest**](GetFiatDepositUrlRequest.md)|  | 

### Return type

[**GetFiatDepositUrl200Response**](GetFiatDepositUrl200Response.md)

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
**503** | Service temporary unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_card_token**
> issue_card_token(issue_card_token_request)

Issue card token

This endpoint issues a [card token](/glossary#card-token) for the specified card number.

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
from main_api_generated.models.issue_card_token_request import IssueCardTokenRequest
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
    api_instance = main_api_generated.DepositApi(api_client)
    issue_card_token_request = {"cardNumber":"4111111111111111"} # IssueCardTokenRequest | 

    try:
        # Issue card token
        await api_instance.issue_card_token(issue_card_token_request)
    except Exception as e:
        print("Exception when calling DepositApi->issue_card_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_card_token_request** | [**IssueCardTokenRequest**](IssueCardTokenRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Validation succeeded and card token is returned |  -  |
**401** | Request authorization failed |  -  |
**422** | Inner validation failed  Response error codes: - 1 - specified card number is invalid  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

