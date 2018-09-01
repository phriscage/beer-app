# Beer App - Development
This documentation provides details for how to extend the Beer App interface and API. 

* [Setup Kubernetes](#setup_kubernetes)
* [Setup Backend](#setup_backend)
* [Setup Frontend](#setup_frontend)
* [Deployment](#deployment)


## <a name="setup_kubernetes">Setup Kubernetes</a>
These instructions to setup a k8s environment are via the *gcloud* SDK CLI. You can also setup via the GCP *console*. 
The k8s environment is only for development and testing using [Skaffold](https://github.com/GoogleContainerTools/skaffold)

Set your **CLUSTER_NAME** environment variable

        export CLUSTER_NAME=skaffold

Create a GKE cluster via *gcloud* CLI and verify the instances are created:

        gcloud container clusters create $CLUSTER_NAME --cluster-version=1.10
        gcloud compute instances list

To authenticate to Container Registry, use gcloud as a [Docker credential helper](https://cloud.google.com/container-registry/docs/advanced-authentication). To do so, run the following command:
Enable 

        gcloud auth configure-docker


## <a name="setup_backend"></a>Setup Backend:
Create the application with [Skaffold](https://github.com/GoogleContainerTools/skaffold)

Beer API development

        skaffold dev


Beer API Development with all service dependencies

        skaffold dev -p test


## <a name="setup_frontend"></a>Setup Frontend:
Install the Node packages via NPM (This will be added to a Docker development image in the future)

        cd frontend
        npm install

Build and run the development environment as a Node instance and Docker application locally. You can specify configuration variables if needed via command line.I.E. `CLIENT_ID=1234 npm run dev`. Make changes accordingly.

        npm run dev

Launch browser to UI:

        http://localhost:8080


## <a name="deployment"></a>Deployment:
Deploy the application with [Skaffold](https://github.com/GoogleContainerTools/skaffold). 

export a TAG environment variable and run the `skaffold run -t <TAG>` command

        export TAG=dev

        skaffold run -t $TAG


## To-Do
* automated builds
