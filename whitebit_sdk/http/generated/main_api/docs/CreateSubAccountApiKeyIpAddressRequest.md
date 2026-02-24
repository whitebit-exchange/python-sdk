# CreateSubAccountApiKeyIpAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** | ID of the API key to add IP address to | 
**ip** | **str** | IP address to add to allowed list | 

## Example

```python
from main_api_generated.models.create_sub_account_api_key_ip_address_request import CreateSubAccountApiKeyIpAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubAccountApiKeyIpAddressRequest from a JSON string
create_sub_account_api_key_ip_address_request_instance = CreateSubAccountApiKeyIpAddressRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSubAccountApiKeyIpAddressRequest.to_json())

# convert the object into a dict
create_sub_account_api_key_ip_address_request_dict = create_sub_account_api_key_ip_address_request_instance.to_dict()
# create an instance of CreateSubAccountApiKeyIpAddressRequest from a dict
create_sub_account_api_key_ip_address_request_from_dict = CreateSubAccountApiKeyIpAddressRequest.from_dict(create_sub_account_api_key_ip_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


