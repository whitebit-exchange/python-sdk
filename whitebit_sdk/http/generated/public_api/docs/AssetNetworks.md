# AssetNetworks

Currency networks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposits** | **List[str]** | Networks available for depositing | [optional] 
**withdraws** | **List[str]** | Networks available for withdrawing | [optional] 
**default** | **str** | Default network for depositing / withdrawing if available | [optional] 

## Example

```python
from public_api_generated.models.asset_networks import AssetNetworks

# TODO update the JSON string below
json = "{}"
# create an instance of AssetNetworks from a JSON string
asset_networks_instance = AssetNetworks.from_json(json)
# print the JSON string representation of the object
print(AssetNetworks.to_json())

# convert the object into a dict
asset_networks_dict = asset_networks_instance.to_dict()
# create an instance of AssetNetworks from a dict
asset_networks_from_dict = AssetNetworks.from_dict(asset_networks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


