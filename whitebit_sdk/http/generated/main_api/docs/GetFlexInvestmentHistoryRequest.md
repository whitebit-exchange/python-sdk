# GetFlexInvestmentHistoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**limit** | **int** | Pagination limit. | [optional] [default to 50]
**offset** | **int** | Pagination offset. | [optional] [default to 0]
**plan** | **str** | Filter by plan ID (UUID). | [optional] 
**investment** | **str** | Filter by investment ID. | [optional] 
**transaction** | **str** | Filter by transaction ID. | [optional] 
**date_from** | **int** | Filter from date (timestamp). | [optional] 
**date_to** | **int** | Filter to date (timestamp). | [optional] 
**action_types** | **List[int]** | Array of operation type IDs. See table below. | [optional] 

## Example

```python
from main_api_generated.models.get_flex_investment_history_request import GetFlexInvestmentHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetFlexInvestmentHistoryRequest from a JSON string
get_flex_investment_history_request_instance = GetFlexInvestmentHistoryRequest.from_json(json)
# print the JSON string representation of the object
print(GetFlexInvestmentHistoryRequest.to_json())

# convert the object into a dict
get_flex_investment_history_request_dict = get_flex_investment_history_request_instance.to_dict()
# create an instance of GetFlexInvestmentHistoryRequest from a dict
get_flex_investment_history_request_from_dict = GetFlexInvestmentHistoryRequest.from_dict(get_flex_investment_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


