# FlexPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Flex plan identifier | [optional] 
**ticker** | **str** | Currency [ticker](/glossary#ticker) | [optional] 
**min_investment** | **str** | Minimum investment amount | [optional] 
**max_investment** | **str** | Maximum investment amount | [optional] 
**max_rate** | **str** | Maximum interest rate | [optional] 

## Example

```python
from main_api_generated.models.flex_plan import FlexPlan

# TODO update the JSON string below
json = "{}"
# create an instance of FlexPlan from a JSON string
flex_plan_instance = FlexPlan.from_json(json)
# print the JSON string representation of the object
print(FlexPlan.to_json())

# convert the object into a dict
flex_plan_dict = flex_plan_instance.to_dict()
# create an instance of FlexPlan from a dict
flex_plan_from_dict = FlexPlan.from_dict(flex_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


