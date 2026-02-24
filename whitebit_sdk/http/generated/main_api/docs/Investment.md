# Investment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Investment identifier | [optional] 
**plan** | [**FixedPlan**](FixedPlan.md) |  | [optional] 
**status** | **int** | Investment status (1 - active, 2 - closed) | [optional] 
**created** | **int** | Timestamp of investment creation | [optional] 
**updated** | **int** | Timestamp of investment update | [optional] 
**payment_time** | **int** | Timestamp of the payment time | [optional] 
**amount** | **str** | Investment amount | [optional] 
**interest_paid** | **str** | Interest paid amount | [optional] 

## Example

```python
from main_api_generated.models.investment import Investment

# TODO update the JSON string below
json = "{}"
# create an instance of Investment from a JSON string
investment_instance = Investment.from_json(json)
# print the JSON string representation of the object
print(Investment.to_json())

# convert the object into a dict
investment_dict = investment_instance.to_dict()
# create an instance of Investment from a dict
investment_from_dict = Investment.from_dict(investment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


