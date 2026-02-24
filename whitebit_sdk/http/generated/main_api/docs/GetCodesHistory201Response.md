# GetCodesHistory201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of code history entries | [optional] 
**data** | [**List[CodeHistory]**](CodeHistory.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 

## Example

```python
from main_api_generated.models.get_codes_history201_response import GetCodesHistory201Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCodesHistory201Response from a JSON string
get_codes_history201_response_instance = GetCodesHistory201Response.from_json(json)
# print the JSON string representation of the object
print(GetCodesHistory201Response.to_json())

# convert the object into a dict
get_codes_history201_response_dict = get_codes_history201_response_instance.to_dict()
# create an instance of GetCodesHistory201Response from a dict
get_codes_history201_response_from_dict = GetCodesHistory201Response.from_dict(get_codes_history201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


