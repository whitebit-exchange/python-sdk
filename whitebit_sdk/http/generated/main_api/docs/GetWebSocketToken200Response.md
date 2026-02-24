# GetWebSocketToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**websocket_token** | **str** | WebSocket authentication token | [optional] 

## Example

```python
from main_api_generated.models.get_web_socket_token200_response import GetWebSocketToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebSocketToken200Response from a JSON string
get_web_socket_token200_response_instance = GetWebSocketToken200Response.from_json(json)
# print the JSON string representation of the object
print(GetWebSocketToken200Response.to_json())

# convert the object into a dict
get_web_socket_token200_response_dict = get_web_socket_token200_response_instance.to_dict()
# create an instance of GetWebSocketToken200Response from a dict
get_web_socket_token200_response_from_dict = GetWebSocketToken200Response.from_dict(get_web_socket_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


