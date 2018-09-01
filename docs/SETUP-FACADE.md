# Beer App - Setup Facade
This documentation provides details for how to setup the Facade.

* [Setup Backend - Facade](#setup_backend_facade)

## <a name="setup_backend_facade">Setup Backend - Facade</a>
details-api:
Set your **CLUSTER_NAME** environment variable

        export CLUSTER_NAME=details-api

[Setup Kubernetes and Istio](SETUP-KUBERNETES-ISTIO.md)

Create the application and inject the Istio sidecar proxies to the application Pods:

        kubectl create -f <(istioctl kube-inject -f kubernetes-manifests/beer-app_details.yaml)

Check the status, get external ingress IP, and export IP as GATEWAY_URL=<IP:PORT>:

        kubectl get ing,deploy,po,svc -o wide
        export GATEWAY_URL=`kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}'

Launch browser to view the API and OpenAPI Spec:

        http://$GATEWAY_URL/details

reviews-api:
Set your **CLUSTER_NAME** environment variable

        export CLUSTER_NAME=reviews-api

[Setup Kubernetes and Istio](SETUP-KUBERNETES-ISTIO.md)

Create the application and inject the Istio sidecar proxies to the application Pods:

        kubectl create -f <(istioctl kube-inject -f kubernetes-manifests/beer-app_reviews.yaml)

Check the status, get external ingress IP, and export IP as GATEWAY_URL=<IP:PORT>:

        kubectl get ing,deploy,po,svc -o wide
        export GATEWAY_URL=`kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}'

Launch browser to view the API and OpenAPI Spec:

        http://{GATEWAY_URL}/reviews

You can now add an A/CNAME DNS record to the GATEWAY_URL in Cloud DNS. _Integration of Cloud DNS into kubectl ToDo_
