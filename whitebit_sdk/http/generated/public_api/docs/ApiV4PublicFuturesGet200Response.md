# ApiV4PublicFuturesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**List[FuturesMarket]**](FuturesMarket.md) |  | [optional] 

## Example

```python
from public_api_generated.models.api_v4_public_futures_get200_response import ApiV4PublicFuturesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV4PublicFuturesGet200Response from a JSON string
api_v4_public_futures_get200_response_instance = ApiV4PublicFuturesGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV4PublicFuturesGet200Response.to_json())

# convert the object into a dict
api_v4_public_futures_get200_response_dict = api_v4_public_futures_get200_response_instance.to_dict()
# create an instance of ApiV4PublicFuturesGet200Response from a dict
api_v4_public_futures_get200_response_from_dict = ApiV4PublicFuturesGet200Response.from_dict(api_v4_public_futures_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


