# Beer App - Setup Stand Alone
This documentation provides details for how to setup the backend API stand-alone.

* [Setup Backend - Stand-Alone](#setup_backend_stand-alone)

## <a name="setup_backend_stand-alone">Setup Backend - Stand-alone</a>
Set your **CLUSTER_NAME** environment variable

        export CLUSTER_NAME=beer-app

[Setup Kubernetes and Istio](SETUP-KUBERNETES-ISTIO.md)

Create the application and inject the Istio sidecar proxies to the application Pods. The [beer-app_all.yaml](kubernetes-manifests/beer-app/beer-app_all.yaml) configuration has all services and versions:

        kubectl create -f <(istioctl kube-inject -f kubernetes-manifests/beer-app/beer-app_all.yaml)

Check the status, get external ingress IP, and export IP as GATEWAY_URL=<IP:PORT>:

        kubectl get ing,deploy,po,svc -o wide
        export GATEWAY_URL=`kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}'

Launch browser to view the API and OpenAPI Spec:

        http://$GATEWAY_URL/openapi_spec

You can now add an A/CNAME DNS record to the GATEWAY_URL in Cloud DNS. _Integration of Cloud DNS into kubectl ToDo_
