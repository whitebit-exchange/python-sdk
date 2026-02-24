# SubAccountApiKeyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_account_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**api_key** | **str** |  | [optional] 
**api_secret** | **str** | Empty for security (only shown during creation) | [optional] 
**type** | **str** |  | [optional] 
**last_activity** | **int** |  | [optional] 
**restrict_access** | **bool** |  | [optional] 
**access_endpoints** | [**List[SubAccountApiKeyListAccessEndpointsInner]**](SubAccountApiKeyListAccessEndpointsInner.md) |  | [optional] 

## Example

```python
from main_api_generated.models.sub_account_api_key_list import SubAccountApiKeyList

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountApiKeyList from a JSON string
sub_account_api_key_list_instance = SubAccountApiKeyList.from_json(json)
# print the JSON string representation of the object
print(SubAccountApiKeyList.to_json())

# convert the object into a dict
sub_account_api_key_list_dict = sub_account_api_key_list_instance.to_dict()
# create an instance of SubAccountApiKeyList from a dict
sub_account_api_key_list_from_dict = SubAccountApiKeyList.from_dict(sub_account_api_key_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


