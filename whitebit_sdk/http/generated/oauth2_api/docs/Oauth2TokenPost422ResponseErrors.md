# Oauth2TokenPost422ResponseErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **List[str]** |  | [optional] 
**client_secret** | **List[str]** |  | [optional] 
**code** | **List[str]** |  | [optional] 

## Example

```python
from oauth2_api_generated.models.oauth2_token_post422_response_errors import Oauth2TokenPost422ResponseErrors

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2TokenPost422ResponseErrors from a JSON string
oauth2_token_post422_response_errors_instance = Oauth2TokenPost422ResponseErrors.from_json(json)
# print the JSON string representation of the object
print(Oauth2TokenPost422ResponseErrors.to_json())

# convert the object into a dict
oauth2_token_post422_response_errors_dict = oauth2_token_post422_response_errors_instance.to_dict()
# create an instance of Oauth2TokenPost422ResponseErrors from a dict
oauth2_token_post422_response_errors_from_dict = Oauth2TokenPost422ResponseErrors.from_dict(oauth2_token_post422_response_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


