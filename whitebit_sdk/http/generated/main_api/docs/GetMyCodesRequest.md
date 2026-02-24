# GetMyCodesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**limit** | **int** | LIMIT is a special clause used to limit records a particular query can return. | [optional] [default to 30]
**offset** | **int** | If you want the request to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start. | [optional] [default to 0]

## Example

```python
from main_api_generated.models.get_my_codes_request import GetMyCodesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyCodesRequest from a JSON string
get_my_codes_request_instance = GetMyCodesRequest.from_json(json)
# print the JSON string representation of the object
print(GetMyCodesRequest.to_json())

# convert the object into a dict
get_my_codes_request_dict = get_my_codes_request_instance.to_dict()
# create an instance of GetMyCodesRequest from a dict
get_my_codes_request_from_dict = GetMyCodesRequest.from_dict(get_my_codes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


