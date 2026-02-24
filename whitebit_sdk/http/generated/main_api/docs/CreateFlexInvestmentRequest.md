# CreateFlexInvestmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | **str** | Plan external ID (UUID). | 
**amount** | **str** | Investment amount. | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**with_reinvest** | **bool** | Enable auto-reinvestment. | [optional] [default to False]

## Example

```python
from main_api_generated.models.create_flex_investment_request import CreateFlexInvestmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFlexInvestmentRequest from a JSON string
create_flex_investment_request_instance = CreateFlexInvestmentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFlexInvestmentRequest.to_json())

# convert the object into a dict
create_flex_investment_request_dict = create_flex_investment_request_instance.to_dict()
# create an instance of CreateFlexInvestmentRequest from a dict
create_flex_investment_request_from_dict = CreateFlexInvestmentRequest.from_dict(create_flex_investment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


