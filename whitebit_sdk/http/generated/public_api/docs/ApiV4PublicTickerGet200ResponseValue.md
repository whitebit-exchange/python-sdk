# ApiV4PublicTickerGet200ResponseValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_id** | **int** | CoinmarketCap Id of base currency; 0 - if unknown | [optional] 
**quote_id** | **int** | CoinmarketCap Id of quote currency; 0 - if unknown | [optional] 
**last_price** | **str** | Last price | [optional] 
**quote_volume** | **str** | Volume in quote currency | [optional] 
**base_volume** | **str** | Volume in base currency | [optional] 
**is_frozen** | **bool** | Identifies if trades are closed | [optional] 
**change** | **str** | Change in percent between open and last prices | [optional] 

## Example

```python
from public_api_generated.models.api_v4_public_ticker_get200_response_value import ApiV4PublicTickerGet200ResponseValue

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV4PublicTickerGet200ResponseValue from a JSON string
api_v4_public_ticker_get200_response_value_instance = ApiV4PublicTickerGet200ResponseValue.from_json(json)
# print the JSON string representation of the object
print(ApiV4PublicTickerGet200ResponseValue.to_json())

# convert the object into a dict
api_v4_public_ticker_get200_response_value_dict = api_v4_public_ticker_get200_response_value_instance.to_dict()
# create an instance of ApiV4PublicTickerGet200ResponseValue from a dict
api_v4_public_ticker_get200_response_value_from_dict = ApiV4PublicTickerGet200ResponseValue.from_dict(api_v4_public_ticker_get200_response_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


