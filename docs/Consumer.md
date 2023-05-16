# Consumer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**events** | [**List[Event]**](Event.md) |  | [optional] 

## Example

```python
from qu.la_internal.models.consumer import Consumer

# TODO update the JSON string below
json = "{}"
# create an instance of Consumer from a JSON string
consumer_instance = Consumer.from_json(json)
# print the JSON string representation of the object
print Consumer.to_json()

# convert the object into a dict
consumer_dict = consumer_instance.to_dict()
# create an instance of Consumer from a dict
consumer_form_dict = consumer.from_dict(consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


