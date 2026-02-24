# FeeInfoWithdraw

Withdrawal fees and limits

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_flex** | **str** | Minimum fee amount when flex fee is enabled | [optional] 
**max_flex** | **str** | Maximum fee amount when flex fee is enabled | [optional] 
**percent_flex** | **str** | Flex fee percent | [optional] 
**fixed** | **str** | Fixed fee | [optional] 
**min_amount** | **str** | Minimum withdrawal amount | [optional] 
**max_amount** | **str** | Maximum withdrawal amount | [optional] 

## Example

```python
from main_api_generated.models.fee_info_withdraw import FeeInfoWithdraw

# TODO update the JSON string below
json = "{}"
# create an instance of FeeInfoWithdraw from a JSON string
fee_info_withdraw_instance = FeeInfoWithdraw.from_json(json)
# print the JSON string representation of the object
print(FeeInfoWithdraw.to_json())

# convert the object into a dict
fee_info_withdraw_dict = fee_info_withdraw_instance.to_dict()
# create an instance of FeeInfoWithdraw from a dict
fee_info_withdraw_from_dict = FeeInfoWithdraw.from_dict(fee_info_withdraw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


