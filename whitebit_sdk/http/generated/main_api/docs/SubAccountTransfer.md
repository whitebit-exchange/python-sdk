# SubAccountTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Transfer identifier | [optional] 
**direction** | **str** | Transfer direction (main_to_sub or sub_to_main) | [optional] 
**currency** | **str** | Currency transferred | [optional] 
**amount** | **str** | Transfer amount | [optional] 
**created_at** | **int** | Transfer creation timestamp | [optional] 

## Example

```python
from main_api_generated.models.sub_account_transfer import SubAccountTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountTransfer from a JSON string
sub_account_transfer_instance = SubAccountTransfer.from_json(json)
# print the JSON string representation of the object
print(SubAccountTransfer.to_json())

# convert the object into a dict
sub_account_transfer_dict = sub_account_transfer_instance.to_dict()
# create an instance of SubAccountTransfer from a dict
sub_account_transfer_from_dict = SubAccountTransfer.from_dict(sub_account_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


