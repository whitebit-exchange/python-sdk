# ErrorInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**errors** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from main_api_generated.models.error_inner import ErrorInner

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorInner from a JSON string
error_inner_instance = ErrorInner.from_json(json)
# print the JSON string representation of the object
print(ErrorInner.to_json())

# convert the object into a dict
error_inner_dict = error_inner_instance.to_dict()
# create an instance of ErrorInner from a dict
error_inner_from_dict = ErrorInner.from_dict(error_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


