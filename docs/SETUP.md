# Beer App - Setup
This documentation provides details for how to setup the Beer App interface and API. You will need to create a K8s cluster, install the application and start the front-end client

* [Setup Kubernetes and Istio](#setup_kubernetes_and_istio)
* [Setup Backend](#setup_backend)
* [Setup Frontend](#setup_frontend)
* [Cleanup](#cleanup)


## <a name="setup_kubernetes_and_istio">Setup Kubernetes and Istio</a>
These instructions to setup a k8s and Istio environment are via the  *gcloud* SDK CLI. You can also setup via the GCP *console*.

Set your **CLUSTER_NAME** environment variable

        export CLUSTER_NAME=beer-app

Create a GKE cluster via *gcloud* CLI and verify the instances are created:

        gcloud container clusters create $CLUSTER_NAME --zone=us-east4-a --num-nodes=4 --cluster-version=1.10

        gcloud compute instances list

Enable cluster-admin-binding clusterrolebinding in the cluster:

        kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value core/account)

Install Istio with mTLS:

        kubectl apply -f install/kubernetes/istio-demo-auth.yaml


## <a name="setup_backend"></a>Setup Backend:
Create the application and inject the Istio sidecar proxies to the application Pods. There are a few baseline applications that are defined in the [kubernetes-manifests/beer-app](kubernetes-manifests/beer-app) directory. Depending on your demo/lab, you will start with the appropriate one. If unsure, you can default to [beer-app_all.yaml](kubernetes-manifests/beer-app/beer-app_all.yaml)
* [beer-app_all.yaml](kubernetes-manifests/beer-app/beer-app_all.yaml) configuration has all services and versions
* [beer-app_beer-api-v1.yaml](kubernetes-manifests/beer-app/beer-app_beer-api-v1.yaml) configuration has beer-api-v1 without likes-api
* [beer-app_beer-api-v2.yaml](kubernetes-manifests/beer-app/beer-app_beer-api-v2.yaml) configuration has beer-api-v1, beer-api-v2 with likes-api

        kubectl create -f <(istioctl kube-inject -f kubernetes-manifests/beer-app/beer-app_all.yaml)

Enable mTLS policy for the default namespace. You can verify with `kubectl get policy`:

        kubectl apply -f istio-manifests/beer-app/networking/mtls_default_policy.yaml

Create the Ingress Gateway for the application. You can verify with `kubectl get gateway` and `kubectl get virtualservice`:

        kubectl apply -f istio-manifests/beer-app/networking/beer-api_gateway.yaml

Check the status, get external ingress IP, and export IP as GATEWAY_URL=<IP:PORT>:

        kubectl get gateway,virtualservice,deploy,po,svc -o wide
        export GATEWAY_URL=`kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}'`

Verify a 200 HTTP status code is returned when trying to access the openapi_spec:

        curl -o /dev/null -s -w "%{http_code}\n" http://${GATEWAY_URL}/openapi_spec

You can now add an A/CNAME DNS record to the GATEWAY_URL in Cloud DNS. _Integration of Cloud DNS into kubectl ToDo_


## <a name="setup_frontend"></a>Setup Frontend:
Install the Node packages via NPM (This will be added to a Docker development image in the future)

        cd frontend
        npm install

Build and run the development environment as a Node instance and Docker application locally. You can specify configuration variables if needed via command line.I.E. `CLIENT_ID=1234 npm run dev`. Make changes accordingly.

        npm run dev

Launch browser to UI:

        http://localhost:8080


## <a name="setup_frontend"></a>Setup Frontend:
Let's cleanup everything for a fresh start

        kubectl delete -f kubernetes-manifests/beer-app/beer-app_all.yaml
        kubectl delete -f istio-manifests/beer-app/networking/mtls_default_policy.yaml
        kubectl delete -f istio-manifests/beer-app/networking/beer-api_gateway.yaml

