# CloseFlexInvestmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | **str** | Plan external ID (UUID). | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 

## Example

```python
from main_api_generated.models.close_flex_investment_request import CloseFlexInvestmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloseFlexInvestmentRequest from a JSON string
close_flex_investment_request_instance = CloseFlexInvestmentRequest.from_json(json)
# print the JSON string representation of the object
print(CloseFlexInvestmentRequest.to_json())

# convert the object into a dict
close_flex_investment_request_dict = close_flex_investment_request_instance.to_dict()
# create an instance of CloseFlexInvestmentRequest from a dict
close_flex_investment_request_from_dict = CloseFlexInvestmentRequest.from_dict(close_flex_investment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


