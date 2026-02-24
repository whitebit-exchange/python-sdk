# SubAccountApiKeyAccessEndpointsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Endpoint name | [optional] 
**title** | **str** | Endpoint title | [optional] 

## Example

```python
from main_api_generated.models.sub_account_api_key_access_endpoints_inner import SubAccountApiKeyAccessEndpointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountApiKeyAccessEndpointsInner from a JSON string
sub_account_api_key_access_endpoints_inner_instance = SubAccountApiKeyAccessEndpointsInner.from_json(json)
# print the JSON string representation of the object
print(SubAccountApiKeyAccessEndpointsInner.to_json())

# convert the object into a dict
sub_account_api_key_access_endpoints_inner_dict = sub_account_api_key_access_endpoints_inner_instance.to_dict()
# create an instance of SubAccountApiKeyAccessEndpointsInner from a dict
sub_account_api_key_access_endpoints_inner_from_dict = SubAccountApiKeyAccessEndpointsInner.from_dict(sub_account_api_key_access_endpoints_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


