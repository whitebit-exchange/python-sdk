# TransactionHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Deposit/Withdraw address | [optional] 
**unique_id** | **str** | Unique Id of deposit/withdraw | [optional] 
**created_at** | **int** | Timestamp of deposit/withdraw | [optional] 
**currency** | **str** | Deposit/Withdraw currency full name | [optional] 
**ticker** | **str** | Deposit/Withdraw currency [ticker](/glossary#ticker) | [optional] 
**method** | **int** | Called method: 1 - deposit, 2 - withdraw | [optional] 
**amount** | **str** | Amount of deposit/withdraw | [optional] 
**description** | **str** | Deposit/Withdraw description | [optional] 
**memo** | **str** | [Memo](/glossary#memodestination-tag) for deposit/withdraw | [optional] 
**fee** | **str** | [Fee](/glossary#fee) for deposit/withdraw | [optional] 
**status** | **int** | Transaction status (see endpoint description for status codes) | [optional] 
**network** | **str** | Network if currency is multinetwork | [optional] 
**transaction_hash** | **str** | Deposit/Withdraw transaction hash | [optional] 
**transaction_id** | **str** | Transaction ID | [optional] 
**details** | **object** | Additional details for the transaction | [optional] 
**confirmations** | [**TransactionHistoryConfirmations**](TransactionHistoryConfirmations.md) |  | [optional] 

## Example

```python
from main_api_generated.models.transaction_history import TransactionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionHistory from a JSON string
transaction_history_instance = TransactionHistory.from_json(json)
# print the JSON string representation of the object
print(TransactionHistory.to_json())

# convert the object into a dict
transaction_history_dict = transaction_history_instance.to_dict()
# create an instance of TransactionHistory from a dict
transaction_history_from_dict = TransactionHistory.from_dict(transaction_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


