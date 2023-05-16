# HandlerPayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**event** | **str** |  | [optional] 
**payload** | **str** |  | [optional] 

## Example

```python
from qu.la_internal.models.handler_payload import HandlerPayload

# TODO update the JSON string below
json = "{}"
# create an instance of HandlerPayload from a JSON string
handler_payload_instance = HandlerPayload.from_json(json)
# print the JSON string representation of the object
print HandlerPayload.to_json()

# convert the object into a dict
handler_payload_dict = handler_payload_instance.to_dict()
# create an instance of HandlerPayload from a dict
handler_payload_form_dict = handler_payload.from_dict(handler_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


