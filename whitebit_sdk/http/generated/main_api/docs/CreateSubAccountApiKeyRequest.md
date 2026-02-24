# CreateSubAccountApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | Type of API key (1 - info and trading; 2 - info, trading, deposits, withdraws) | 
**sub_account_id** | **str** | ID of the sub-account to create the API key for | 
**title** | **str** | Custom title/name for the API key | [optional] 

## Example

```python
from main_api_generated.models.create_sub_account_api_key_request import CreateSubAccountApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubAccountApiKeyRequest from a JSON string
create_sub_account_api_key_request_instance = CreateSubAccountApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSubAccountApiKeyRequest.to_json())

# convert the object into a dict
create_sub_account_api_key_request_dict = create_sub_account_api_key_request_instance.to_dict()
# create an instance of CreateSubAccountApiKeyRequest from a dict
create_sub_account_api_key_request_from_dict = CreateSubAccountApiKeyRequest.from_dict(create_sub_account_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


