# ResetSubAccountApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** | ID of the API key to reset | 

## Example

```python
from main_api_generated.models.reset_sub_account_api_key_request import ResetSubAccountApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResetSubAccountApiKeyRequest from a JSON string
reset_sub_account_api_key_request_instance = ResetSubAccountApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(ResetSubAccountApiKeyRequest.to_json())

# convert the object into a dict
reset_sub_account_api_key_request_dict = reset_sub_account_api_key_request_instance.to_dict()
# create an instance of ResetSubAccountApiKeyRequest from a dict
reset_sub_account_api_key_request_from_dict = ResetSubAccountApiKeyRequest.from_dict(reset_sub_account_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


