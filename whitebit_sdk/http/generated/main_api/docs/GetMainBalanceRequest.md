# GetMainBalanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**ticker** | **str** | Currency&#39;s ticker. | [optional] 

## Example

```python
from main_api_generated.models.get_main_balance_request import GetMainBalanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMainBalanceRequest from a JSON string
get_main_balance_request_instance = GetMainBalanceRequest.from_json(json)
# print the JSON string representation of the object
print(GetMainBalanceRequest.to_json())

# convert the object into a dict
get_main_balance_request_dict = get_main_balance_request_instance.to_dict()
# create an instance of GetMainBalanceRequest from a dict
get_main_balance_request_from_dict = GetMainBalanceRequest.from_dict(get_main_balance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


