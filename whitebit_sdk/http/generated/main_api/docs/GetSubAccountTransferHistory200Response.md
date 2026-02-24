# GetSubAccountTransferHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**data** | [**List[SubAccountTransfer]**](SubAccountTransfer.md) |  | [optional] 

## Example

```python
from main_api_generated.models.get_sub_account_transfer_history200_response import GetSubAccountTransferHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountTransferHistory200Response from a JSON string
get_sub_account_transfer_history200_response_instance = GetSubAccountTransferHistory200Response.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountTransferHistory200Response.to_json())

# convert the object into a dict
get_sub_account_transfer_history200_response_dict = get_sub_account_transfer_history200_response_instance.to_dict()
# create an instance of GetSubAccountTransferHistory200Response from a dict
get_sub_account_transfer_history200_response_from_dict = GetSubAccountTransferHistory200Response.from_dict(get_sub_account_transfer_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


