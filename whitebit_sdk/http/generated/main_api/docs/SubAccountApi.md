# main_api_generated.SubAccountApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**block_sub_account**](SubAccountApi.md#block_sub_account) | **POST** /api/v4/sub-account/block | Block Sub-Account
[**create_sub_account**](SubAccountApi.md#create_sub_account) | **POST** /api/v4/sub-account/create | Create Sub-Account
[**delete_sub_account**](SubAccountApi.md#delete_sub_account) | **POST** /api/v4/sub-account/delete | Delete Sub-Account
[**edit_sub_account**](SubAccountApi.md#edit_sub_account) | **POST** /api/v4/sub-account/edit | Edit Sub-Account
[**get_sub_account_balances**](SubAccountApi.md#get_sub_account_balances) | **POST** /api/v4/sub-account/balances | Sub-Account Balances
[**get_sub_account_transfer_history**](SubAccountApi.md#get_sub_account_transfer_history) | **POST** /api/v4/sub-account/transfer/history | Get Sub-Account Transfer History
[**list_sub_accounts**](SubAccountApi.md#list_sub_accounts) | **POST** /api/v4/sub-account/list | List of Sub-Accounts
[**sub_account_transfer**](SubAccountApi.md#sub_account_transfer) | **POST** /api/v4/sub-account/transfer | Sub-Account Transfer
[**unblock_sub_account**](SubAccountApi.md#unblock_sub_account) | **POST** /api/v4/sub-account/unblock | Unblock Sub-Account


# **block_sub_account**
> object block_sub_account(delete_sub_account_request)

Block Sub-Account

This endpoint blocks [sub-account](/glossary#sub-account).

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
from main_api_generated.models.delete_sub_account_request import DeleteSubAccountRequest
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
    api_instance = main_api_generated.SubAccountApi(api_client)
    delete_sub_account_request = main_api_generated.DeleteSubAccountRequest() # DeleteSubAccountRequest | 

    try:
        # Block Sub-Account
        api_response = await api_instance.block_sub_account(delete_sub_account_request)
        print("The response of SubAccountApi->block_sub_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountApi->block_sub_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_sub_account_request** | [**DeleteSubAccountRequest**](DeleteSubAccountRequest.md)|  | 

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
**200** | Sub-account blocked successfully |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sub_account**
> SubAccount create_sub_account(create_sub_account_request)

Create Sub-Account

This endpoint creates new [sub-account](/glossary#sub-account).

<Note>
The `email` field requirement depends on the `shareKyc` parameter:
- When `shareKyc` is `false` or not provided: `email` is **required**
- When `shareKyc` is `true`: `email` is **optional**
</Note>

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
from main_api_generated.models.create_sub_account_request import CreateSubAccountRequest
from main_api_generated.models.sub_account import SubAccount
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
    api_instance = main_api_generated.SubAccountApi(api_client)
    create_sub_account_request = main_api_generated.CreateSubAccountRequest() # CreateSubAccountRequest | 

    try:
        # Create Sub-Account
        api_response = await api_instance.create_sub_account(create_sub_account_request)
        print("The response of SubAccountApi->create_sub_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountApi->create_sub_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sub_account_request** | [**CreateSubAccountRequest**](CreateSubAccountRequest.md)|  | 

### Return type

[**SubAccount**](SubAccount.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sub-account created successfully |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sub_account**
> object delete_sub_account(delete_sub_account_request)

Delete Sub-Account

This endpoint deletes [sub-account](/glossary#sub-account).

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
from main_api_generated.models.delete_sub_account_request import DeleteSubAccountRequest
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
    api_instance = main_api_generated.SubAccountApi(api_client)
    delete_sub_account_request = main_api_generated.DeleteSubAccountRequest() # DeleteSubAccountRequest | 

    try:
        # Delete Sub-Account
        api_response = await api_instance.delete_sub_account(delete_sub_account_request)
        print("The response of SubAccountApi->delete_sub_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountApi->delete_sub_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_sub_account_request** | [**DeleteSubAccountRequest**](DeleteSubAccountRequest.md)|  | 

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
**200** | Sub-account deleted successfully |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_sub_account**
> object edit_sub_account(edit_sub_account_request)

Edit Sub-Account

This endpoint edits [sub-account](/glossary#sub-account).

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
from main_api_generated.models.edit_sub_account_request import EditSubAccountRequest
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
    api_instance = main_api_generated.SubAccountApi(api_client)
    edit_sub_account_request = main_api_generated.EditSubAccountRequest() # EditSubAccountRequest | 

    try:
        # Edit Sub-Account
        api_response = await api_instance.edit_sub_account(edit_sub_account_request)
        print("The response of SubAccountApi->edit_sub_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountApi->edit_sub_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_sub_account_request** | [**EditSubAccountRequest**](EditSubAccountRequest.md)|  | 

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
**200** | Sub-account edited successfully |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_account_balances**
> Dict[str, List[GetSubAccountBalances200ResponseValueInner]] get_sub_account_balances(get_sub_account_balances_request)

Sub-Account Balances

This endpoint returns [sub-account](/glossary#sub-account) balances.

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
from main_api_generated.models.get_sub_account_balances200_response_value_inner import GetSubAccountBalances200ResponseValueInner
from main_api_generated.models.get_sub_account_balances_request import GetSubAccountBalancesRequest
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
    api_instance = main_api_generated.SubAccountApi(api_client)
    get_sub_account_balances_request = main_api_generated.GetSubAccountBalancesRequest() # GetSubAccountBalancesRequest | 

    try:
        # Sub-Account Balances
        api_response = await api_instance.get_sub_account_balances(get_sub_account_balances_request)
        print("The response of SubAccountApi->get_sub_account_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountApi->get_sub_account_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_sub_account_balances_request** | [**GetSubAccountBalancesRequest**](GetSubAccountBalancesRequest.md)|  | 

### Return type

**Dict[str, List[GetSubAccountBalances200ResponseValueInner]]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**422** | Account is not confirmed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_account_transfer_history**
> GetSubAccountTransferHistory200Response get_sub_account_transfer_history(get_sub_account_transfer_history_request)

Get Sub-Account Transfer History

This endpoint returns history of transfers between main account and [sub-account](/glossary#sub-account).

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
from main_api_generated.models.get_sub_account_transfer_history200_response import GetSubAccountTransferHistory200Response
from main_api_generated.models.get_sub_account_transfer_history_request import GetSubAccountTransferHistoryRequest
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
    api_instance = main_api_generated.SubAccountApi(api_client)
    get_sub_account_transfer_history_request = main_api_generated.GetSubAccountTransferHistoryRequest() # GetSubAccountTransferHistoryRequest | 

    try:
        # Get Sub-Account Transfer History
        api_response = await api_instance.get_sub_account_transfer_history(get_sub_account_transfer_history_request)
        print("The response of SubAccountApi->get_sub_account_transfer_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountApi->get_sub_account_transfer_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_sub_account_transfer_history_request** | [**GetSubAccountTransferHistoryRequest**](GetSubAccountTransferHistoryRequest.md)|  | 

### Return type

[**GetSubAccountTransferHistory200Response**](GetSubAccountTransferHistory200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**422** | Account is not confirmed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sub_accounts**
> ListSubAccounts200Response list_sub_accounts(list_sub_accounts_request)

List of Sub-Accounts

This endpoint returns list of current user [sub-accounts](/glossary#sub-account).

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
from main_api_generated.models.list_sub_accounts200_response import ListSubAccounts200Response
from main_api_generated.models.list_sub_accounts_request import ListSubAccountsRequest
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
    api_instance = main_api_generated.SubAccountApi(api_client)
    list_sub_accounts_request = main_api_generated.ListSubAccountsRequest() # ListSubAccountsRequest | 

    try:
        # List of Sub-Accounts
        api_response = await api_instance.list_sub_accounts(list_sub_accounts_request)
        print("The response of SubAccountApi->list_sub_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountApi->list_sub_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_sub_accounts_request** | [**ListSubAccountsRequest**](ListSubAccountsRequest.md)|  | 

### Return type

[**ListSubAccounts200Response**](ListSubAccounts200Response.md)

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

# **sub_account_transfer**
> object sub_account_transfer(sub_account_transfer_request)

Sub-Account Transfer

This endpoint creates transfer from main account to [sub-account](/glossary#sub-account) or vice versa.

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
from main_api_generated.models.sub_account_transfer_request import SubAccountTransferRequest
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
    api_instance = main_api_generated.SubAccountApi(api_client)
    sub_account_transfer_request = main_api_generated.SubAccountTransferRequest() # SubAccountTransferRequest | 

    try:
        # Sub-Account Transfer
        api_response = await api_instance.sub_account_transfer(sub_account_transfer_request)
        print("The response of SubAccountApi->sub_account_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountApi->sub_account_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_transfer_request** | [**SubAccountTransferRequest**](SubAccountTransferRequest.md)|  | 

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
**200** | Transfer successful |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unblock_sub_account**
> object unblock_sub_account(delete_sub_account_request)

Unblock Sub-Account

This endpoint unblocks [sub-account](/glossary#sub-account).

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
from main_api_generated.models.delete_sub_account_request import DeleteSubAccountRequest
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
    api_instance = main_api_generated.SubAccountApi(api_client)
    delete_sub_account_request = main_api_generated.DeleteSubAccountRequest() # DeleteSubAccountRequest | 

    try:
        # Unblock Sub-Account
        api_response = await api_instance.unblock_sub_account(delete_sub_account_request)
        print("The response of SubAccountApi->unblock_sub_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountApi->unblock_sub_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_sub_account_request** | [**DeleteSubAccountRequest**](DeleteSubAccountRequest.md)|  | 

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
**200** | Sub-account unblocked successfully |  -  |
**400** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

