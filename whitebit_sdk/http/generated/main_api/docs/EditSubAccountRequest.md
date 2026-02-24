# EditSubAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Sub-account id | 
**alias** | **str** | Name for sub-account | 
**permissions** | [**CreateSubAccountRequestPermissions**](CreateSubAccountRequestPermissions.md) |  | 

## Example

```python
from main_api_generated.models.edit_sub_account_request import EditSubAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditSubAccountRequest from a JSON string
edit_sub_account_request_instance = EditSubAccountRequest.from_json(json)
# print the JSON string representation of the object
print(EditSubAccountRequest.to_json())

# convert the object into a dict
edit_sub_account_request_dict = edit_sub_account_request_instance.to_dict()
# create an instance of EditSubAccountRequest from a dict
edit_sub_account_request_from_dict = EditSubAccountRequest.from_dict(edit_sub_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


