# main_api_generated.MiningPoolApi

All URIs are relative to *https://whitebit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mining_hashrate**](MiningPoolApi.md#get_mining_hashrate) | **POST** /api/v4/mining/hashrate | Get Mining Account Hashrate
[**get_mining_rewards**](MiningPoolApi.md#get_mining_rewards) | **POST** /api/v4/mining/rewards | Get Rewards


# **get_mining_hashrate**
> GetMiningHashrate200Response get_mining_hashrate(get_mining_hashrate_request)

Get Mining Account Hashrate

This endpoint returns hashrate of mining pool account.

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
from main_api_generated.models.get_mining_hashrate200_response import GetMiningHashrate200Response
from main_api_generated.models.get_mining_hashrate_request import GetMiningHashrateRequest
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
    api_instance = main_api_generated.MiningPoolApi(api_client)
    get_mining_hashrate_request = main_api_generated.GetMiningHashrateRequest() # GetMiningHashrateRequest | 

    try:
        # Get Mining Account Hashrate
        api_response = await api_instance.get_mining_hashrate(get_mining_hashrate_request)
        print("The response of MiningPoolApi->get_mining_hashrate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningPoolApi->get_mining_hashrate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_mining_hashrate_request** | [**GetMiningHashrateRequest**](GetMiningHashrateRequest.md)|  | 

### Return type

[**GetMiningHashrate200Response**](GetMiningHashrate200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**422** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mining_rewards**
> GetMiningRewards200Response get_mining_rewards(get_mining_rewards_request)

Get Rewards

This endpoint returns rewards received from mining.

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
from main_api_generated.models.get_mining_rewards200_response import GetMiningRewards200Response
from main_api_generated.models.get_mining_rewards_request import GetMiningRewardsRequest
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
    api_instance = main_api_generated.MiningPoolApi(api_client)
    get_mining_rewards_request = main_api_generated.GetMiningRewardsRequest() # GetMiningRewardsRequest | 

    try:
        # Get Rewards
        api_response = await api_instance.get_mining_rewards(get_mining_rewards_request)
        print("The response of MiningPoolApi->get_mining_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiningPoolApi->get_mining_rewards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_mining_rewards_request** | [**GetMiningRewardsRequest**](GetMiningRewardsRequest.md)|  | 

### Return type

[**GetMiningRewards200Response**](GetMiningRewards200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**422** | Request validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

