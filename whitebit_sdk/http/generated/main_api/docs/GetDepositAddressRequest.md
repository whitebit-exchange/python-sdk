# GetDepositAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | Currencies ticker. Example: BTC ⚠️ Currency [ticker](/glossary#ticker) should not be [fiat](/glossary#fiat) and it’s “can_deposit” status must be “true”. You can find this status in [Asset Status endpoint](/public/http-v4/asset-status-list) response.  | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**network** | **str** | Cryptocurrency network. ⚠️ If currency has multiple networks like USDT - you need to specify network to be used. You can find [ticker](/glossary#ticker) networks list in “networks” field from response [Asset Status endpoint](/public/http-v4/asset-status-list).  | [optional] 

## Example

```python
from main_api_generated.models.get_deposit_address_request import GetDepositAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDepositAddressRequest from a JSON string
get_deposit_address_request_instance = GetDepositAddressRequest.from_json(json)
# print the JSON string representation of the object
print(GetDepositAddressRequest.to_json())

# convert the object into a dict
get_deposit_address_request_dict = get_deposit_address_request_instance.to_dict()
# create an instance of GetDepositAddressRequest from a dict
get_deposit_address_request_from_dict = GetDepositAddressRequest.from_dict(get_deposit_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


