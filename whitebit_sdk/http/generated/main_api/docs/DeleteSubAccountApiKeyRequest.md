# DeleteSubAccountApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** | ID of the API key to delete | 

## Example

```python
from main_api_generated.models.delete_sub_account_api_key_request import DeleteSubAccountApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSubAccountApiKeyRequest from a JSON string
delete_sub_account_api_key_request_instance = DeleteSubAccountApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteSubAccountApiKeyRequest.to_json())

# convert the object into a dict
delete_sub_account_api_key_request_dict = delete_sub_account_api_key_request_instance.to_dict()
# create an instance of DeleteSubAccountApiKeyRequest from a dict
delete_sub_account_api_key_request_from_dict = DeleteSubAccountApiKeyRequest.from_dict(delete_sub_account_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


