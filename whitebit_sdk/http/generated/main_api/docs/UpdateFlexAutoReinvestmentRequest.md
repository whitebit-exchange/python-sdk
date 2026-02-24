# UpdateFlexAutoReinvestmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | **str** | Plan external ID (UUID). | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**enabled** | **bool** | Enable or disable auto-reinvestment. | [optional] [default to False]

## Example

```python
from main_api_generated.models.update_flex_auto_reinvestment_request import UpdateFlexAutoReinvestmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFlexAutoReinvestmentRequest from a JSON string
update_flex_auto_reinvestment_request_instance = UpdateFlexAutoReinvestmentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFlexAutoReinvestmentRequest.to_json())

# convert the object into a dict
update_flex_auto_reinvestment_request_dict = update_flex_auto_reinvestment_request_instance.to_dict()
# create an instance of UpdateFlexAutoReinvestmentRequest from a dict
update_flex_auto_reinvestment_request_from_dict = UpdateFlexAutoReinvestmentRequest.from_dict(update_flex_auto_reinvestment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


