# GetSubAccountBalances200ResponseValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main** | **str** |  | [optional] 
**spot** | **str** |  | [optional] 
**collateral** | **str** |  | [optional] 

## Example

```python
from main_api_generated.models.get_sub_account_balances200_response_value_inner import GetSubAccountBalances200ResponseValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountBalances200ResponseValueInner from a JSON string
get_sub_account_balances200_response_value_inner_instance = GetSubAccountBalances200ResponseValueInner.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountBalances200ResponseValueInner.to_json())

# convert the object into a dict
get_sub_account_balances200_response_value_inner_dict = get_sub_account_balances200_response_value_inner_instance.to_dict()
# create an instance of GetSubAccountBalances200ResponseValueInner from a dict
get_sub_account_balances200_response_value_inner_from_dict = GetSubAccountBalances200ResponseValueInner.from_dict(get_sub_account_balances200_response_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


