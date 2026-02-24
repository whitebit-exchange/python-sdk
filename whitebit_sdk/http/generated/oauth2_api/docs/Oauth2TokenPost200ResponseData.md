# Oauth2TokenPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token for API requests | [optional] 
**expires_in** | **int** | Token expiration time in seconds | [optional] 
**refresh_token** | **str** | Token used to refresh the access token | [optional] 
**scope** | **str** | Comma-separated list of granted scopes | [optional] 
**token_type** | **str** | Type of the token | [optional] 

## Example

```python
from oauth2_api_generated.models.oauth2_token_post200_response_data import Oauth2TokenPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2TokenPost200ResponseData from a JSON string
oauth2_token_post200_response_data_instance = Oauth2TokenPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print(Oauth2TokenPost200ResponseData.to_json())

# convert the object into a dict
oauth2_token_post200_response_data_dict = oauth2_token_post200_response_data_instance.to_dict()
# create an instance of Oauth2TokenPost200ResponseData from a dict
oauth2_token_post200_response_data_from_dict = Oauth2TokenPost200ResponseData.from_dict(oauth2_token_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


