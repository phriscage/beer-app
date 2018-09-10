# Beer App Labs - Mesh JWT claims traffic routing
This documentation provides details for Running the Mesh JWT validation lab.

Please verify that you have read and completed the follow documents before continuing the Lab exercises:

[prerequisites](../docs/PREREQUISITES.md)
[Setup](../docs/SETUP.md)
[Setup Mesh Proxy](../docs/SETUP-MESH-PROXY.md)
[Mesh JWT validation](Mesh-JWT-validation.md)


Enable all the Beer App services to route to *v1* via the [virtual-service-all-v1.yaml](istio-manifests/beer-app/networking/virtual-service-all-v1.yaml) file. This changes all VirtualService destinations to be *v1*. _Note_ Beer App VirtualService needs to bind to the Ingress Gateway.

        kubectl apply -f istio-manifests/beer-app/networking/virtual-service-all-v1.yaml
        

Verify only *v1* FQDNs are returned from the health check service with the *Authorization* header:

        curl -s http://${GATEWAY_URL}/api/health?debug=true -H "Authorization: Bearer $ACCESS_TOKEN" | python -c "import sys, json; print json.load(sys.stdin)['data']['host']['fqdn']"

Dynamically route the *@google.com* authorized users to route to *v2* of the Beer API via the [virtual-service-beer-api-google.com-v2.yaml](istio-manifests/beer-app/networking/virtual-service-beer-api-google.com-v2.yaml). This file changes the Beer App VirtualService destinations for Beer API to be *v2* for any *@google.com* email claim.

        kubectl apply -f istio-manifests/beer-app/networking/virtual-service-beer-api-google.com-v2.yaml
        

Verify only *v2* FQDNs are returned from the health check service with the *Authorization* header: _Note_ The _request.auth.claims_ property is not available in the routing spec yet so we pass a HTTP header instead. 

        curl -s http://${GATEWAY_URL}/api/health?debug=true -H "Authorization: Bearer $ACCESS_TOKEN" -H "x-email: chrispage@google.com" | python -c "import sys, json; print json.load(sys.stdin)['data']['host']['fqdn']"

Open the Apigee Edge analytics to view the errors and success for the service proxies.


## Clean up

        kubectl delete -f istio-manifests/beer-app/networking/virtual-service-beer-api-google.com-v2.yaml
