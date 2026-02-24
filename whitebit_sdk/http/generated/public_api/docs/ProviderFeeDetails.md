# ProviderFeeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_amount** | **str** |  | [optional] 
**max_amount** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**flex** | **str** |  | [optional] 
**is_depositable** | **bool** |  | [optional] 
**is_api_depositable** | **bool** |  | [optional] 
**is_withdrawal** | **bool** |  | [optional] 
**is_api_withdrawal** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**ticker** | **str** |  | [optional] 

## Example

```python
from public_api_generated.models.provider_fee_details import ProviderFeeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderFeeDetails from a JSON string
provider_fee_details_instance = ProviderFeeDetails.from_json(json)
# print the JSON string representation of the object
print(ProviderFeeDetails.to_json())

# convert the object into a dict
provider_fee_details_dict = provider_fee_details_instance.to_dict()
# create an instance of ProviderFeeDetails from a dict
provider_fee_details_from_dict = ProviderFeeDetails.from_dict(provider_fee_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


