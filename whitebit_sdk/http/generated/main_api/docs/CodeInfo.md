# CodeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Code amount | [optional] 
**code** | **str** | WhiteBIT code | [optional] 
**var_date** | **int** | Code creation timestamp | [optional] 
**status** | **str** | Code status | [optional] 
**ticker** | **str** | Code [ticker](/glossary#ticker) | [optional] 
**external_id** | **str** | Code external identifier | [optional] 

## Example

```python
from main_api_generated.models.code_info import CodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CodeInfo from a JSON string
code_info_instance = CodeInfo.from_json(json)
# print the JSON string representation of the object
print(CodeInfo.to_json())

# convert the object into a dict
code_info_dict = code_info_instance.to_dict()
# create an instance of CodeInfo from a dict
code_info_from_dict = CodeInfo.from_dict(code_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


