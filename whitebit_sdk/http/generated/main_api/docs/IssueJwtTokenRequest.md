# IssueJwtTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**nonce_window** | **bool** | Nonce window setting | [optional] 

## Example

```python
from main_api_generated.models.issue_jwt_token_request import IssueJwtTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssueJwtTokenRequest from a JSON string
issue_jwt_token_request_instance = IssueJwtTokenRequest.from_json(json)
# print the JSON string representation of the object
print(IssueJwtTokenRequest.to_json())

# convert the object into a dict
issue_jwt_token_request_dict = issue_jwt_token_request_instance.to_dict()
# create an instance of IssueJwtTokenRequest from a dict
issue_jwt_token_request_from_dict = IssueJwtTokenRequest.from_dict(issue_jwt_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


