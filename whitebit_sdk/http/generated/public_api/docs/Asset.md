# Asset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Full name of cryptocurrency | [optional] 
**unified_cryptoasset_id** | **int** | Unique ID of cryptocurrency assigned by Unified Cryptoasset ID, 0 if unknown | [optional] 
**can_withdraw** | **bool** | Identifies whether withdrawals are enabled or disabled | [optional] 
**can_deposit** | **bool** | Identifies whether deposits are enabled or disabled | [optional] 
**min_withdraw** | **str** | Identifies the single minimum withdrawal amount of a cryptocurrency | [optional] 
**max_withdraw** | **str** | Identifies the single maximum withdrawal amount of a cryptocurrency | [optional] 
**maker_fee** | **str** | Maker fee in percentage | [optional] 
**taker_fee** | **str** | Taker fee in percentage | [optional] 
**min_deposit** | **str** | Min deposit amount | [optional] 
**max_deposit** | **str** | Max deposit amount, will not be returned if there is no limit, 0 if unlimited | [optional] 
**currency_precision** | **int** | Max number of digits to the right of the decimal point | [optional] 
**is_memo** | **bool** | Identifies if currency has memo address | [optional] 
**memo** | [**AssetMemo**](AssetMemo.md) |  | [optional] 
**networks** | [**AssetNetworks**](AssetNetworks.md) |  | [optional] 
**limits** | [**AssetLimits**](AssetLimits.md) |  | [optional] 
**confirmations** | **Dict[str, int]** | Deposit confirmations count mapped by network | [optional] 
**providers** | [**AssetProviders**](AssetProviders.md) |  | [optional] 

## Example

```python
from public_api_generated.models.asset import Asset

# TODO update the JSON string below
json = "{}"
# create an instance of Asset from a JSON string
asset_instance = Asset.from_json(json)
# print the JSON string representation of the object
print(Asset.to_json())

# convert the object into a dict
asset_dict = asset_instance.to_dict()
# create an instance of Asset from a dict
asset_from_dict = Asset.from_dict(asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


