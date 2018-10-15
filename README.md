# Beer App
## <a name="overview">Overview</a>
This application provides information about beer data in a simple interface. The application is comprised of a lightweight, responsive browser interface, a Beer Data API, and corresponding Beer microservices. The Beer API is exposed either through an API Management proxy endpoint or Istio ingress point with Apigee Edge enforcing AuthN/AuthZ, Security, Quota, Rate limting, etc. The Beer API is constructed from various Beer microservices (Details, Reviews, Likes, etc.) that run in a Kubernetes (K8s) cluster. Istio is installed in the K8s cluster to provide service mesh management by leveraging Envoy as a sidecar proxy. Istio provides traffic management, observability, policy enforcement, and security (mTLS) for the cluster services. The Apigee Istio Mixer plugin provides additional security and governance with api key/token validation, quota enforcement, and analytics.

These are the API Management deployment patterns:

* **Edge Proxy** environment: The Beer API and services reside in a K8s environment (private or public cloud) and are proxied directly from the API Management Edge proxy. This is the default example. 

![alt text](images/beer-app_architecture.png)

* **Mesh Proxy** environment: The Beer API and services reside in a K8s environment (private or public cloud) and are proxied directly from the Istio/Envoy sidecar proxies. This is the Apigee Istio Mixer example. 

![alt text](images/beer-app_architecture-mesh.png)

* **Facade Proxy** environment: The Beer API services reside in separate K8s environment(s) (private and public cloud) or namespaces and the Beer API is orchestrated and proxied from the API Management platform.

![alt text](images/beer-app_architecture-facade.png)

The examples focus on running the Beer App services in [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/). Additional examples will be provided for Docker for Desktop, Minikube, Pivotal Cloud Foundry, etc. 

There are a few [prerequisites](docs/PREREQUISITES.md) that need to be validated and/or installed before continuing to the setup. The [Setup](docs/SETUP.md) contains all the commands required to setup the environment to run the demo and labs.

* [Prerequisites](docs/PREREQUISITES.md)
* [Setup](docs/SETUP.md)
* [Labs!](labs/)
* [Development](docs/DEVELOPMENT.md)
* [To-Do](#todo)


## <a name="todo">To Do!</a>
* ~~Frontend has not been containerized and ported to K8s yet. Manual installation required for now...~~ updated
* Add Cloud DNS A/CNAME record creation in app 
