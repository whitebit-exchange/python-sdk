# Oauth2TokenPost422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**Oauth2TokenPost422ResponseErrors**](Oauth2TokenPost422ResponseErrors.md) |  | [optional] 
**notification** | **str** |  | [optional] 

## Example

```python
from oauth2_api_generated.models.oauth2_token_post422_response import Oauth2TokenPost422Response

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2TokenPost422Response from a JSON string
oauth2_token_post422_response_instance = Oauth2TokenPost422Response.from_json(json)
# print the JSON string representation of the object
print(Oauth2TokenPost422Response.to_json())

# convert the object into a dict
oauth2_token_post422_response_dict = oauth2_token_post422_response_instance.to_dict()
# create an instance of Oauth2TokenPost422Response from a dict
oauth2_token_post422_response_from_dict = Oauth2TokenPost422Response.from_dict(oauth2_token_post422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


