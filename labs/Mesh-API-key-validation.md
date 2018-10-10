# Beer App Labs - Mesh API Key validation
This documentation provides details for Running the Mesh API Key validation lab.

Please verify that you have read and completed the follow documents before continuing the Lab exercises:

[prerequisites](../docs/PREREQUISITES.md)
[Setup](../docs/SETUP.md)
[Setup Mesh Proxy](../docs/SETUP-MESH-PROXY.md)
[Setup Apigee](../docs/SETUP-APIGEE.md)


* [Create Client Application](#create_client_application)

## <a name="create_client_application">Create Client Application</a>
Create an application, add one of the Beer App API products created in [Setup Apigee](../docs/SETUP-APIGEE.md), and capture the consumer/client key. This can be done via the Apigee Management UI, Developer Portal, or Management API. We will use the client key as the credential to call the Beer API services 

        export CLIENT_KEY=<consumer/client key>

Verify an Ok 200 HTTP status code is returned when trying to access the services with the *x-api-key* header:

        curl -o /dev/null -s -w "%{http_code}\n" http://${GATEWAY_URL}/api/health -H "X-api-key: ${CLIENT_KEY}"

Open the Apigee Edge analytics to view the errors and success for the service proxies.


## <a name="next"></a>Next:

        Try some of more [labs](labs)

