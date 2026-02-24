# SubAccountPermissions

Sub-account permissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spot_enabled** | **bool** | Spot trading enabled | [optional] 
**collateral_enabled** | **bool** | Collateral trading enabled | [optional] 

## Example

```python
from main_api_generated.models.sub_account_permissions import SubAccountPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountPermissions from a JSON string
sub_account_permissions_instance = SubAccountPermissions.from_json(json)
# print the JSON string representation of the object
print(SubAccountPermissions.to_json())

# convert the object into a dict
sub_account_permissions_dict = sub_account_permissions_instance.to_dict()
# create an instance of SubAccountPermissions from a dict
sub_account_permissions_from_dict = SubAccountPermissions.from_dict(sub_account_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


