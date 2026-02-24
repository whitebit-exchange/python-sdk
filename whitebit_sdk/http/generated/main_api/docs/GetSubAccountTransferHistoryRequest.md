# GetSubAccountTransferHistoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Sub-account id | 
**direction** | **str** | Transfer direction (optional) | [optional] 
**limit** | **int** |  | [optional] [default to 30]
**offset** | **int** |  | [optional] [default to 0]

## Example

```python
from main_api_generated.models.get_sub_account_transfer_history_request import GetSubAccountTransferHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountTransferHistoryRequest from a JSON string
get_sub_account_transfer_history_request_instance = GetSubAccountTransferHistoryRequest.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountTransferHistoryRequest.to_json())

# convert the object into a dict
get_sub_account_transfer_history_request_dict = get_sub_account_transfer_history_request_instance.to_dict()
# create an instance of GetSubAccountTransferHistoryRequest from a dict
get_sub_account_transfer_history_request_from_dict = GetSubAccountTransferHistoryRequest.from_dict(get_sub_account_transfer_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


