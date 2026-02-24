# FlexInvestment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Flex investment identifier | [optional] 
**plan_id** | **str** | Flex plan identifier | [optional] 
**currency** | **str** | Investment currency | [optional] 
**invested** | **str** | Invested amount | [optional] 
**with_auto_reinvest** | **bool** | Auto-reinvestment enabled | [optional] 
**status** | **int** | Investment status (1&#x3D;ACTIVE, 0&#x3D;CLOSED) | [optional] 
**created_at** | **int** | Investment creation timestamp | [optional] 
**updated_at** | **int** | Investment last update timestamp | [optional] 

## Example

```python
from main_api_generated.models.flex_investment import FlexInvestment

# TODO update the JSON string below
json = "{}"
# create an instance of FlexInvestment from a JSON string
flex_investment_instance = FlexInvestment.from_json(json)
# print the JSON string representation of the object
print(FlexInvestment.to_json())

# convert the object into a dict
flex_investment_dict = flex_investment_instance.to_dict()
# create an instance of FlexInvestment from a dict
flex_investment_from_dict = FlexInvestment.from_dict(flex_investment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


