# GetFixedInvestmentsHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**records** | [**List[Investment]**](Investment.md) |  | [optional] 

## Example

```python
from main_api_generated.models.get_fixed_investments_history200_response import GetFixedInvestmentsHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedInvestmentsHistory200Response from a JSON string
get_fixed_investments_history200_response_instance = GetFixedInvestmentsHistory200Response.from_json(json)
# print the JSON string representation of the object
print(GetFixedInvestmentsHistory200Response.to_json())

# convert the object into a dict
get_fixed_investments_history200_response_dict = get_fixed_investments_history200_response_instance.to_dict()
# create an instance of GetFixedInvestmentsHistory200Response from a dict
get_fixed_investments_history200_response_from_dict = GetFixedInvestmentsHistory200Response.from_dict(get_fixed_investments_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


