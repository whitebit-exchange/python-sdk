# GetFixedPlansRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**ticker** | **str** | [Invest plan](/glossary#crypto-lending) source currency&#39;s [ticker](/glossary#ticker). Example: BTC | [optional] 

## Example

```python
from main_api_generated.models.get_fixed_plans_request import GetFixedPlansRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedPlansRequest from a JSON string
get_fixed_plans_request_instance = GetFixedPlansRequest.from_json(json)
# print the JSON string representation of the object
print(GetFixedPlansRequest.to_json())

# convert the object into a dict
get_fixed_plans_request_dict = get_fixed_plans_request_instance.to_dict()
# create an instance of GetFixedPlansRequest from a dict
get_fixed_plans_request_from_dict = GetFixedPlansRequest.from_dict(get_fixed_plans_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


