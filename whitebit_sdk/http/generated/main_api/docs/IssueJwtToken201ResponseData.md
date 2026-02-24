# IssueJwtToken201ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | JWT token | [optional] 
**expires_at** | **int** | Token expiration timestamp | [optional] 

## Example

```python
from main_api_generated.models.issue_jwt_token201_response_data import IssueJwtToken201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of IssueJwtToken201ResponseData from a JSON string
issue_jwt_token201_response_data_instance = IssueJwtToken201ResponseData.from_json(json)
# print the JSON string representation of the object
print(IssueJwtToken201ResponseData.to_json())

# convert the object into a dict
issue_jwt_token201_response_data_dict = issue_jwt_token201_response_data_instance.to_dict()
# create an instance of IssueJwtToken201ResponseData from a dict
issue_jwt_token201_response_data_from_dict = IssueJwtToken201ResponseData.from_dict(issue_jwt_token201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


