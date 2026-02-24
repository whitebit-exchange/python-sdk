# OrderbookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker_id** | **str** | Market Name | [optional] 
**timestamp** | **int** | Current timestamp | [optional] 
**asks** | **List[List[str]]** | Array of ask orders | [optional] 
**bids** | **List[List[str]]** | Array of bid orders | [optional] 

## Example

```python
from public_api_generated.models.orderbook_response import OrderbookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderbookResponse from a JSON string
orderbook_response_instance = OrderbookResponse.from_json(json)
# print the JSON string representation of the object
print(OrderbookResponse.to_json())

# convert the object into a dict
orderbook_response_dict = orderbook_response_instance.to_dict()
# create an instance of OrderbookResponse from a dict
orderbook_response_from_dict = OrderbookResponse.from_dict(orderbook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


