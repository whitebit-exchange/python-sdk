# Oauth2RefreshTokenPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The new access token for API requests | [optional] 
**expires_in** | **int** | Token expiration time in seconds | [optional] 
**refresh_token** | **str** | New refresh token | [optional] 
**scope** | **str** | Comma-separated list of granted scopes | [optional] 
**token_type** | **str** | Type of the token | [optional] 

## Example

```python
from oauth2_api_generated.models.oauth2_refresh_token_post200_response_data import Oauth2RefreshTokenPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2RefreshTokenPost200ResponseData from a JSON string
oauth2_refresh_token_post200_response_data_instance = Oauth2RefreshTokenPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print(Oauth2RefreshTokenPost200ResponseData.to_json())

# convert the object into a dict
oauth2_refresh_token_post200_response_data_dict = oauth2_refresh_token_post200_response_data_instance.to_dict()
# create an instance of Oauth2RefreshTokenPost200ResponseData from a dict
oauth2_refresh_token_post200_response_data_from_dict = Oauth2RefreshTokenPost200ResponseData.from_dict(oauth2_refresh_token_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


