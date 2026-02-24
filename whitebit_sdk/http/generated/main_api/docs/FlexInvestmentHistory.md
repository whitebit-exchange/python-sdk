# FlexInvestmentHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** | Transaction creation timestamp | [optional] 
**plan_id** | **str** | Flex plan identifier | [optional] 
**investment_id** | **str** | Flex investment identifier | [optional] 
**currency** | **str** | Transaction currency | [optional] 
**amount** | **str** | Transaction amount | [optional] 
**transaction_id** | **str** | Transaction identifier | [optional] 
**action_type** | **int** | Action type: 1-INVEST, 2-REINVEST, 3-WITHDRAW_FROM_INVESTMENT, 4-DAILY_EARNING, 5-CLOSE_INVESTMENT, 6-OPEN_INVESTMENT | [optional] 

## Example

```python
from main_api_generated.models.flex_investment_history import FlexInvestmentHistory

# TODO update the JSON string below
json = "{}"
# create an instance of FlexInvestmentHistory from a JSON string
flex_investment_history_instance = FlexInvestmentHistory.from_json(json)
# print the JSON string representation of the object
print(FlexInvestmentHistory.to_json())

# convert the object into a dict
flex_investment_history_dict = flex_investment_history_instance.to_dict()
# create an instance of FlexInvestmentHistory from a dict
flex_investment_history_from_dict = FlexInvestmentHistory.from_dict(flex_investment_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


