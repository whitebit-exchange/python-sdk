# CreateCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | Currency&#39;s [ticker](/glossary#ticker). Example: BTC | 
**amount** | **str** | Amount to transfer. Max [precision](/glossary#precision) &#x3D; 8, value should be greater than zero and your [main balance](/glossary#balance-main). | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**passphrase** | **str** | Passphrase for applying [WhiteBIT codes](/glossary#whitebit-codes). Passphrase must contain only latin letters, numbers and symbols (like !@#$%^, no whitespaces). Max: 25 symbols. | [optional] 
**description** | **str** | Additional text description for [code](/glossary#whitebit-codes). Visible only for creator. Max: 75 symbols. | [optional] 

## Example

```python
from main_api_generated.models.create_code_request import CreateCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCodeRequest from a JSON string
create_code_request_instance = CreateCodeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCodeRequest.to_json())

# convert the object into a dict
create_code_request_dict = create_code_request_instance.to_dict()
# create an instance of CreateCodeRequest from a dict
create_code_request_from_dict = CreateCodeRequest.from_dict(create_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


