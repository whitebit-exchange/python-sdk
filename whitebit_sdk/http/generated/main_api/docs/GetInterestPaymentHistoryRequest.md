# GetInterestPaymentHistoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**plan_id** | **str** | [Invest plan](/glossary#crypto-lending) identifier | [optional] 
**ticker** | **str** | [Invest plan](/glossary#crypto-lending) target currency&#39;s [ticker](/glossary#ticker) | [optional] 
**limit** | **int** | LIMIT is a special clause used to limit records a particular query can return. | [optional] [default to 100]
**offset** | **int** | If you want the request to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start. | [optional] [default to 0]

## Example

```python
from main_api_generated.models.get_interest_payment_history_request import GetInterestPaymentHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetInterestPaymentHistoryRequest from a JSON string
get_interest_payment_history_request_instance = GetInterestPaymentHistoryRequest.from_json(json)
# print the JSON string representation of the object
print(GetInterestPaymentHistoryRequest.to_json())

# convert the object into a dict
get_interest_payment_history_request_dict = get_interest_payment_history_request_instance.to_dict()
# create an instance of GetInterestPaymentHistoryRequest from a dict
get_interest_payment_history_request_from_dict = GetInterestPaymentHistoryRequest.from_dict(get_interest_payment_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


