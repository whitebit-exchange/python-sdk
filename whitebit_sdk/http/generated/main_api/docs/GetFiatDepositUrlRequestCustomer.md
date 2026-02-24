# GetFiatDepositUrlRequestCustomer

Customer information (required for USD/EUR with VISAMASTER [provider](/glossary#provider))

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Customer billing first name.  ⚠️ Required if currency USD or EUR with VISAMASTER [provider](/glossary#provider).  | [optional] 
**last_name** | **str** | Customer billing last name.  ⚠️ Required if currency USD or EUR with VISAMASTER [provider](/glossary#provider).  | [optional] 
**email** | **str** | Customer billing email.  ⚠️ Required if currency USD or EUR with VISAMASTER [provider](/glossary#provider).  | [optional] 
**birth_date** | **date** | Customer birth date (Format YYYY-MM-DD).  ⚠️ Required if currency USD or EUR with VISAMASTER [provider](/glossary#provider).  | [optional] 
**address** | [**GetFiatDepositUrlRequestCustomerAddress**](GetFiatDepositUrlRequestCustomerAddress.md) |  | [optional] 

## Example

```python
from main_api_generated.models.get_fiat_deposit_url_request_customer import GetFiatDepositUrlRequestCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of GetFiatDepositUrlRequestCustomer from a JSON string
get_fiat_deposit_url_request_customer_instance = GetFiatDepositUrlRequestCustomer.from_json(json)
# print the JSON string representation of the object
print(GetFiatDepositUrlRequestCustomer.to_json())

# convert the object into a dict
get_fiat_deposit_url_request_customer_dict = get_fiat_deposit_url_request_customer_instance.to_dict()
# create an instance of GetFiatDepositUrlRequestCustomer from a dict
get_fiat_deposit_url_request_customer_from_dict = GetFiatDepositUrlRequestCustomer.from_dict(get_fiat_deposit_url_request_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


