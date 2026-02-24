# ListSubAccountApiKeysRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_account_id** | **str** | ID of the sub-account to list API keys for | [optional] 
**limit** | **int** |  | [optional] [default to 30]
**offset** | **int** |  | [optional] [default to 0]

## Example

```python
from main_api_generated.models.list_sub_account_api_keys_request import ListSubAccountApiKeysRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListSubAccountApiKeysRequest from a JSON string
list_sub_account_api_keys_request_instance = ListSubAccountApiKeysRequest.from_json(json)
# print the JSON string representation of the object
print(ListSubAccountApiKeysRequest.to_json())

# convert the object into a dict
list_sub_account_api_keys_request_dict = list_sub_account_api_keys_request_instance.to_dict()
# create an instance of ListSubAccountApiKeysRequest from a dict
list_sub_account_api_keys_request_from_dict = ListSubAccountApiKeysRequest.from_dict(list_sub_account_api_keys_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


