# SubAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Sub-account identifier | [optional] 
**alias** | **str** | Sub-account alias/name | [optional] 
**user_id** | **str** | User identifier associated with account | [optional] 
**email** | **str** | Sub-account email (masked) | [optional] 
**status** | **str** | Sub-account status | [optional] 
**color** | **str** | Sub-account color | [optional] 
**kyc** | [**SubAccountKyc**](SubAccountKyc.md) |  | [optional] 
**permissions** | [**SubAccountPermissions**](SubAccountPermissions.md) |  | [optional] 

## Example

```python
from main_api_generated.models.sub_account import SubAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccount from a JSON string
sub_account_instance = SubAccount.from_json(json)
# print the JSON string representation of the object
print(SubAccount.to_json())

# convert the object into a dict
sub_account_dict = sub_account_instance.to_dict()
# create an instance of SubAccount from a dict
sub_account_from_dict = SubAccount.from_dict(sub_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


