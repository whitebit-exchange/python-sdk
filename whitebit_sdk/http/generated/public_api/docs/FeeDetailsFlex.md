# FeeDetailsFlex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_fee** | **str** |  | [optional] 
**max_fee** | **str** |  | [optional] 
**percent** | **str** |  | [optional] 

## Example

```python
from public_api_generated.models.fee_details_flex import FeeDetailsFlex

# TODO update the JSON string below
json = "{}"
# create an instance of FeeDetailsFlex from a JSON string
fee_details_flex_instance = FeeDetailsFlex.from_json(json)
# print the JSON string representation of the object
print(FeeDetailsFlex.to_json())

# convert the object into a dict
fee_details_flex_dict = fee_details_flex_instance.to_dict()
# create an instance of FeeDetailsFlex from a dict
fee_details_flex_from_dict = FeeDetailsFlex.from_dict(fee_details_flex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


