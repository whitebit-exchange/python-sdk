# CreateNewAddress201ResponseRequired


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_amount** | **str** | Max amount of deposit that can be accepted by exchange - if you deposit more than that number, it won&#39;t be accepted by exchange | [optional] 
**min_amount** | **str** | Min amount of deposit that accepted by exchange - if you deposit less than that number, it won&#39;t be accepted by exchange | [optional] 
**fixed_fee** | **str** | Fixed deposit fee | [optional] 
**flex_fee** | [**GetDepositAddress200ResponseRequiredFlexFee**](GetDepositAddress200ResponseRequiredFlexFee.md) |  | [optional] 

## Example

```python
from main_api_generated.models.create_new_address201_response_required import CreateNewAddress201ResponseRequired

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewAddress201ResponseRequired from a JSON string
create_new_address201_response_required_instance = CreateNewAddress201ResponseRequired.from_json(json)
# print the JSON string representation of the object
print(CreateNewAddress201ResponseRequired.to_json())

# convert the object into a dict
create_new_address201_response_required_dict = create_new_address201_response_required_instance.to_dict()
# create an instance of CreateNewAddress201ResponseRequired from a dict
create_new_address201_response_required_from_dict = CreateNewAddress201ResponseRequired.from_dict(create_new_address201_response_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


