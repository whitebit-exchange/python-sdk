# CreateWithdrawRequestTravelRule

Travel Rule information data array.  ⚠️ Required if currency is crypto and you are from [EEA](/glossary#eea) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Travel rule receiver type. Values: \&quot;individual\&quot; or \&quot;entity\&quot;  ⚠️ Required if currency is crypto and you are from [EEA](/glossary#eea)  | [optional] 
**vasp** | **str** | Travel rule destination platform (VASP) name.  ⚠️ Required if currency is crypto and you are from [EEA](/glossary#eea)  | [optional] 
**name** | **str** | Travel rule. If individual - first_name ; if entity - entity_name  ⚠️ Required if currency is crypto and you are from [EEA](/glossary#eea)  | [optional] 
**address** | **str** | Travel rule. If individual - last_name ; if entity - entity_address  ⚠️ Required if currency is crypto and you are from [EEA](/glossary#eea)  | [optional] 

## Example

```python
from main_api_generated.models.create_withdraw_request_travel_rule import CreateWithdrawRequestTravelRule

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWithdrawRequestTravelRule from a JSON string
create_withdraw_request_travel_rule_instance = CreateWithdrawRequestTravelRule.from_json(json)
# print the JSON string representation of the object
print(CreateWithdrawRequestTravelRule.to_json())

# convert the object into a dict
create_withdraw_request_travel_rule_dict = create_withdraw_request_travel_rule_instance.to_dict()
# create an instance of CreateWithdrawRequestTravelRule from a dict
create_withdraw_request_travel_rule_from_dict = CreateWithdrawRequestTravelRule.from_dict(create_withdraw_request_travel_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


