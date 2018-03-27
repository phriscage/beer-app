# Beer App - Development
This documentation provides details for how to extend the Beer App interface and API. 

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Deployment](#deployment)


## <a name="prerequisites"></a>Prerequisites:
* [Docker](https://www.docker.com) installed and running
* [Docker Compose](https://www.docker.com/products/docker-compose) installed
* [Node](https://nodejs.org/en/) installed
* [Npm](https://www.npmjs.com/) installed


## <a name="setup"></a>Setup:
Frontend: 
Install the Node packages via NPM (This will be added to a Docker development image in the future)
        
        cd frontend
        npm install

Backend:
N/A

Build and run the development environment as a Node instance and Docker application locally. You can specify configuration variables if needed via command line.I.E. `CLIENT_ID=1234 npm run dev`. Make changes accordingly.

Frontend:
        
        npm run dev

Backend

        TAG=dev make test


## <a name="deployment"></a>Deployment:
Set your **PROJECT_ID** environment variable

        export PROJECT_ID="$(gcloud config get-value project -q)"

Set your **CLUSTER_NAME** environment variable

        export CLUSTER_NAME=beer-app

Get the credentials for Kubectl:

        gcloud container clusters get-credentials $CLUSTER_NAME

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


### Deployment Updates:
Update the container image name/version for an existing deployment

        kubectl set image deployment/beer-api beer-api=gcr.io/${PROJECT_ID}/beer-api:${TAG}


## To-Do
* automated builds
