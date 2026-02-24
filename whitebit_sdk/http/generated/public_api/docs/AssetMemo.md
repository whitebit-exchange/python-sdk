# AssetMemo

Identifies if currency requires memo for deposits/withdraws

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit** | **bool** |  | [optional] 
**withdraw** | **bool** |  | [optional] 

## Example

```python
from public_api_generated.models.asset_memo import AssetMemo

# TODO update the JSON string below
json = "{}"
# create an instance of AssetMemo from a JSON string
asset_memo_instance = AssetMemo.from_json(json)
# print the JSON string representation of the object
print(AssetMemo.to_json())

# convert the object into a dict
asset_memo_dict = asset_memo_instance.to_dict()
# create an instance of AssetMemo from a dict
asset_memo_from_dict = AssetMemo.from_dict(asset_memo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


