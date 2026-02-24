# CreateFixedInvestmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** | [Invest plan](/glossary#crypto-lending) identifier | 
**amount** | **str** | Investment amount | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 

## Example

```python
from main_api_generated.models.create_fixed_investment_request import CreateFixedInvestmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFixedInvestmentRequest from a JSON string
create_fixed_investment_request_instance = CreateFixedInvestmentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFixedInvestmentRequest.to_json())

# convert the object into a dict
create_fixed_investment_request_dict = create_fixed_investment_request_instance.to_dict()
# create an instance of CreateFixedInvestmentRequest from a dict
create_fixed_investment_request_from_dict = CreateFixedInvestmentRequest.from_dict(create_fixed_investment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


