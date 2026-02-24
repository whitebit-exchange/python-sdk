# GetMiningHashrate200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** |  | [optional] 
**hashrate** | [**List[GetMiningHashrate200ResponseDataHashrateInner]**](GetMiningHashrate200ResponseDataHashrateInner.md) |  | [optional] 

## Example

```python
from main_api_generated.models.get_mining_hashrate200_response_data import GetMiningHashrate200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningHashrate200ResponseData from a JSON string
get_mining_hashrate200_response_data_instance = GetMiningHashrate200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetMiningHashrate200ResponseData.to_json())

# convert the object into a dict
get_mining_hashrate200_response_data_dict = get_mining_hashrate200_response_data_instance.to_dict()
# create an instance of GetMiningHashrate200ResponseData from a dict
get_mining_hashrate200_response_data_from_dict = GetMiningHashrate200ResponseData.from_dict(get_mining_hashrate200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


