# ApiV4PublicTradesMarketGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_id** | **int** | A unique ID associated with the trade for the currency pair transaction Note: Unix timestamp does not qualify as trade_id. | [optional] 
**price** | **str** | Transaction price in quote pair volume. | [optional] 
**quote_volume** | **str** | Transaction amount in quote pair volume. | [optional] 
**base_volume** | **str** | Transaction amount in base pair volume. | [optional] 
**trade_timestamp** | **int** | Unix timestamp in milliseconds, identifies when the transaction occurred. | [optional] 
**type** | **str** | Used to determine whether or not the transaction originated as a buy or sell. Buy – Identifies an ask that was removed from the order book. Sell – Identifies a bid that was removed from the order book. | [optional] 
**rpi** | **bool** | Indicates whether the trade involved a Retail Price Improvement (RPI) order | [optional] 

## Example

```python
from public_api_generated.models.api_v4_public_trades_market_get200_response_inner import ApiV4PublicTradesMarketGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV4PublicTradesMarketGet200ResponseInner from a JSON string
api_v4_public_trades_market_get200_response_inner_instance = ApiV4PublicTradesMarketGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiV4PublicTradesMarketGet200ResponseInner.to_json())

# convert the object into a dict
api_v4_public_trades_market_get200_response_inner_dict = api_v4_public_trades_market_get200_response_inner_instance.to_dict()
# create an instance of ApiV4PublicTradesMarketGet200ResponseInner from a dict
api_v4_public_trades_market_get200_response_inner_from_dict = ApiV4PublicTradesMarketGet200ResponseInner.from_dict(api_v4_public_trades_market_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


