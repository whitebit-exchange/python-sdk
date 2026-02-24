# ApiV4PublicMarketsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Market pair name | [optional] 
**stock** | **str** | Ticker of stock currency | [optional] 
**money** | **str** | Ticker of money currency | [optional] 
**stock_prec** | **str** | Stock currency precision | [optional] 
**money_prec** | **str** | Precision of money currency | [optional] 
**fee_prec** | **str** | Fee precision | [optional] 
**maker_fee** | **str** | Default maker fee ratio | [optional] 
**taker_fee** | **str** | Default taker fee ratio | [optional] 
**min_amount** | **str** | Minimal amount of stock to trade | [optional] 
**min_total** | **str** | Minimal amount of money to trade | [optional] 
**max_total** | **str** | Maximum total(amount * price) of money to trade | [optional] 
**trades_enabled** | **bool** | Is trading enabled | [optional] 
**is_collateral** | **bool** | Is margin trading enabled | [optional] 
**type** | **str** | Market type. Possible values: spot, futures | [optional] 

## Example

```python
from public_api_generated.models.api_v4_public_markets_get200_response_inner import ApiV4PublicMarketsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV4PublicMarketsGet200ResponseInner from a JSON string
api_v4_public_markets_get200_response_inner_instance = ApiV4PublicMarketsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ApiV4PublicMarketsGet200ResponseInner.to_json())

# convert the object into a dict
api_v4_public_markets_get200_response_inner_dict = api_v4_public_markets_get200_response_inner_instance.to_dict()
# create an instance of ApiV4PublicMarketsGet200ResponseInner from a dict
api_v4_public_markets_get200_response_inner_from_dict = ApiV4PublicMarketsGet200ResponseInner.from_dict(api_v4_public_markets_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


