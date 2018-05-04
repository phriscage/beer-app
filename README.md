# Beer App
This application provides information about Beers in a simple interface. The application is comprised of a lightweight, responsive browser interface, a Beer Data API, and corespeonding Beer microservices. The Beer API is exposed through an API Management proxy endpoint point that enforces AuthN/AuthZ, Security, Rate limting, etc. The Beer API is constructed from various Beer microservices (Details, Reviews, etc.) that run in a Kubernetes (K8s) cluster. Istio is installed in the K8s cluster to provide service mesh management by leveraging Envoy as a sidecar proxy. Istio initially provides routing, load balancing, and security (mTLS) for the cluster services.

These are the initial deployment patterns:

* **Stand-alone** application environment: The Beer API and services reside in a K8s environment (private or public cloud) and is proxied directly from the API Management platform. This is the default example. 

![alt text](images/beer-app_architecture.png)

* **Hybrid** private and/or public application environment: The Beer API services reside in separate or hybrid K8s environment(s) (private and public cloud) and the Beer API is orchestrated and proxied from the API Management platform.

![alt text](images/beer-app_architecture-hybrid.png)

The initial examples, **Stand-alone** and **Hybrid**, focuses on running the Beer App services in [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/). Additional examples will be provided for Minikube, Pivotal Cloud Foundry, etc. 

* [Prerequisites](#prerequisites)
* [Setup](SETUP.md)
* [API Management](APIGEE.md)
* [Development](DEVELOPMENT.md)
* [To-Do](#todo)


## <a name="prerequisites"></a>Prerequisites:
* [Google Cloud Platform](https://cloud.google.com/) project created
* [Google Cloud Platform SDK](https://cloud.google.com/sdk/) installed and configured
* [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/) cluster knowledge
* [Istio](https://istio.io/) service mesh management knowledge

* [Node](https://nodejs.org/en/) installed
* [Npm](https://www.npmjs.com/) installed


## <a name="todo">To Do!</a>
* Frontend has not been containerized and ported to K8s yet. Manual installation required for now...
* Add Cloud DNS A/CNAME record creation in app 
