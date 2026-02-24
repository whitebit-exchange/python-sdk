# ListSubAccountsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** | Search term | [optional] 
**limit** | **int** |  | [optional] [default to 30]
**offset** | **int** |  | [optional] [default to 0]

## Example

```python
from main_api_generated.models.list_sub_accounts_request import ListSubAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListSubAccountsRequest from a JSON string
list_sub_accounts_request_instance = ListSubAccountsRequest.from_json(json)
# print the JSON string representation of the object
print(ListSubAccountsRequest.to_json())

# convert the object into a dict
list_sub_accounts_request_dict = list_sub_accounts_request_instance.to_dict()
# create an instance of ListSubAccountsRequest from a dict
list_sub_accounts_request_from_dict = ListSubAccountsRequest.from_dict(list_sub_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


