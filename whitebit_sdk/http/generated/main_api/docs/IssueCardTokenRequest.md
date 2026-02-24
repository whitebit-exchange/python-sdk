# IssueCardTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_number** | **str** | Target card number | 

## Example

```python
from main_api_generated.models.issue_card_token_request import IssueCardTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssueCardTokenRequest from a JSON string
issue_card_token_request_instance = IssueCardTokenRequest.from_json(json)
# print the JSON string representation of the object
print(IssueCardTokenRequest.to_json())

# convert the object into a dict
issue_card_token_request_dict = issue_card_token_request_instance.to_dict()
# create an instance of IssueCardTokenRequest from a dict
issue_card_token_request_from_dict = IssueCardTokenRequest.from_dict(issue_card_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


