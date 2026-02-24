# ApiV4PublicFundingHistoryMarketGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**funding_time** | **str** | Timestamp when funding was executed | [optional] 
**funding_rate** | **str** | Funding rate value | [optional] 
**market** | **str** | Market name | [optional] 
**settlement_price** | **str** | Price at which funding was settled | [optional] 
**rate_calculated_time** | **str** | Timestamp when the funding rate was calculated | [optional] 

## Example

```python
from public_api_generated.models.api_v4_public_funding_history_market_get200_response_inner import ApiV4PublicFundingHistoryMarketGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV4PublicFundingHistoryMarketGet200ResponseInner from a JSON string
api_v4_public_funding_history_market_get200_response_inner_instance = ApiV4PublicFundingHistoryMarketGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiV4PublicFundingHistoryMarketGet200ResponseInner.to_json())

# convert the object into a dict
api_v4_public_funding_history_market_get200_response_inner_dict = api_v4_public_funding_history_market_get200_response_inner_instance.to_dict()
# create an instance of ApiV4PublicFundingHistoryMarketGet200ResponseInner from a dict
api_v4_public_funding_history_market_get200_response_inner_from_dict = ApiV4PublicFundingHistoryMarketGet200ResponseInner.from_dict(api_v4_public_funding_history_market_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


