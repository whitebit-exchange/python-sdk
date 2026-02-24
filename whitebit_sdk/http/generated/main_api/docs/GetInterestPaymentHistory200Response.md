# GetInterestPaymentHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**records** | [**List[InterestPayment]**](InterestPayment.md) |  | [optional] 

## Example

```python
from main_api_generated.models.get_interest_payment_history200_response import GetInterestPaymentHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetInterestPaymentHistory200Response from a JSON string
get_interest_payment_history200_response_instance = GetInterestPaymentHistory200Response.from_json(json)
# print the JSON string representation of the object
print(GetInterestPaymentHistory200Response.to_json())

# convert the object into a dict
get_interest_payment_history200_response_dict = get_interest_payment_history200_response_instance.to_dict()
# create an instance of GetInterestPaymentHistory200Response from a dict
get_interest_payment_history200_response_from_dict = GetInterestPaymentHistory200Response.from_dict(get_interest_payment_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


