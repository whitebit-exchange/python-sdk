# CreateSubAccountRequestPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spot_enabled** | **bool** | Enable transfers to trade balance | 
**collateral_enabled** | **bool** | Enable transfers to collateral balance | 

## Example

```python
from main_api_generated.models.create_sub_account_request_permissions import CreateSubAccountRequestPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubAccountRequestPermissions from a JSON string
create_sub_account_request_permissions_instance = CreateSubAccountRequestPermissions.from_json(json)
# print the JSON string representation of the object
print(CreateSubAccountRequestPermissions.to_json())

# convert the object into a dict
create_sub_account_request_permissions_dict = create_sub_account_request_permissions_instance.to_dict()
# create an instance of CreateSubAccountRequestPermissions from a dict
create_sub_account_request_permissions_from_dict = CreateSubAccountRequestPermissions.from_dict(create_sub_account_request_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


