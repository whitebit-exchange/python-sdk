# GetDepositWithdrawHistory201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**records** | [**List[TransactionHistory]**](TransactionHistory.md) |  | [optional] 
**total** | **int** | Total number of transactions, use this for calculating &#39;limit&#39; and &#39;offset&#39; | [optional] 

## Example

```python
from main_api_generated.models.get_deposit_withdraw_history201_response import GetDepositWithdrawHistory201Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDepositWithdrawHistory201Response from a JSON string
get_deposit_withdraw_history201_response_instance = GetDepositWithdrawHistory201Response.from_json(json)
# print the JSON string representation of the object
print(GetDepositWithdrawHistory201Response.to_json())

# convert the object into a dict
get_deposit_withdraw_history201_response_dict = get_deposit_withdraw_history201_response_instance.to_dict()
# create an instance of GetDepositWithdrawHistory201Response from a dict
get_deposit_withdraw_history201_response_from_dict = GetDepositWithdrawHistory201Response.from_dict(get_deposit_withdraw_history201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


