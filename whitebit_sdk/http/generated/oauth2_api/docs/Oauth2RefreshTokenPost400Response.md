# Oauth2RefreshTokenPost400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Oauth2RefreshTokenPost400ResponseData**](Oauth2RefreshTokenPost400ResponseData.md) |  | [optional] 

## Example

```python
from oauth2_api_generated.models.oauth2_refresh_token_post400_response import Oauth2RefreshTokenPost400Response

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2RefreshTokenPost400Response from a JSON string
oauth2_refresh_token_post400_response_instance = Oauth2RefreshTokenPost400Response.from_json(json)
# print the JSON string representation of the object
print(Oauth2RefreshTokenPost400Response.to_json())

# convert the object into a dict
oauth2_refresh_token_post400_response_dict = oauth2_refresh_token_post400_response_instance.to_dict()
# create an instance of Oauth2RefreshTokenPost400Response from a dict
oauth2_refresh_token_post400_response_from_dict = Oauth2RefreshTokenPost400Response.from_dict(oauth2_refresh_token_post400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


