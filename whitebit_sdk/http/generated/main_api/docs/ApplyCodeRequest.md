# ApplyCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | [Code](/glossary#whitebit-codes) that will be applied. | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**passphrase** | **str** | Should be provided if the [code](/glossary#whitebit-codes) was created with passphrase. Max: 25 symbols. | [optional] 

## Example

```python
from main_api_generated.models.apply_code_request import ApplyCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyCodeRequest from a JSON string
apply_code_request_instance = ApplyCodeRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyCodeRequest.to_json())

# convert the object into a dict
apply_code_request_dict = apply_code_request_instance.to_dict()
# create an instance of ApplyCodeRequest from a dict
apply_code_request_from_dict = ApplyCodeRequest.from_dict(apply_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


