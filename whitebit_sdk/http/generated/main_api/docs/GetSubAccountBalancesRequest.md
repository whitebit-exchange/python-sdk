# GetSubAccountBalancesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Sub-account id | 
**ticker** | **str** | Currency&#39;s ticker (if not provided, returns data by all currencies) | [optional] 

## Example

```python
from main_api_generated.models.get_sub_account_balances_request import GetSubAccountBalancesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountBalancesRequest from a JSON string
get_sub_account_balances_request_instance = GetSubAccountBalancesRequest.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountBalancesRequest.to_json())

# convert the object into a dict
get_sub_account_balances_request_dict = get_sub_account_balances_request_instance.to_dict()
# create an instance of GetSubAccountBalancesRequest from a dict
get_sub_account_balances_request_from_dict = GetSubAccountBalancesRequest.from_dict(get_sub_account_balances_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


