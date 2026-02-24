# ErrorV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** | Error message | [optional] 
**params** | **List[str]** |  | [optional] 

## Example

```python
from public_api_generated.models.error_v4 import ErrorV4

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorV4 from a JSON string
error_v4_instance = ErrorV4.from_json(json)
# print the JSON string representation of the object
print(ErrorV4.to_json())

# convert the object into a dict
error_v4_dict = error_v4_instance.to_dict()
# create an instance of ErrorV4 from a dict
error_v4_from_dict = ErrorV4.from_dict(error_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


