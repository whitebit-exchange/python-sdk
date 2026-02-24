# MiningReward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mining_account_name** | **str** | Mining account name | [optional] 
**total_reward** | **str** | Total reward amount | [optional] 
**reward** | **str** | Reward amount (without fee) | [optional] 
**fee** | **str** | Fee amount | [optional] 
**fpps_rate** | **str** | FPPS rate | [optional] 
**hash_rate** | **str** | Hash rate | [optional] 
**var_date** | **int** | Reward date timestamp | [optional] 

## Example

```python
from main_api_generated.models.mining_reward import MiningReward

# TODO update the JSON string below
json = "{}"
# create an instance of MiningReward from a JSON string
mining_reward_instance = MiningReward.from_json(json)
# print the JSON string representation of the object
print(MiningReward.to_json())

# convert the object into a dict
mining_reward_dict = mining_reward_instance.to_dict()
# create an instance of MiningReward from a dict
mining_reward_from_dict = MiningReward.from_dict(mining_reward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


