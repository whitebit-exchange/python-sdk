# GetFlexInvestmentHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FlexInvestmentHistory]**](FlexInvestmentHistory.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 

## Example

```python
from main_api_generated.models.get_flex_investment_history200_response import GetFlexInvestmentHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetFlexInvestmentHistory200Response from a JSON string
get_flex_investment_history200_response_instance = GetFlexInvestmentHistory200Response.from_json(json)
# print the JSON string representation of the object
print(GetFlexInvestmentHistory200Response.to_json())

# convert the object into a dict
get_flex_investment_history200_response_dict = get_flex_investment_history200_response_instance.to_dict()
# create an instance of GetFlexInvestmentHistory200Response from a dict
get_flex_investment_history200_response_from_dict = GetFlexInvestmentHistory200Response.from_dict(get_flex_investment_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


