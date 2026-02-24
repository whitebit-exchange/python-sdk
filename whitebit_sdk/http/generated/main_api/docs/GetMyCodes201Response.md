# GetMyCodes201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of codes | [optional] 
**data** | [**List[CodeInfo]**](CodeInfo.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 

## Example

```python
from main_api_generated.models.get_my_codes201_response import GetMyCodes201Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyCodes201Response from a JSON string
get_my_codes201_response_instance = GetMyCodes201Response.from_json(json)
# print the JSON string representation of the object
print(GetMyCodes201Response.to_json())

# convert the object into a dict
get_my_codes201_response_dict = get_my_codes201_response_instance.to_dict()
# create an instance of GetMyCodes201Response from a dict
get_my_codes201_response_from_dict = GetMyCodes201Response.from_dict(get_my_codes201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


