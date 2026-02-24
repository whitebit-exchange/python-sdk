# GetFiatDepositUrlRequestCustomerAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** | Customer address line1.  ⚠️ Required if currency USD or EUR with VISAMASTER [provider](/glossary#provider).  | [optional] 
**line2** | **str** | Customer address line2 | [optional] 
**city** | **str** | Customer city.  ⚠️ Required if currency USD or EUR with VISAMASTER [provider](/glossary#provider).  | [optional] 
**zip_code** | **str** | Customer zip-code.  ⚠️ Required if currency USD or EUR with VISAMASTER [provider](/glossary#provider).  | [optional] 
**country_code** | **str** | Customer country code.  ⚠️ Required if currency USD or EUR with VISAMASTER [provider](/glossary#provider).  | [optional] 

## Example

```python
from main_api_generated.models.get_fiat_deposit_url_request_customer_address import GetFiatDepositUrlRequestCustomerAddress

# TODO update the JSON string below
json = "{}"
# create an instance of GetFiatDepositUrlRequestCustomerAddress from a JSON string
get_fiat_deposit_url_request_customer_address_instance = GetFiatDepositUrlRequestCustomerAddress.from_json(json)
# print the JSON string representation of the object
print(GetFiatDepositUrlRequestCustomerAddress.to_json())

# convert the object into a dict
get_fiat_deposit_url_request_customer_address_dict = get_fiat_deposit_url_request_customer_address_instance.to_dict()
# create an instance of GetFiatDepositUrlRequestCustomerAddress from a dict
get_fiat_deposit_url_request_customer_address_from_dict = GetFiatDepositUrlRequestCustomerAddress.from_dict(get_fiat_deposit_url_request_customer_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


