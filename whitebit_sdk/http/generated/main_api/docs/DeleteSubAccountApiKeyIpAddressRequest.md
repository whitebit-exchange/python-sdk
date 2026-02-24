# DeleteSubAccountApiKeyIpAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** | ID of the API key to remove IP address from | 
**ip** | **str** | IP address to remove from allowed list | 

## Example

```python
from main_api_generated.models.delete_sub_account_api_key_ip_address_request import DeleteSubAccountApiKeyIpAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSubAccountApiKeyIpAddressRequest from a JSON string
delete_sub_account_api_key_ip_address_request_instance = DeleteSubAccountApiKeyIpAddressRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteSubAccountApiKeyIpAddressRequest.to_json())

# convert the object into a dict
delete_sub_account_api_key_ip_address_request_dict = delete_sub_account_api_key_ip_address_request_instance.to_dict()
# create an instance of DeleteSubAccountApiKeyIpAddressRequest from a dict
delete_sub_account_api_key_ip_address_request_from_dict = DeleteSubAccountApiKeyIpAddressRequest.from_dict(delete_sub_account_api_key_ip_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


