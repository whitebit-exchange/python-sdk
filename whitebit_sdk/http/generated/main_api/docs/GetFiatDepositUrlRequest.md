# GetFiatDepositUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | Currency&#39;s [ticker](/glossary#ticker) ([fiat](/glossary#fiat)). ⚠️ Currencies ticker should be fiat and has \&quot;can_deposit\&quot; status must be \&quot;true\&quot;. Use [Asset Status endpoint](/public/http-v4/asset-status-list) to know more about currency. | 
**provider** | **str** | [Fiat](/glossary#fiat) currency [provider](/glossary#provider). ⚠️ Currency provider should be taken from [Asset Status endpoint](/public/http-v4/asset-status-list) response. | 
**amount** | **str** | Deposit amount | 
**unique_id** | **str** | Unique transaction identifier on client&#39;s side | 
**request** | **str** | Request signature | 
**nonce** | **str** | Unique request identifier | 
**customer** | [**GetFiatDepositUrlRequestCustomer**](GetFiatDepositUrlRequestCustomer.md) |  | [optional] 
**success_link** | **str** | Customer will be redirected to this URL by acquiring [provider](/glossary#provider) after success deposit. To activate this feature, please contact support | [optional] 
**failure_link** | **str** | Customer will be redirected to this URL in case of fail or rejection on acquiring provider side. To activate this feature, please contact support | [optional] 
**return_link** | **str** | Customer will be redirected to the URL defined if selects &#39;back&#39; option after from the payment success or failure page. To activate this feature, define desired link. If not populated, option &#39;back&#39; won&#39;t be displayed | [optional] 

## Example

```python
from main_api_generated.models.get_fiat_deposit_url_request import GetFiatDepositUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetFiatDepositUrlRequest from a JSON string
get_fiat_deposit_url_request_instance = GetFiatDepositUrlRequest.from_json(json)
# print the JSON string representation of the object
print(GetFiatDepositUrlRequest.to_json())

# convert the object into a dict
get_fiat_deposit_url_request_dict = get_fiat_deposit_url_request_instance.to_dict()
# create an instance of GetFiatDepositUrlRequest from a dict
get_fiat_deposit_url_request_from_dict = GetFiatDepositUrlRequest.from_dict(get_fiat_deposit_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


