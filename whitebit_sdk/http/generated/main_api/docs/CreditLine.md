# CreditLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**total_funding** | **str** |  | [optional] 
**current_ltv** | **str** |  | [optional] 
**initial_ltv** | **str** |  | [optional] 
**margin_call_ltv** | **str** |  | [optional] 
**liquidation_ltv** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 

## Example

```python
from main_api_generated.models.credit_line import CreditLine

# TODO update the JSON string below
json = "{}"
# create an instance of CreditLine from a JSON string
credit_line_instance = CreditLine.from_json(json)
# print the JSON string representation of the object
print(CreditLine.to_json())

# convert the object into a dict
credit_line_dict = credit_line_instance.to_dict()
# create an instance of CreditLine from a dict
credit_line_from_dict = CreditLine.from_dict(credit_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


