# GetUserFlexInvestmentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**limit** | **int** | Pagination limit. Default: 100. | [optional] [default to 100]
**offset** | **int** | Pagination offset. Default: 0. | [optional] [default to 0]
**ticker** | **str** | Filter by currency [ticker](/glossary#ticker). Example: USDT. | [optional] 
**plan** | **str** | Filter by plan ID (UUID). | [optional] 
**investment** | **str** | Filter by investment ID. | [optional] 
**investment_status** | **int** | Filter by status (1&#x3D;ACTIVE, 0&#x3D;CLOSED). | [optional] 

## Example

```python
from main_api_generated.models.get_user_flex_investments_request import GetUserFlexInvestmentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserFlexInvestmentsRequest from a JSON string
get_user_flex_investments_request_instance = GetUserFlexInvestmentsRequest.from_json(json)
# print the JSON string representation of the object
print(GetUserFlexInvestmentsRequest.to_json())

# convert the object into a dict
get_user_flex_investments_request_dict = get_user_flex_investments_request_instance.to_dict()
# create an instance of GetUserFlexInvestmentsRequest from a dict
get_user_flex_investments_request_from_dict = GetUserFlexInvestmentsRequest.from_dict(get_user_flex_investments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


