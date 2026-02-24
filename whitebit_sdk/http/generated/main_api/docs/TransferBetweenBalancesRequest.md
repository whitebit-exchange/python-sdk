# TransferBetweenBalancesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | Currency&#39;s [ticker](/glossary#ticker). Example: BTC | 
**amount** | **str** | Amount to transfer. Max [precision](/glossary#precision) &#x3D; 8, value should be greater than zero and less or equal your available balance. | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**method** | **str** | Transfer method.  ⚠️ We highly recommend to use **from** and **to** fields, which provides more flexibility. This way will be deprecated in future.  Example: **deposit** if you need to transfer from [main](/glossary#balance-main) to [trade](/glossary#balance-spotbalance-trade) / **withdraw** if you need to transfer from [trade](/glossary#balance-spotbalance-trade) balance to [main](/glossary#balance-main). For [collateral balances](/glossary#balance-collateral) you can use **collateral-deposit** to transfer from main to collateral balance and **collateral-withdraw** to transfer from collateral balance to main  **Not required** if **from** and **to** are set.  | [optional] 
**var_from** | **str** | Balance FROM which funds will move to. Acceptable values: [**main**](/glossary#balance-main), [**spot**](/glossary#balance-spotbalance-trade), [**collateral**](/glossary#balance-collateral)  **Not required** if **method** is set.  | [optional] 
**to** | **str** | Balance TO which funds will move to. Acceptable values: [**main**](/glossary#balance-main), [**spot**](/glossary#balance-spotbalance-trade), [**collateral**](/glossary#balance-collateral)  **Not required** if **method** is set.  | [optional] 

## Example

```python
from main_api_generated.models.transfer_between_balances_request import TransferBetweenBalancesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferBetweenBalancesRequest from a JSON string
transfer_between_balances_request_instance = TransferBetweenBalancesRequest.from_json(json)
# print the JSON string representation of the object
print(TransferBetweenBalancesRequest.to_json())

# convert the object into a dict
transfer_between_balances_request_dict = transfer_between_balances_request_instance.to_dict()
# create an instance of TransferBetweenBalancesRequest from a dict
transfer_between_balances_request_from_dict = TransferBetweenBalancesRequest.from_dict(transfer_between_balances_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


