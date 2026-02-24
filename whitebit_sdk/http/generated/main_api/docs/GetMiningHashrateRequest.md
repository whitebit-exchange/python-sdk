# GetMiningHashrateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Mining pool account | 
**var_from** | **int** | Unix timestamp of starting point | [optional] 
**to** | **int** | Unix timestamp of final point | [optional] 
**interval** | **str** | Timestamp interval | [optional] [default to '1h']

## Example

```python
from main_api_generated.models.get_mining_hashrate_request import GetMiningHashrateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningHashrateRequest from a JSON string
get_mining_hashrate_request_instance = GetMiningHashrateRequest.from_json(json)
# print the JSON string representation of the object
print(GetMiningHashrateRequest.to_json())

# convert the object into a dict
get_mining_hashrate_request_dict = get_mining_hashrate_request_instance.to_dict()
# create an instance of GetMiningHashrateRequest from a dict
get_mining_hashrate_request_from_dict = GetMiningHashrateRequest.from_dict(get_mining_hashrate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


