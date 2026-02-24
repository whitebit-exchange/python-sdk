# SubAccountKyc

KYC information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_kyc** | **bool** | Whether KYC is shared with main account | [optional] 
**kyc_status** | **str** | KYC status | [optional] 

## Example

```python
from main_api_generated.models.sub_account_kyc import SubAccountKyc

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountKyc from a JSON string
sub_account_kyc_instance = SubAccountKyc.from_json(json)
# print the JSON string representation of the object
print(SubAccountKyc.to_json())

# convert the object into a dict
sub_account_kyc_dict = sub_account_kyc_instance.to_dict()
# create an instance of SubAccountKyc from a dict
sub_account_kyc_from_dict = SubAccountKyc.from_dict(sub_account_kyc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


