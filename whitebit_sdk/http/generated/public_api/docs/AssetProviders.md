# AssetProviders

Fiat currency providers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposits** | **List[str]** |  | [optional] 
**withdraws** | **List[str]** |  | [optional] 

## Example

```python
from public_api_generated.models.asset_providers import AssetProviders

# TODO update the JSON string below
json = "{}"
# create an instance of AssetProviders from a JSON string
asset_providers_instance = AssetProviders.from_json(json)
# print the JSON string representation of the object
print(AssetProviders.to_json())

# convert the object into a dict
asset_providers_dict = asset_providers_instance.to_dict()
# create an instance of AssetProviders from a dict
asset_providers_from_dict = AssetProviders.from_dict(asset_providers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


