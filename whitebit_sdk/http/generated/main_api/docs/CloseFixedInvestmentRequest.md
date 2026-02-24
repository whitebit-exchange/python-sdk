# CloseFixedInvestmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Investment identifier | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 

## Example

```python
from main_api_generated.models.close_fixed_investment_request import CloseFixedInvestmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloseFixedInvestmentRequest from a JSON string
close_fixed_investment_request_instance = CloseFixedInvestmentRequest.from_json(json)
# print the JSON string representation of the object
print(CloseFixedInvestmentRequest.to_json())

# convert the object into a dict
close_fixed_investment_request_dict = close_fixed_investment_request_instance.to_dict()
# create an instance of CloseFixedInvestmentRequest from a dict
close_fixed_investment_request_from_dict = CloseFixedInvestmentRequest.from_dict(close_fixed_investment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


