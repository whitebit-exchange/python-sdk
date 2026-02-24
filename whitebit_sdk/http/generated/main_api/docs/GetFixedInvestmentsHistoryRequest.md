# GetFixedInvestmentsHistoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**id** | **str** | Investment identifier | [optional] 
**ticker** | **str** | [Invest plan](/glossary#crypto-lending) source currency&#39;s [ticker](/glossary#ticker) | [optional] 
**status** | **int** | Investment status (1 - active, 2 - closed) | [optional] 
**limit** | **int** | LIMIT is a special clause used to limit records a particular query can return. | [optional] [default to 100]
**offset** | **int** | If you want the request to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start. | [optional] [default to 0]

## Example

```python
from main_api_generated.models.get_fixed_investments_history_request import GetFixedInvestmentsHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedInvestmentsHistoryRequest from a JSON string
get_fixed_investments_history_request_instance = GetFixedInvestmentsHistoryRequest.from_json(json)
# print the JSON string representation of the object
print(GetFixedInvestmentsHistoryRequest.to_json())

# convert the object into a dict
get_fixed_investments_history_request_dict = get_fixed_investments_history_request_instance.to_dict()
# create an instance of GetFixedInvestmentsHistoryRequest from a dict
get_fixed_investments_history_request_from_dict = GetFixedInvestmentsHistoryRequest.from_dict(get_fixed_investments_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


