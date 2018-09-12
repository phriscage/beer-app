# Beer App Labs - Mesh API Key validation
This documentation provides details for Running the Mesh API Key validation lab.

Please verify that you have read and completed the [prerequisites](../docs/PREREQUISITES.md), [Setup](../docs/SETUP.md), and [Setup Mesh Proxy](../docs/SETUP-MESH-PROXY.md) documents before continuing the Lab exercises.

* [Create API Product and Application](#create_api_product_and_application)

## <a name="create_api_product_and_application">Create API Product and Application</a>
Create an API product in your Apigee organization, set a strict quota (10 calls per minute), and add the appropriate Beer API services (list below) via Edge Management UI or *apigee-istio* CLI. There are instructions for how to leverage the *apigee-istio* command [here](https://github.com/apigee/istio-mixer-adapter).
```
beer-api.default.svc.cluster.local
details-api.default.svc.cluster.local
reviews-api.default.svc.cluster.local
likes-api.default.svc.cluster.local
```
        
Create an application, add the above API product, and capture the consumer/client key. We will use the client key as the credential to call the Beer API services 

        export CLIENT_KEY=<consumer/client key>

Verify an Ok 200 HTTP status code is returned when trying to access the services with the *x-api-key* header:

        curl -o /dev/null -s -w "%{http_code}\n" http://${GATEWAY_URL}/api/health -H "X-api-key: ${CLIENT_KEY}"

Open the Apigee Edge analytics to view the errors and success for the service proxies.


## <a name="next"></a>Next:

        Try some of more [labs](labs)

