# GetDepositAddress200ResponseRequired


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_fee** | **str** | Fixed deposit fee | [optional] 
**flex_fee** | [**GetDepositAddress200ResponseRequiredFlexFee**](GetDepositAddress200ResponseRequiredFlexFee.md) |  | [optional] 
**max_amount** | **str** | Max amount of deposit that can be accepted by exchange - if you deposit more than that number, it won&#39;t be accepted by exchange | [optional] 
**min_amount** | **str** | Min amount of deposit that can be accepted by exchange - if you will deposit less than that number, it won&#39;t be accepted by exchange | [optional] 

## Example

```python
from main_api_generated.models.get_deposit_address200_response_required import GetDepositAddress200ResponseRequired

# TODO update the JSON string below
json = "{}"
# create an instance of GetDepositAddress200ResponseRequired from a JSON string
get_deposit_address200_response_required_instance = GetDepositAddress200ResponseRequired.from_json(json)
# print the JSON string representation of the object
print(GetDepositAddress200ResponseRequired.to_json())

# convert the object into a dict
get_deposit_address200_response_required_dict = get_deposit_address200_response_required_instance.to_dict()
# create an instance of GetDepositAddress200ResponseRequired from a dict
get_deposit_address200_response_required_from_dict = GetDepositAddress200ResponseRequired.from_dict(get_deposit_address200_response_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


