# SubAccountTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Sub-account id | 
**direction** | **str** | Transfer direction | 
**amount** | **str** | Transfer amount (min 0.00000001) | 
**ticker** | **str** | Currency&#39;s [ticker](/glossary#ticker) | 

## Example

```python
from main_api_generated.models.sub_account_transfer_request import SubAccountTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountTransferRequest from a JSON string
sub_account_transfer_request_instance = SubAccountTransferRequest.from_json(json)
# print the JSON string representation of the object
print(SubAccountTransferRequest.to_json())

# convert the object into a dict
sub_account_transfer_request_dict = sub_account_transfer_request_instance.to_dict()
# create an instance of SubAccountTransferRequest from a dict
sub_account_transfer_request_from_dict = SubAccountTransferRequest.from_dict(sub_account_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


