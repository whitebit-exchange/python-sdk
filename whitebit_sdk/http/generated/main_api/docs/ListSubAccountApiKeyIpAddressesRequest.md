# ListSubAccountApiKeyIpAddressesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** | ID of the API key to list IP addresses for | 

## Example

```python
from main_api_generated.models.list_sub_account_api_key_ip_addresses_request import ListSubAccountApiKeyIpAddressesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListSubAccountApiKeyIpAddressesRequest from a JSON string
list_sub_account_api_key_ip_addresses_request_instance = ListSubAccountApiKeyIpAddressesRequest.from_json(json)
# print the JSON string representation of the object
print(ListSubAccountApiKeyIpAddressesRequest.to_json())

# convert the object into a dict
list_sub_account_api_key_ip_addresses_request_dict = list_sub_account_api_key_ip_addresses_request_instance.to_dict()
# create an instance of ListSubAccountApiKeyIpAddressesRequest from a dict
list_sub_account_api_key_ip_addresses_request_from_dict = ListSubAccountApiKeyIpAddressesRequest.from_dict(list_sub_account_api_key_ip_addresses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


