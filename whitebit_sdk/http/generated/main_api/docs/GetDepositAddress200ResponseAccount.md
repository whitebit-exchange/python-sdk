# GetDepositAddress200ResponseAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Deposit address | [optional] 
**memo** | **str** | Memo if currency requires memo | [optional] 

## Example

```python
from main_api_generated.models.get_deposit_address200_response_account import GetDepositAddress200ResponseAccount

# TODO update the JSON string below
json = "{}"
# create an instance of GetDepositAddress200ResponseAccount from a JSON string
get_deposit_address200_response_account_instance = GetDepositAddress200ResponseAccount.from_json(json)
# print the JSON string representation of the object
print(GetDepositAddress200ResponseAccount.to_json())

# convert the object into a dict
get_deposit_address200_response_account_dict = get_deposit_address200_response_account_instance.to_dict()
# create an instance of GetDepositAddress200ResponseAccount from a dict
get_deposit_address200_response_account_from_dict = GetDepositAddress200ResponseAccount.from_dict(get_deposit_address200_response_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


