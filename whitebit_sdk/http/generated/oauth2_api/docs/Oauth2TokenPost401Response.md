# Oauth2TokenPost401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Oauth2TokenPost401ResponseData**](Oauth2TokenPost401ResponseData.md) |  | [optional] 

## Example

```python
from oauth2_api_generated.models.oauth2_token_post401_response import Oauth2TokenPost401Response

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2TokenPost401Response from a JSON string
oauth2_token_post401_response_instance = Oauth2TokenPost401Response.from_json(json)
# print the JSON string representation of the object
print(Oauth2TokenPost401Response.to_json())

# convert the object into a dict
oauth2_token_post401_response_dict = oauth2_token_post401_response_instance.to_dict()
# create an instance of Oauth2TokenPost401Response from a dict
oauth2_token_post401_response_from_dict = Oauth2TokenPost401Response.from_dict(oauth2_token_post401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


