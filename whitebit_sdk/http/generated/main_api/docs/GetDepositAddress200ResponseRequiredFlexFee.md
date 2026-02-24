# GetDepositAddress200ResponseRequiredFlexFee

Flexible fee - is fee that use percent rate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_fee** | **str** | Maximum fixed fee that you will pay | [optional] 
**min_fee** | **str** | Minimum fixed fee that you will pay | [optional] 
**percent** | **str** | Percent of deposit that you will pay | [optional] 

## Example

```python
from main_api_generated.models.get_deposit_address200_response_required_flex_fee import GetDepositAddress200ResponseRequiredFlexFee

# TODO update the JSON string below
json = "{}"
# create an instance of GetDepositAddress200ResponseRequiredFlexFee from a JSON string
get_deposit_address200_response_required_flex_fee_instance = GetDepositAddress200ResponseRequiredFlexFee.from_json(json)
# print the JSON string representation of the object
print(GetDepositAddress200ResponseRequiredFlexFee.to_json())

# convert the object into a dict
get_deposit_address200_response_required_flex_fee_dict = get_deposit_address200_response_required_flex_fee_instance.to_dict()
# create an instance of GetDepositAddress200ResponseRequiredFlexFee from a dict
get_deposit_address200_response_required_flex_fee_from_dict = GetDepositAddress200ResponseRequiredFlexFee.from_dict(get_deposit_address200_response_required_flex_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


