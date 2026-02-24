# CodeHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Code amount change (- is created, + is applied) | [optional] 
**code** | **str** | WhiteBIT code | [optional] 
**var_date** | **int** | Code activation timestamp (for applied) or code creation timestamp (for created) | [optional] 
**status** | **str** | Current code status | [optional] 
**ticker** | **str** | Code [ticker](/glossary#ticker) | [optional] 
**external_id** | **str** | Code external identifier | [optional] 

## Example

```python
from main_api_generated.models.code_history import CodeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of CodeHistory from a JSON string
code_history_instance = CodeHistory.from_json(json)
# print the JSON string representation of the object
print(CodeHistory.to_json())

# convert the object into a dict
code_history_dict = code_history_instance.to_dict()
# create an instance of CodeHistory from a dict
code_history_from_dict = CodeHistory.from_dict(code_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


