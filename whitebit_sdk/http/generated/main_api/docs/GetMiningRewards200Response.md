# GetMiningRewards200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**data** | [**List[MiningReward]**](MiningReward.md) |  | [optional] 

## Example

```python
from main_api_generated.models.get_mining_rewards200_response import GetMiningRewards200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningRewards200Response from a JSON string
get_mining_rewards200_response_instance = GetMiningRewards200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiningRewards200Response.to_json())

# convert the object into a dict
get_mining_rewards200_response_dict = get_mining_rewards200_response_instance.to_dict()
# create an instance of GetMiningRewards200Response from a dict
get_mining_rewards200_response_from_dict = GetMiningRewards200Response.from_dict(get_mining_rewards200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


