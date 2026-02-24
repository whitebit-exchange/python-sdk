# TransactionHistoryConfirmations

Confirmation details for crypto transactions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual** | **int** | Actual number of confirmations | [optional] 
**required** | **int** | Required number of confirmations | [optional] 

## Example

```python
from main_api_generated.models.transaction_history_confirmations import TransactionHistoryConfirmations

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionHistoryConfirmations from a JSON string
transaction_history_confirmations_instance = TransactionHistoryConfirmations.from_json(json)
# print the JSON string representation of the object
print(TransactionHistoryConfirmations.to_json())

# convert the object into a dict
transaction_history_confirmations_dict = transaction_history_confirmations_instance.to_dict()
# create an instance of TransactionHistoryConfirmations from a dict
transaction_history_confirmations_from_dict = TransactionHistoryConfirmations.from_dict(transaction_history_confirmations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


