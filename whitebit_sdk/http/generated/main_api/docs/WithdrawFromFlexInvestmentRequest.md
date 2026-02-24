# WithdrawFromFlexInvestmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | **str** | Plan external ID (UUID). | 
**amount** | **str** | Withdrawal amount. | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 

## Example

```python
from main_api_generated.models.withdraw_from_flex_investment_request import WithdrawFromFlexInvestmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawFromFlexInvestmentRequest from a JSON string
withdraw_from_flex_investment_request_instance = WithdrawFromFlexInvestmentRequest.from_json(json)
# print the JSON string representation of the object
print(WithdrawFromFlexInvestmentRequest.to_json())

# convert the object into a dict
withdraw_from_flex_investment_request_dict = withdraw_from_flex_investment_request_instance.to_dict()
# create an instance of WithdrawFromFlexInvestmentRequest from a dict
withdraw_from_flex_investment_request_from_dict = WithdrawFromFlexInvestmentRequest.from_dict(withdraw_from_flex_investment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


