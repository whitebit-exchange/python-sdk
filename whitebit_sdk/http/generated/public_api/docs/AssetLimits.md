# AssetLimits

Currency limits by each network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit** | [**Dict[str, AssetLimitsDepositValue]**](AssetLimitsDepositValue.md) | Deposits limits | [optional] 
**withdraw** | [**Dict[str, AssetLimitsWithdrawValue]**](AssetLimitsWithdrawValue.md) | Withdraws limits | [optional] 

## Example

```python
from public_api_generated.models.asset_limits import AssetLimits

# TODO update the JSON string below
json = "{}"
# create an instance of AssetLimits from a JSON string
asset_limits_instance = AssetLimits.from_json(json)
# print the JSON string representation of the object
print(AssetLimits.to_json())

# convert the object into a dict
asset_limits_dict = asset_limits_instance.to_dict()
# create an instance of AssetLimits from a dict
asset_limits_from_dict = AssetLimits.from_dict(asset_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


