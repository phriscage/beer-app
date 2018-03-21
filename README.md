# Beer App
This application provides information about Beers in a simple interface. The application is comprised of a lightweight, responsive Javascript interface and a Beer Data API. The Beer API is exposed through an API Proxy endpoint point that enforces AuthN/AuthZ, Security, Rate limting, etc. The Beer API version 1 is constructed from various Beer microservices (Details, Reviews, etc.) that run in a Kubernetes (K8s) cluster. Beer service version 1 can currenlty run in any K8s compatible environment. 

This initial example focuses on running the Beer App in [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/). Additional examples will be provided for Minikube, Pivotal Cloud Foundry, etc.

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Development](DEVELOPMENT.md)


## <a name="prerequisites"></a>Prerequisites:
* [Google Cloud Platform](https://cloud.google.com/) project created
* [Google Cloud Platform SDK](https://cloud.google.com/sdk/) installed and configured
* [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/) cluster knowledge


## <a name="Setup"></a>Deployment:
Set your **PROJECT_ID** environment variable

        export PROJECT_ID="$(gcloud config get-value project -q)"

Set your **CLUSTER_NAME** environment variable

        export CLUSTER_NAME=beers-cluster

Create a GKE multi-zone cluster with GKE alpha versions enabled:

        gcloud container clusters create $CLUSTER_NAME --zone=us-east4-a --additional-zones us-east4-b,us-east4-c --num-nodes=1 --cluster-version=1.9.2-gke.1 --enable-kubernetes-alpha

Check status:

        gcloud compute instances list

Create the application and dependencies in the GKE cluster:

        kubectl create -f manifests/beer-app.yaml

Check the status:

        kubectl get deploy,po,svc -o wide

Launch browser to UI and API:

        http://localhost:80
        http://localhost:8080
