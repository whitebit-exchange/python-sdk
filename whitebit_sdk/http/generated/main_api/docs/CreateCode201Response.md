# CreateCode201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Generated WhiteBIT code | [optional] 
**message** | **str** | Success message | [optional] 
**external_id** | **str** | External identifier | [optional] 

## Example

```python
from main_api_generated.models.create_code201_response import CreateCode201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCode201Response from a JSON string
create_code201_response_instance = CreateCode201Response.from_json(json)
# print the JSON string representation of the object
print(CreateCode201Response.to_json())

# convert the object into a dict
create_code201_response_dict = create_code201_response_instance.to_dict()
# create an instance of CreateCode201Response from a dict
create_code201_response_from_dict = CreateCode201Response.from_dict(create_code201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


