# GetFlexPlansRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**limit** | **int** | Pagination limit. | [optional] [default to 100]
**offset** | **int** | Pagination offset. | [optional] [default to 0]
**ticker** | **str** | Filter by currency [ticker](/glossary#ticker). Example: USDT | [optional] 

## Example

```python
from main_api_generated.models.get_flex_plans_request import GetFlexPlansRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetFlexPlansRequest from a JSON string
get_flex_plans_request_instance = GetFlexPlansRequest.from_json(json)
# print the JSON string representation of the object
print(GetFlexPlansRequest.to_json())

# convert the object into a dict
get_flex_plans_request_dict = get_flex_plans_request_instance.to_dict()
# create an instance of GetFlexPlansRequest from a dict
get_flex_plans_request_from_dict = GetFlexPlansRequest.from_dict(get_flex_plans_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


