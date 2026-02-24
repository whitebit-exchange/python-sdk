# WithdrawRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | Currencies [ticker](/glossary#ticker). Example: BTC ⚠️ Currencies ticker must have \&quot;can_deposit\&quot; status equal to \&quot;true\&quot;. Use [Asset Status endpoint](/public/http-v4/asset-status-list) to know more about currency. | 
**amount** | **str** | Withdraw amount (including [fee](/glossary#fee)). If you want fee to be added to the specified amount, you need to use /main-account/withdraw-pay request | 
**address** | **str** | Target address (wallet address for cryptocurrencies, identifier/[card token](/glossary#card-token) for [fiat](/glossary#fiat) currencies) | 
**unique_id** | **str** | Unique transaction identifier. ⚠️ Note that you should generate new unique id for each withdrawal request. | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**memo** | **str** | Required if currency is memoable. See [memo](/glossary#memodestination-tag) for details. | [optional] 
**provider** | **str** | [Fiat](/glossary#fiat) currency [provider](/glossary#provider). Example: VISAMASTER ⚠️ Currency provider should be taken from [Asset Status endpoint](/public/http-v4/asset-status-list) response. Required if currency is fiat. | [optional] 
**network** | **str** | Cryptocurrency network. Available for [multinetwork](/glossary#multinetwork) currencies. Example: OMNI ⚠️ Currency network should be taken from [Asset Status endpoint](/public/http-v4/asset-status-list) response. Default for USDT is ERC20 | [optional] 
**partial_enable** | **bool** | Optional parameter for [FIAT](/glossary#fiat) withdrawals with increased Maximum Limit if set as \&quot;true\&quot;. In order to use this parameter your application should support \&quot;Partially successful\&quot; withdrawal status and latest updates in deposit/withdrawal history. | [optional] 
**beneficiary** | **object** | Beneficiary information data. Required if currency [ticker](/glossary#ticker) is one of: UAH_IBAN, USD_VISAMASTER, EUR_VISAMASTER, USD, EUR | [optional] 
**travel_rule** | **object** | Travel Rule information data. Required if currency is crypto and you are from [EEA](/glossary#eea) | [optional] 

## Example

```python
from main_api_generated.models.withdraw_request import WithdrawRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawRequest from a JSON string
withdraw_request_instance = WithdrawRequest.from_json(json)
# print the JSON string representation of the object
print(WithdrawRequest.to_json())

# convert the object into a dict
withdraw_request_dict = withdraw_request_instance.to_dict()
# create an instance of WithdrawRequest from a dict
withdraw_request_from_dict = WithdrawRequest.from_dict(withdraw_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


