# Beer App - Setup
This documentation provides details for how to setup the Beer App interface and API.

* [Setup Frontend](#setup_frontend)
* [Setup Backend - Stand-Alone](#setup_backend_stand-alone)
* [Setup Backend - Hybrid](#setup_backend_hybrid)


## <a name="setup_frontend"></a>Setup Frontend:
Install the Node packages via NPM (This will be added to a Docker development image in the future)

        cd frontend
        npm install

Build and run the development environment as a Node instance and Docker application locally. You can specify configuration variables if needed via command line.I.E. `CLIENT_ID=1234 npm run dev`. Make changes accordingly.

        npm run dev

Launch browser to UI:

        http://localhost:8080


## <a name="setup_backend_stand-alone">Setup Backend - Stand-alone</a>
Set your **CLUSTER_NAME** environment variable

        export CLUSTER_NAME=beer-app

Create a GKE multi-zone cluster with GKE alpha versions enabled:

        gcloud container clusters create $CLUSTER_NAME --zone=us-east4-a --additional-zones us-east4-b,us-east4-c --num-nodes=1 --cluster-version=1.9.6 --enable-kubernetes-alpha

        gcloud compute instances list

Get the credentials for Kubectl:

        gcloud container clusters get-credentials $CLUSTER_NAME

Enable cluster-admin-binding clusterrolebinding in the cluster:

        kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value core/account)

Install Istio:

        kubectl apply -f install/kubernetes/istio-auth.yaml

Create the application and dependencies in the GKE cluster:

        kubectl create -f manifests/beer-app.yaml

Inject the Istio sidecar proxies to the application Pods:

        kubectl apply -f <(istioctl kube-inject -f manifests/beer-app.yaml )

Check the status:

        kubectl get deploy,po,svc -o wide

Get the external IP:

        kubectl get ing -o wide

Launch browser to view the API and OpenAPI Spec:

        http://{EXTERNAL-IP}:80/openapi_spec

You can now add an A/CNAME DNS record to the EXTERNAL-IP in Cloud DNS. _Integration of Cloud DNS into kubectl ToDo_


## <a name="setup_backend_hybrid">Setup Backend - Hybrid</a>
details-api:
Set your **CLUSTER_NAME** environment variable

        export CLUSTER_NAME=details-api

Create a GKE multi-zone cluster with GKE alpha versions enabled:

        gcloud container clusters create $CLUSTER_NAME --zone=us-east4-a --additional-zones us-east4-b,us-east4-c --num-nodes=1 --cluster-version=1.9.6 --enable-kubernetes-alpha

        gcloud compute instances list

Get the credentials for Kubectl:

        gcloud container clusters get-credentials $CLUSTER_NAME

Enable cluster-admin-binding clusterrolebinding in the cluster:

        kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value core/account)

Install Istio:

        kubectl apply -f install/kubernetes/istio-auth.yaml

Create the application and dependencies in the GKE cluster:

        kubectl create -f manifests/beer-app_details.yaml

Inject the Istio sidecar proxies to the application Pods:

        kubectl apply -f <(istioctl kube-inject -f manifests/beer-app_details.yaml)

Check the status:

        kubectl get deploy,po,svc -o wide

Get the external IP:

        kubectl get ing -o wide

Launch browser to view the API and OpenAPI Spec:

        http://{EXTERNAL-IP}:80/details

reviews-api:
Set your **CLUSTER_NAME** environment variable

        export CLUSTER_NAME=reviews-api

Create a GKE multi-zone cluster with GKE alpha versions enabled:

        gcloud container clusters create $CLUSTER_NAME --zone=us-east4-a --additional-zones us-east4-b,us-east4-c --num-nodes=1 --cluster-version=1.9.6 --enable-kubernetes-alpha

        gcloud compute instances list

Get the credentials for Kubectl:

        gcloud container clusters get-credentials $CLUSTER_NAME

Enable cluster-admin-binding clusterrolebinding in the cluster:

        kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value core/account)

Install Istio:

        kubectl apply -f install/kubernetes/istio-auth.yaml

Create the application and dependencies in the GKE cluster:

        kubectl create -f manifests/beer-app_reviews.yaml

Inject the Istio sidecar proxies to the application Pods:

        kubectl apply -f <(istioctl kube-inject -f manifests/beer-app_reviews.yaml)

Check the status:

        kubectl get deploy,po,svc -o wide

Get the external IP:

        kubectl get ing -o wide

Launch browser to view the API and OpenAPI Spec:

        http://{EXTERNAL-IP}:80/reviews

You can now add an A/CNAME DNS record to the EXTERNAL-IP in Cloud DNS. _Integration of Cloud DNS into kubectl ToDo_

