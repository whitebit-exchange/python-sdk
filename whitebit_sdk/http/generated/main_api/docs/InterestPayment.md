# InterestPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** | Invest plan identifier | [optional] 
**investment_id** | **str** | Investment identifier | [optional] 
**amount** | **str** | Interest amount | [optional] 
**ticker** | **str** | Interest currency [ticker](/glossary#ticker) | [optional] 
**timestamp** | **int** | Transaction timestamp | [optional] 

## Example

```python
from main_api_generated.models.interest_payment import InterestPayment

# TODO update the JSON string below
json = "{}"
# create an instance of InterestPayment from a JSON string
interest_payment_instance = InterestPayment.from_json(json)
# print the JSON string representation of the object
print(InterestPayment.to_json())

# convert the object into a dict
interest_payment_dict = interest_payment_instance.to_dict()
# create an instance of InterestPayment from a dict
interest_payment_from_dict = InterestPayment.from_dict(interest_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


