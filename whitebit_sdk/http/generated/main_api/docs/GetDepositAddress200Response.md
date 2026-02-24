# GetDepositAddress200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**GetDepositAddress200ResponseAccount**](GetDepositAddress200ResponseAccount.md) |  | [optional] 
**required** | [**GetDepositAddress200ResponseRequired**](GetDepositAddress200ResponseRequired.md) |  | [optional] 

## Example

```python
from main_api_generated.models.get_deposit_address200_response import GetDepositAddress200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDepositAddress200Response from a JSON string
get_deposit_address200_response_instance = GetDepositAddress200Response.from_json(json)
# print the JSON string representation of the object
print(GetDepositAddress200Response.to_json())

# convert the object into a dict
get_deposit_address200_response_dict = get_deposit_address200_response_instance.to_dict()
# create an instance of GetDepositAddress200Response from a dict
get_deposit_address200_response_from_dict = GetDepositAddress200Response.from_dict(get_deposit_address200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


