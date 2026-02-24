# FeeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | Currency [ticker](/glossary#ticker) | [optional] 
**name** | **str** | Currency name | [optional] 
**can_deposit** | **str** | Deposit status (currency availability) | [optional] 
**can_withdraw** | **str** | Withdrawal status (currency availability) | [optional] 
**deposit** | [**FeeInfoDeposit**](FeeInfoDeposit.md) |  | [optional] 
**withdraw** | [**FeeInfoWithdraw**](FeeInfoWithdraw.md) |  | [optional] 

## Example

```python
from main_api_generated.models.fee_info import FeeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FeeInfo from a JSON string
fee_info_instance = FeeInfo.from_json(json)
# print the JSON string representation of the object
print(FeeInfo.to_json())

# convert the object into a dict
fee_info_dict = fee_info_instance.to_dict()
# create an instance of FeeInfo from a dict
fee_info_from_dict = FeeInfo.from_dict(fee_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


