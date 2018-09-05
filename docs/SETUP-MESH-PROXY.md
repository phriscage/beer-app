# Beer App - Setup Mesh Proxy 
This documentation provides details for configuring the Apigee Istio Mixer to leverage Istio's Envoy sidecar proxy. 

Please verify that you have read the [prerequisites](PREREQUISITES.md) and [Setup](SETUP.md) documents and followed required actions before continuing.

* [Setup Apigee Istio Mixer](#setup_apigee_istio_mixer)

## <a name="setup_apigee_istio_mixer">Setup Apigee Istio Mixer</a>
These instructions to configure the Apigee Istio Mixer definitions and handler so requests between services will be enforced via Apigee. 

Apply the Apigee configurations:

        kubectl apply -f istio-manifests/apigee/definitions.yaml
        kubectl apply -f istio-manifests/apigee/handler.yaml

Enalbe the Apigee rule for *authorization* and *analytics* for all _inbound_ requests in the _default_ namespace:
```
  match: context.reporter.kind == "inbound" && destination.namespace == "default"
    && destination.service != "details-db" && destination.service != "reviews-db"
```
        kubectl apply -f istio-manifests/apigee/inbound_default_rule.yaml

Verify an unauthorized 403 HTTP status code is returned when trying to access the services:

        curl -o /dev/null -s -w "%{http_code}\n" http://${GATEWAY_URL}/api/beers

You have now enalbed Apigee *authorization*, *quota enforcement*, and *analytics* for all services in the mesh.
