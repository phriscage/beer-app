# Beer App
This application provides information about Beers. The Beer data is constructed from various Beer microservices.

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Development](#development)
* [Deployment](#deployment)


## <a name="prerequisites"></a>Prerequisites:
* [Docker](https://www.docker.com) installed and running
* [Docker Compose](https://www.docker.com/products/docker-compose) installed
* [Node](https://nodejs.org/en/) installed
* [Npm](https://www.npmjs.com/) installed
* [Google Cloud Platform](https://cloud.google.com/) project created
* [Google Cloud Platform SDK](https://cloud.google.com/sdk/) installed and configured
* [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/) cluster created


## <a name="setup"></a>Setup:
Frontend: 
Install the Node packages via NPM
        
        cd frontend
        npm install

Backend:
TBD


## <a name="development"></a>Development:
Build and run the development environment as a Node instance and Docker application locally. You can specify configuration variables if needed via command line.I.E. `CLIENT_ID=1234 npm run dev`. Make changes accordingly.

Frontend:
        
        cd frontend
        npm run dev

Backend

        TAG=dev make test


## <a name="deployment"></a>Deployment:
Set your **PROJECT_ID** environment variable

        export PROJECT_ID="$(gcloud config get-value project -q)"

Set your **CLUSTER_NAME** environment variable

        export CLUSTER_NAME=beers-cluster

Create a GKE multi-zone cluster with alpha versions enabled:

        gcloud container clusters create $CLUSTER_NAME --zone=us-east4-a --additional-zones us-east4-b,us-east4-c --num-nodes=1 --cluster-version=1.9.2-gke.1 --enable-kubernetes-alpha

Check status:

        gcloud compute instances list

Define the version number as the _TAG_ environment variable and build the image.

        export TAG=<VERSION NUMBER>
        make

Tag and push the new image for GCR

         docker tag <IMAGE ID> gcr.io/${PROJECT_ID}/beer-api:${TAG}
         gcloud docker -- push gcr.io/${PROJECT_ID}/beer-api:${TAG}


Create the application and dependencies in the GKE cluster:

        kubectl create -f manifests/beer-app.yaml

Check the status:

        kubectl get deploy,po,svc -o wide


## To-Do
* automated builds
