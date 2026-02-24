# CreateFlexInvestment201ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Transaction ID for the investment | [optional] 

## Example

```python
from main_api_generated.models.create_flex_investment201_response_data import CreateFlexInvestment201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFlexInvestment201ResponseData from a JSON string
create_flex_investment201_response_data_instance = CreateFlexInvestment201ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateFlexInvestment201ResponseData.to_json())

# convert the object into a dict
create_flex_investment201_response_data_dict = create_flex_investment201_response_data_instance.to_dict()
# create an instance of CreateFlexInvestment201ResponseData from a dict
create_flex_investment201_response_data_from_dict = CreateFlexInvestment201ResponseData.from_dict(create_flex_investment201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


