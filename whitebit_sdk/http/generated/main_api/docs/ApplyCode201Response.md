# ApplyCode201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**ticker** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 

## Example

```python
from main_api_generated.models.apply_code201_response import ApplyCode201Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyCode201Response from a JSON string
apply_code201_response_instance = ApplyCode201Response.from_json(json)
# print the JSON string representation of the object
print(ApplyCode201Response.to_json())

# convert the object into a dict
apply_code201_response_dict = apply_code201_response_instance.to_dict()
# create an instance of ApplyCode201Response from a dict
apply_code201_response_from_dict = ApplyCode201Response.from_dict(apply_code201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


