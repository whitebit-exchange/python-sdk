# FixedPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Invest plan identifier | [optional] 
**ticker** | **str** | Source currency ticker | [optional] 
**status** | **int** | Status (1 - active, 2 - no coins left, 3 - inactive, 4 - pause) | [optional] 
**percent** | **str** | Interest percent | [optional] 
**duration** | **int** | Investment duration (in minutes) | [optional] 
**interest_ticker** | **str** | Target currency ticker | [optional] 
**interest_ratio** | **str** | Target currency to source currency ratio | [optional] 
**min_investment** | **str** | Minimum investment amount | [optional] 
**max_investment** | **str** | Maximum investment amount | [optional] 
**max_possible_investment** | **str** | Maximum investment amount due to current invest plan state | [optional] 

## Example

```python
from main_api_generated.models.fixed_plan import FixedPlan

# TODO update the JSON string below
json = "{}"
# create an instance of FixedPlan from a JSON string
fixed_plan_instance = FixedPlan.from_json(json)
# print the JSON string representation of the object
print(FixedPlan.to_json())

# convert the object into a dict
fixed_plan_dict = fixed_plan_instance.to_dict()
# create an instance of FixedPlan from a dict
fixed_plan_from_dict = FixedPlan.from_dict(fixed_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


