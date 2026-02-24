# CreateWithdrawRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | Currency&#39;s [ticker](/glossary#ticker). Example: BTC  ⚠️ Currencies ticker must have \&quot;can_deposit\&quot; status equal to \&quot;true\&quot;. Use [Asset Status endpoint](/public/http-v4/asset-status-list) to know more about currency.  | 
**amount** | **str** | Withdraw amount (including [fee](/glossary#fee)). If you want fee to be added to the specified amount, you need to use /main-account/withdraw-pay request.  | 
**address** | **str** | Target address (wallet address for cryptocurrencies, identifier/[card token](/glossary#card-token) for [fiat](/glossary#fiat) currencies) | 
**unique_id** | **str** | Unique transaction identifier.  ⚠️ Note that you should generate new unique id for each withdrawal request.  | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**memo** | **str** | [Memo](/glossary#memodestination-tag).  ⚠️ Required if currency is memoable.  | [optional] 
**provider** | **str** | [Fiat](/glossary#fiat) currency [provider](/glossary#provider). Example: VISAMASTER  ⚠️ Required for fiat currencies. Currency provider should be taken from [Asset Status endpoint](/public/http-v4/asset-status-list) response.  | [optional] 
**network** | **str** | Cryptocurrency network. Available for multi network currencies. Example: OMNI  ⚠️ Currency network should be taken from [Asset Status endpoint](/public/http-v4/asset-status-list) response. Default for USDT is ERC20  | [optional] 
**partial_enable** | **bool** | Optional parameter for [FIAT](/glossary#fiat) withdrawals with increased Maximum Limit if set as \&quot;true\&quot;. In order to use this parameter your application should support \&quot;Partially successful\&quot; withdrawal status and latest updates in deposit/withdrawal history. | [optional] 
**beneficiary** | [**CreateWithdrawRequestBeneficiary**](CreateWithdrawRequestBeneficiary.md) |  | [optional] 
**travel_rule** | [**CreateWithdrawRequestTravelRule**](CreateWithdrawRequestTravelRule.md) |  | [optional] 
**payment_description** | **str** | Description of withdrawal destination  ⚠️ Required if currency is crypto and withdrawal from whitebit-tr.com  | [optional] 

## Example

```python
from main_api_generated.models.create_withdraw_request import CreateWithdrawRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWithdrawRequest from a JSON string
create_withdraw_request_instance = CreateWithdrawRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWithdrawRequest.to_json())

# convert the object into a dict
create_withdraw_request_dict = create_withdraw_request_instance.to_dict()
# create an instance of CreateWithdrawRequest from a dict
create_withdraw_request_from_dict = CreateWithdrawRequest.from_dict(create_withdraw_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


