# main_api_generated.SubAccountAPIKeysApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sub_account_api_key**](SubAccountAPIKeysApi.md#create_sub_account_api_key) | **POST** /api/v4/sub-account/api-key/create | Create Sub-Account API Key
[**create_sub_account_api_key_ip_address**](SubAccountAPIKeysApi.md#create_sub_account_api_key_ip_address) | **POST** /api/v4/sub-account/api-key/ip-address/create | Create Sub-Account API Key IP Address
[**delete_sub_account_api_key**](SubAccountAPIKeysApi.md#delete_sub_account_api_key) | **POST** /api/v4/sub-account/api-key/delete | Delete Sub-Account API Key
[**delete_sub_account_api_key_ip_address**](SubAccountAPIKeysApi.md#delete_sub_account_api_key_ip_address) | **POST** /api/v4/sub-account/api-key/ip-address/delete | Delete Sub-Account API Key IP Address
[**edit_sub_account_api_key**](SubAccountAPIKeysApi.md#edit_sub_account_api_key) | **POST** /api/v4/sub-account/api-key/edit | Edit Sub-Account API Key
[**list_sub_account_api_key_ip_addresses**](SubAccountAPIKeysApi.md#list_sub_account_api_key_ip_addresses) | **POST** /api/v4/sub-account/api-key/ip-address/list | List Sub-Account API Key IP Addresses
[**list_sub_account_api_keys**](SubAccountAPIKeysApi.md#list_sub_account_api_keys) | **POST** /api/v4/sub-account/api-key/list | List Sub-Account API Keys
[**reset_sub_account_api_key**](SubAccountAPIKeysApi.md#reset_sub_account_api_key) | **POST** /api/v4/sub-account/api-key/reset | Reset Sub-Account API Key


# **create_sub_account_api_key**
> SubAccountApiKey create_sub_account_api_key(create_sub_account_api_key_request)

Create Sub-Account API Key

This endpoint creates a new API key for a [sub-account](/glossary#sub-account).

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
from main_api_generated.models.create_sub_account_api_key_request import CreateSubAccountApiKeyRequest
from main_api_generated.models.sub_account_api_key import SubAccountApiKey
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
    api_instance = main_api_generated.SubAccountAPIKeysApi(api_client)
    create_sub_account_api_key_request = main_api_generated.CreateSubAccountApiKeyRequest() # CreateSubAccountApiKeyRequest | 

    try:
        # Create Sub-Account API Key
        api_response = await api_instance.create_sub_account_api_key(create_sub_account_api_key_request)
        print("The response of SubAccountAPIKeysApi->create_sub_account_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountAPIKeysApi->create_sub_account_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sub_account_api_key_request** | [**CreateSubAccountApiKeyRequest**](CreateSubAccountApiKeyRequest.md)|  | 

### Return type

[**SubAccountApiKey**](SubAccountApiKey.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | API key created successfully |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sub_account_api_key_ip_address**
> ListSubAccountApiKeyIpAddresses200Response create_sub_account_api_key_ip_address(create_sub_account_api_key_ip_address_request)

Create Sub-Account API Key IP Address

This endpoint adds a new IP address to the allowed list for a [sub-account](/glossary#sub-account) API key.

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
from main_api_generated.models.create_sub_account_api_key_ip_address_request import CreateSubAccountApiKeyIpAddressRequest
from main_api_generated.models.list_sub_account_api_key_ip_addresses200_response import ListSubAccountApiKeyIpAddresses200Response
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
    api_instance = main_api_generated.SubAccountAPIKeysApi(api_client)
    create_sub_account_api_key_ip_address_request = main_api_generated.CreateSubAccountApiKeyIpAddressRequest() # CreateSubAccountApiKeyIpAddressRequest | 

    try:
        # Create Sub-Account API Key IP Address
        api_response = await api_instance.create_sub_account_api_key_ip_address(create_sub_account_api_key_ip_address_request)
        print("The response of SubAccountAPIKeysApi->create_sub_account_api_key_ip_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountAPIKeysApi->create_sub_account_api_key_ip_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sub_account_api_key_ip_address_request** | [**CreateSubAccountApiKeyIpAddressRequest**](CreateSubAccountApiKeyIpAddressRequest.md)|  | 

### Return type

[**ListSubAccountApiKeyIpAddresses200Response**](ListSubAccountApiKeyIpAddresses200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | IP address added successfully |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sub_account_api_key**
> object delete_sub_account_api_key(delete_sub_account_api_key_request)

Delete Sub-Account API Key

This endpoint deletes a [sub-account](/glossary#sub-account) API key.

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
from main_api_generated.models.delete_sub_account_api_key_request import DeleteSubAccountApiKeyRequest
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
    api_instance = main_api_generated.SubAccountAPIKeysApi(api_client)
    delete_sub_account_api_key_request = main_api_generated.DeleteSubAccountApiKeyRequest() # DeleteSubAccountApiKeyRequest | 

    try:
        # Delete Sub-Account API Key
        api_response = await api_instance.delete_sub_account_api_key(delete_sub_account_api_key_request)
        print("The response of SubAccountAPIKeysApi->delete_sub_account_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountAPIKeysApi->delete_sub_account_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_sub_account_api_key_request** | [**DeleteSubAccountApiKeyRequest**](DeleteSubAccountApiKeyRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key deleted successfully |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sub_account_api_key_ip_address**
> ListSubAccountApiKeyIpAddresses200Response delete_sub_account_api_key_ip_address(delete_sub_account_api_key_ip_address_request)

Delete Sub-Account API Key IP Address

This endpoint removes an IP address from the allowed list for a [sub-account](/glossary#sub-account) API key.

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
from main_api_generated.models.delete_sub_account_api_key_ip_address_request import DeleteSubAccountApiKeyIpAddressRequest
from main_api_generated.models.list_sub_account_api_key_ip_addresses200_response import ListSubAccountApiKeyIpAddresses200Response
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
    api_instance = main_api_generated.SubAccountAPIKeysApi(api_client)
    delete_sub_account_api_key_ip_address_request = main_api_generated.DeleteSubAccountApiKeyIpAddressRequest() # DeleteSubAccountApiKeyIpAddressRequest | 

    try:
        # Delete Sub-Account API Key IP Address
        api_response = await api_instance.delete_sub_account_api_key_ip_address(delete_sub_account_api_key_ip_address_request)
        print("The response of SubAccountAPIKeysApi->delete_sub_account_api_key_ip_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountAPIKeysApi->delete_sub_account_api_key_ip_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_sub_account_api_key_ip_address_request** | [**DeleteSubAccountApiKeyIpAddressRequest**](DeleteSubAccountApiKeyIpAddressRequest.md)|  | 

### Return type

[**ListSubAccountApiKeyIpAddresses200Response**](ListSubAccountApiKeyIpAddresses200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP address removed successfully |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_sub_account_api_key**
> object edit_sub_account_api_key(edit_sub_account_api_key_request)

Edit Sub-Account API Key

This endpoint updates an existing [sub-account](/glossary#sub-account) API key.

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
from main_api_generated.models.edit_sub_account_api_key_request import EditSubAccountApiKeyRequest
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
    api_instance = main_api_generated.SubAccountAPIKeysApi(api_client)
    edit_sub_account_api_key_request = main_api_generated.EditSubAccountApiKeyRequest() # EditSubAccountApiKeyRequest | 

    try:
        # Edit Sub-Account API Key
        api_response = await api_instance.edit_sub_account_api_key(edit_sub_account_api_key_request)
        print("The response of SubAccountAPIKeysApi->edit_sub_account_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountAPIKeysApi->edit_sub_account_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_sub_account_api_key_request** | [**EditSubAccountApiKeyRequest**](EditSubAccountApiKeyRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key updated successfully |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sub_account_api_key_ip_addresses**
> ListSubAccountApiKeyIpAddresses200Response list_sub_account_api_key_ip_addresses(list_sub_account_api_key_ip_addresses_request)

List Sub-Account API Key IP Addresses

This endpoint retrieves the list of IP addresses allowed for a [sub-account](/glossary#sub-account) API key.

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
from main_api_generated.models.list_sub_account_api_key_ip_addresses200_response import ListSubAccountApiKeyIpAddresses200Response
from main_api_generated.models.list_sub_account_api_key_ip_addresses_request import ListSubAccountApiKeyIpAddressesRequest
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
    api_instance = main_api_generated.SubAccountAPIKeysApi(api_client)
    list_sub_account_api_key_ip_addresses_request = main_api_generated.ListSubAccountApiKeyIpAddressesRequest() # ListSubAccountApiKeyIpAddressesRequest | 

    try:
        # List Sub-Account API Key IP Addresses
        api_response = await api_instance.list_sub_account_api_key_ip_addresses(list_sub_account_api_key_ip_addresses_request)
        print("The response of SubAccountAPIKeysApi->list_sub_account_api_key_ip_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountAPIKeysApi->list_sub_account_api_key_ip_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_sub_account_api_key_ip_addresses_request** | [**ListSubAccountApiKeyIpAddressesRequest**](ListSubAccountApiKeyIpAddressesRequest.md)|  | 

### Return type

[**ListSubAccountApiKeyIpAddresses200Response**](ListSubAccountApiKeyIpAddresses200Response.md)

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

# **list_sub_account_api_keys**
> ListSubAccountApiKeys200Response list_sub_account_api_keys(list_sub_account_api_keys_request)

List Sub-Account API Keys

This endpoint retrieves a list of API keys for a [sub-account](/glossary#sub-account).
Note: For security reasons, the apiSecret field returns an empty string.

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
from main_api_generated.models.list_sub_account_api_keys200_response import ListSubAccountApiKeys200Response
from main_api_generated.models.list_sub_account_api_keys_request import ListSubAccountApiKeysRequest
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
    api_instance = main_api_generated.SubAccountAPIKeysApi(api_client)
    list_sub_account_api_keys_request = main_api_generated.ListSubAccountApiKeysRequest() # ListSubAccountApiKeysRequest | 

    try:
        # List Sub-Account API Keys
        api_response = await api_instance.list_sub_account_api_keys(list_sub_account_api_keys_request)
        print("The response of SubAccountAPIKeysApi->list_sub_account_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountAPIKeysApi->list_sub_account_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_sub_account_api_keys_request** | [**ListSubAccountApiKeysRequest**](ListSubAccountApiKeysRequest.md)|  | 

### Return type

[**ListSubAccountApiKeys200Response**](ListSubAccountApiKeys200Response.md)

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

# **reset_sub_account_api_key**
> object reset_sub_account_api_key(reset_sub_account_api_key_request)

Reset Sub-Account API Key

This endpoint resets (regenerates) an existing [sub-account](/glossary#sub-account) API key.

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
from main_api_generated.models.reset_sub_account_api_key_request import ResetSubAccountApiKeyRequest
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
    api_instance = main_api_generated.SubAccountAPIKeysApi(api_client)
    reset_sub_account_api_key_request = main_api_generated.ResetSubAccountApiKeyRequest() # ResetSubAccountApiKeyRequest | 

    try:
        # Reset Sub-Account API Key
        api_response = await api_instance.reset_sub_account_api_key(reset_sub_account_api_key_request)
        print("The response of SubAccountAPIKeysApi->reset_sub_account_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountAPIKeysApi->reset_sub_account_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_sub_account_api_key_request** | [**ResetSubAccountApiKeyRequest**](ResetSubAccountApiKeyRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key reset successfully |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

