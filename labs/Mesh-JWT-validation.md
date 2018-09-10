# Beer App Labs - Mesh JWT validation
This documentation provides details for Running the Mesh JWT validation lab.

Please verify that you have read and completed the [prerequisites](../docs/PREREQUISITES.md), [Setup](../docs/SETUP.md), and [Setup Mesh Proxy](../docs/SETUP-MESH-PROXY.md) documents before continuing the Lab exercises.


The Istio Auth Policy for Apigee JWT *authorization* enables JWT validation. Change the  *issuer* and *jwks_url* in the [Policy](istio-manifests/apigee/authentication-default-policy.yaml). This Policy will be applied to all the services in the *default* namepsace
```
  - jwt:
      issuer: urn://chrispage-eval.apigee.net ## apigee-istio token inspect fails
      jwks_uri: https://chrispage-eval-test.apigee.net/v3/oauth/certs
```

Enable the JWT Policy for the cluster *default* namespace:

        kubectl apply -f istio-manifests/apigee/authentication-default-policy.yaml

You can verify it was applied by the following command:

        kubectl get policy --export=true -o yaml

We need a JWT token. So have apigee-istio get you a JWT token:

        ACCESS_TOKEN=`./apigee/apigee-istio token create -e test -o chrispage-eval -u $USERNAME -p $PASSWORD -i $CLIENT_ID -s $CLIENT_SECRET`; clear; echo $ACCESS_TOKEN

Verify an Ok 200 HTTP status code is returned when trying to access the services with the *Authorization* header:

        curl -o /dev/null -s -w "%{http_code}\n" http://${GATEWAY_URL}/api/health -H "Authorization: Bearer ${ACCESS_TOKEN}"

Open the Apigee Edge analytics to view the errors and success for the service proxies.


## Clean up 

        kubectl delete -f istio-manifests/apigee/authentication-default-policy.yaml
