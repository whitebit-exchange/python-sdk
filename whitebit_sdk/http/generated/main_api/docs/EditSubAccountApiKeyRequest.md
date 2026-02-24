# EditSubAccountApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** | ID of the API key to update | 
**title** | **str** | New title for the API key | 
**urls** | [**List[EditSubAccountApiKeyRequestUrlsInner]**](EditSubAccountApiKeyRequestUrlsInner.md) | Array of URL objects for API key restrictions | 

## Example

```python
from main_api_generated.models.edit_sub_account_api_key_request import EditSubAccountApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditSubAccountApiKeyRequest from a JSON string
edit_sub_account_api_key_request_instance = EditSubAccountApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(EditSubAccountApiKeyRequest.to_json())

# convert the object into a dict
edit_sub_account_api_key_request_dict = edit_sub_account_api_key_request_instance.to_dict()
# create an instance of EditSubAccountApiKeyRequest from a dict
edit_sub_account_api_key_request_from_dict = EditSubAccountApiKeyRequest.from_dict(edit_sub_account_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


