# CreateNewAddress201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**GetDepositAddress200ResponseAccount**](GetDepositAddress200ResponseAccount.md) |  | [optional] 
**required** | [**CreateNewAddress201ResponseRequired**](CreateNewAddress201ResponseRequired.md) |  | [optional] 

## Example

```python
from main_api_generated.models.create_new_address201_response import CreateNewAddress201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewAddress201Response from a JSON string
create_new_address201_response_instance = CreateNewAddress201Response.from_json(json)
# print the JSON string representation of the object
print(CreateNewAddress201Response.to_json())

# convert the object into a dict
create_new_address201_response_dict = create_new_address201_response_instance.to_dict()
# create an instance of CreateNewAddress201Response from a dict
create_new_address201_response_from_dict = CreateNewAddress201Response.from_dict(create_new_address201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


