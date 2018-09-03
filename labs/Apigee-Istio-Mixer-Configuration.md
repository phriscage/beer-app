# Beer App Labs - Apigee Istio Mixer Configuration
This documentation provides details for Running the Apigee Istio Mixer Lab. 

Please verify that you have read the [prerequisites](../docs/PREREQUISITES.md) and [Setup](../docs/SETUP.md) documents and followed required actions before continuing the Lab exercises.

* [Setup Apigee Istio Mixer](#setup_apigee_istio_mixer)

## <a name="setup_apigee_istio_mixer">Setup Apigee Istio Mixer</a>
These instructions to setup the Apigee Istio Mixer

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

You have now enalbed *authorization* for all services.

Create an API product in your Apigee organization, add the appropriate Beer API services (list below) via Edge Management UI or *apigee-istio* CLI. https://github.com/apigee/istio-mixer-adapter. Create an application and capture the consumer/app key.
```
beer-api.default.svc.cluster.local
details-api.default.svc.cluster.local
reviews-api.default.svc.cluster.local
likes-api.default.svc.cluster.local
```
        
Verify an Ok 200 HTTP status code is returned when trying to access the services with the *x-api-key* header:

        curl -o /dev/null -s -w "%{http_code}\n" http://${GATEWAY_URL}/api/beers -H 'X-api-key: <consumer key>'
