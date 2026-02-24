# GetDepositWithdrawHistoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**transaction_method** | **int** | Method. Example: **1** to display deposits / **2** to display withdraws. Do not send this parameter in order to receive both deposits and withdraws.  | [optional] 
**ticker** | **str** | Currency&#39;s [ticker](/glossary#ticker). Example: BTC | [optional] 
**address** | **str** | Can be used for filtering transactions by specific address. | [optional] 
**memo** | **str** | Can be used for filtering transactions by specific [memo](/glossary#memodestination-tag) | [optional] 
**addresses** | **List[str]** | Can be used for filtering transactions by specific array of addresses. | [optional] 
**unique_id** | **str** | Can be used for filtering transactions by specific unique id | [optional] 
**limit** | **int** | LIMIT is a special clause used to limit records a particular query can return. | [optional] [default to 50]
**offset** | **int** | If you want the request to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start. | [optional] [default to 0]
**status** | **List[int]** | Can be used for filtering transactions by status codes.  ⚠️ Caution: You must use this parameter with appropriate &#x60;transactionMethod&#x60; and use valid status codes for this method. You can find them in the endpoint description above. Example: &#x60;\&quot;status\&quot;: [3,7]&#x60;  | [optional] 

## Example

```python
from main_api_generated.models.get_deposit_withdraw_history_request import GetDepositWithdrawHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDepositWithdrawHistoryRequest from a JSON string
get_deposit_withdraw_history_request_instance = GetDepositWithdrawHistoryRequest.from_json(json)
# print the JSON string representation of the object
print(GetDepositWithdrawHistoryRequest.to_json())

# convert the object into a dict
get_deposit_withdraw_history_request_dict = get_deposit_withdraw_history_request_instance.to_dict()
# create an instance of GetDepositWithdrawHistoryRequest from a dict
get_deposit_withdraw_history_request_from_dict = GetDepositWithdrawHistoryRequest.from_dict(get_deposit_withdraw_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


