# CreateWithdrawRequestBeneficiary

Beneficiary information data array.  ⚠️ Required if currency [ticker](/glossary#ticker) is one of: UAH_IBAN, USD_VISAMASTER, EUR_VISAMASTER, USD, EUR 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Beneficiary first name. Max length: 40 symbols, latin letters and special characters.  ⚠️ Required if currency [ticker](/glossary#ticker) is one of: UAH_IBAN, USD_VISAMASTER, USD, EUR  | [optional] 
**last_name** | **str** | Beneficiary last name. Max length: 40 symbols, latin letters and special characters.  ⚠️ Required if currency [ticker](/glossary#ticker) is one of: UAH_IBAN, USD_VISAMASTER, USD, EUR  | [optional] 
**tin** | **int** | Beneficiary TAX payer number. Integer, 10 digits.  ⚠️ Required if currency is UAH_IBAN.  | [optional] 
**phone** | **str** | Beneficiary phone number.  ⚠️ Required if currency [ticker](/glossary#ticker) is one of: USD_VISAMASTER, EUR_VISAMASTER  | [optional] 
**email** | **str** | Beneficiary email.  ⚠️ Required if currency [ticker](/glossary#ticker) is one of: USD_VISAMASTER, EUR_VISAMASTER  | [optional] 
**birth_date** | **date** | Beneficiary birth date. Format: YYYY-MM-DD.  ⚠️ Required if currency [ticker](/glossary#ticker) is one of: USD_VISAMASTER, EUR_VISAMASTER  | [optional] 

## Example

```python
from main_api_generated.models.create_withdraw_request_beneficiary import CreateWithdrawRequestBeneficiary

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWithdrawRequestBeneficiary from a JSON string
create_withdraw_request_beneficiary_instance = CreateWithdrawRequestBeneficiary.from_json(json)
# print the JSON string representation of the object
print(CreateWithdrawRequestBeneficiary.to_json())

# convert the object into a dict
create_withdraw_request_beneficiary_dict = create_withdraw_request_beneficiary_instance.to_dict()
# create an instance of CreateWithdrawRequestBeneficiary from a dict
create_withdraw_request_beneficiary_from_dict = CreateWithdrawRequestBeneficiary.from_dict(create_withdraw_request_beneficiary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


