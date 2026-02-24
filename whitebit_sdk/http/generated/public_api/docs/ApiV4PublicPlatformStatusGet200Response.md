# ApiV4PublicPlatformStatusGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | 1 - system operational, 0 - system maintenance | [optional] 

## Example

```python
from public_api_generated.models.api_v4_public_platform_status_get200_response import ApiV4PublicPlatformStatusGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV4PublicPlatformStatusGet200Response from a JSON string
api_v4_public_platform_status_get200_response_instance = ApiV4PublicPlatformStatusGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV4PublicPlatformStatusGet200Response.to_json())

# convert the object into a dict
api_v4_public_platform_status_get200_response_dict = api_v4_public_platform_status_get200_response_instance.to_dict()
# create an instance of ApiV4PublicPlatformStatusGet200Response from a dict
api_v4_public_platform_status_get200_response_from_dict = ApiV4PublicPlatformStatusGet200Response.from_dict(api_v4_public_platform_status_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


