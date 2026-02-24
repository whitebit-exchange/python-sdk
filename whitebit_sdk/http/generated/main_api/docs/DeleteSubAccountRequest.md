# DeleteSubAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Sub-account id | 

## Example

```python
from main_api_generated.models.delete_sub_account_request import DeleteSubAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSubAccountRequest from a JSON string
delete_sub_account_request_instance = DeleteSubAccountRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteSubAccountRequest.to_json())

# convert the object into a dict
delete_sub_account_request_dict = delete_sub_account_request_instance.to_dict()
# create an instance of DeleteSubAccountRequest from a dict
delete_sub_account_request_from_dict = DeleteSubAccountRequest.from_dict(delete_sub_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


