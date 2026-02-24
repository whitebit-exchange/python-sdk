# SubAccountApiKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_account_id** | **str** | Sub-account identifier | [optional] 
**id** | **str** | API key identifier | [optional] 
**title** | **str** | API key title/name | [optional] 
**is_enabled** | **bool** | Whether the API key is enabled | [optional] 
**api_key** | **str** | API key | [optional] 
**api_secret** | **str** | API secret | [optional] 
**type** | **int** | API key type (1 - info and trading, 2 - info, trading, deposit and withdraw) | [optional] 
**last_activity** | **int** | Last activity timestamp | [optional] 
**restrict_access** | **bool** | Whether access is restricted | [optional] 
**access_endpoints** | [**List[SubAccountApiKeyAccessEndpointsInner]**](SubAccountApiKeyAccessEndpointsInner.md) | List of allowed endpoints | [optional] 

## Example

```python
from main_api_generated.models.sub_account_api_key import SubAccountApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountApiKey from a JSON string
sub_account_api_key_instance = SubAccountApiKey.from_json(json)
# print the JSON string representation of the object
print(SubAccountApiKey.to_json())

# convert the object into a dict
sub_account_api_key_dict = sub_account_api_key_instance.to_dict()
# create an instance of SubAccountApiKey from a dict
sub_account_api_key_from_dict = SubAccountApiKey.from_dict(sub_account_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


