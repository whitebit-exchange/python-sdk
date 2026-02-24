# ApiV4PublicMiningPoolGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_links** | **List[str]** |  | [optional] 
**location** | **str** |  | [optional] 
**assets** | **List[str]** |  | [optional] 
**reward_schemes** | **List[str]** |  | [optional] 
**workers** | **int** |  | [optional] 
**current_hash_rate** | **str** |  | [optional] 
**last7days_hash_rate** | [**List[ApiV4PublicMiningPoolGet200ResponseDataInnerLast7daysHashRateInner]**](ApiV4PublicMiningPoolGet200ResponseDataInnerLast7daysHashRateInner.md) |  | [optional] 
**blocks** | [**List[ApiV4PublicMiningPoolGet200ResponseDataInnerBlocksInner]**](ApiV4PublicMiningPoolGet200ResponseDataInnerBlocksInner.md) |  | [optional] 

## Example

```python
from public_api_generated.models.api_v4_public_mining_pool_get200_response_data_inner import ApiV4PublicMiningPoolGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV4PublicMiningPoolGet200ResponseDataInner from a JSON string
api_v4_public_mining_pool_get200_response_data_inner_instance = ApiV4PublicMiningPoolGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ApiV4PublicMiningPoolGet200ResponseDataInner.to_json())

# convert the object into a dict
api_v4_public_mining_pool_get200_response_data_inner_dict = api_v4_public_mining_pool_get200_response_data_inner_instance.to_dict()
# create an instance of ApiV4PublicMiningPoolGet200ResponseDataInner from a dict
api_v4_public_mining_pool_get200_response_data_inner_from_dict = ApiV4PublicMiningPoolGet200ResponseDataInner.from_dict(api_v4_public_mining_pool_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


