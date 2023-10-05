# qu.la_internal.EventsApi

All URIs are relative to *http://localhost/public/api/internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_handler**](EventsApi.md#execute_handler) | **POST** /handlers | Execute event handlers
[**get_event_consumers**](EventsApi.md#get_event_consumers) | **GET** /handlers | Get event consumer definitions


# **execute_handler**
> execute_handler(handler_payload=handler_payload)

Execute event handlers

Execute event handler by handler ID

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qu.la_internal
from qu.la_internal.models.handler_payload import HandlerPayload
from qu.la_internal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/public/api/internal
# See configuration.py for a list of all supported configuration parameters.
configuration = qu.la_internal.Configuration(
    host = "http://localhost/public/api/internal"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = qu.la_internal.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with qu.la_internal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qu.la_internal.EventsApi(api_client)
    handler_payload = qu.la_internal.HandlerPayload() # HandlerPayload |  (optional)

    try:
        # Execute event handlers
        await api_instance.execute_handler(handler_payload=handler_payload)
    except Exception as e:
        print("Exception when calling EventsApi->execute_handler: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handler_payload** | [**HandlerPayload**](HandlerPayload.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**501** | Async event handler not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_consumers**
> List[Consumer] get_event_consumers()

Get event consumer definitions

Consumer is defined by unique ID and list of event IDs it consumes

### Example

```python
import time
import os
import qu.la_internal
from qu.la_internal.models.consumer import Consumer
from qu.la_internal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/public/api/internal
# See configuration.py for a list of all supported configuration parameters.
configuration = qu.la_internal.Configuration(
    host = "http://localhost/public/api/internal"
)


# Enter a context with an instance of the API client
async with qu.la_internal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qu.la_internal.EventsApi(api_client)

    try:
        # Get event consumer definitions
        api_response = await api_instance.get_event_consumers()
        print("The response of EventsApi->get_event_consumers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_event_consumers: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Consumer]**](Consumer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**501** | Async event handler not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

