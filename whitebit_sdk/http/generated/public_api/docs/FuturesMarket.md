# FuturesMarket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker_id** | **str** | Identifier of a ticker with delimiter to separate base/target | [optional] 
**stock_currency** | **str** | Symbol/currency code of base pair | [optional] 
**money_currency** | **str** | Symbol/currency code of target pair | [optional] 
**last_price** | **str** | Last transacted price of base currency based on given target currency | [optional] 
**stock_volume** | **str** | 24 hour trading volume in base pair volume | [optional] 
**money_volume** | **str** | 24 hour trading volume in target pair volume | [optional] 
**bid** | **str** | Current highest bid price | [optional] 
**ask** | **str** | Current lowest ask price | [optional] 
**high** | **str** | Rolling 24-hours highest transaction price | [optional] 
**low** | **str** | Rolling 24-hours lowest transaction price | [optional] 
**product_type** | **str** | What product is this? Futures, Perpetual, Options? | [optional] 
**open_interest** | **str** | The open interest in the last 24 hours in contracts | [optional] 
**index_price** | **str** | Underlying index price | [optional] 
**index_name** | **str** | Name of the underlying index if any | [optional] 
**index_currency** | **str** | Underlying currency for index | [optional] 
**funding_rate** | **str** | The current funding rate, which may fluctuate due to market conditions | [optional] 
**next_funding_rate_timestamp** | **str** | Timestamp of the next funding rate change | [optional] 
**brackets** | **Dict[str, int]** | Brackets | [optional] 
**max_leverage** | **int** | Max Leverage | [optional] 
**funding_interval_minutes** | **int** | Funding interval in minutes | [optional] 

## Example

```python
from public_api_generated.models.futures_market import FuturesMarket

# TODO update the JSON string below
json = "{}"
# create an instance of FuturesMarket from a JSON string
futures_market_instance = FuturesMarket.from_json(json)
# print the JSON string representation of the object
print(FuturesMarket.to_json())

# convert the object into a dict
futures_market_dict = futures_market_instance.to_dict()
# create an instance of FuturesMarket from a dict
futures_market_from_dict = FuturesMarket.from_dict(futures_market_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


