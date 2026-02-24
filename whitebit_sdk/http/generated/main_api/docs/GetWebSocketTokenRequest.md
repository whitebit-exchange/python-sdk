# GetWebSocketTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 

## Example

```python
from main_api_generated.models.get_web_socket_token_request import GetWebSocketTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebSocketTokenRequest from a JSON string
get_web_socket_token_request_instance = GetWebSocketTokenRequest.from_json(json)
# print the JSON string representation of the object
print(GetWebSocketTokenRequest.to_json())

# convert the object into a dict
get_web_socket_token_request_dict = get_web_socket_token_request_instance.to_dict()
# create an instance of GetWebSocketTokenRequest from a dict
get_web_socket_token_request_from_dict = GetWebSocketTokenRequest.from_dict(get_web_socket_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


