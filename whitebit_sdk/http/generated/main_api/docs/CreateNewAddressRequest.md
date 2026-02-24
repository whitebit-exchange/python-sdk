# CreateNewAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | Currency&#39;s ticker. | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**network** | **str** | Currency&#39;s network (for multinetwork currencies). Example: OMNI or TRC20 or ERC20. For USDT default network is ERC20(ETH).  | [optional] 
**type** | **str** | Address type, available for specific currencies list (see address types table in endpoint description) | [optional] 

## Example

```python
from main_api_generated.models.create_new_address_request import CreateNewAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewAddressRequest from a JSON string
create_new_address_request_instance = CreateNewAddressRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNewAddressRequest.to_json())

# convert the object into a dict
create_new_address_request_dict = create_new_address_request_instance.to_dict()
# create an instance of CreateNewAddressRequest from a dict
create_new_address_request_from_dict = CreateNewAddressRequest.from_dict(create_new_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


