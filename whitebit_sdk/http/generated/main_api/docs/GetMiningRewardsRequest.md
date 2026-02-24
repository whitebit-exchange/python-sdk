# GetMiningRewardsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Mining pool account | [optional] 
**var_from** | **int** | Date timestamp starting from which rewards are received | [optional] 
**to** | **int** | Date timestamp until which rewards are received | [optional] 
**limit** | **int** |  | [optional] [default to 30]
**offset** | **int** |  | [optional] [default to 0]

## Example

```python
from main_api_generated.models.get_mining_rewards_request import GetMiningRewardsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningRewardsRequest from a JSON string
get_mining_rewards_request_instance = GetMiningRewardsRequest.from_json(json)
# print the JSON string representation of the object
print(GetMiningRewardsRequest.to_json())

# convert the object into a dict
get_mining_rewards_request_dict = get_mining_rewards_request_instance.to_dict()
# create an instance of GetMiningRewardsRequest from a dict
get_mining_rewards_request_from_dict = GetMiningRewardsRequest.from_dict(get_mining_rewards_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


