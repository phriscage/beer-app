# Beer App
This application provides information about Beers in a simple interface. The application is comprised of a lightweight, responsive browser interface, a Beer Data API, and corespeonding Beer microservices. The Beer API is exposed through an API Proxy endpoint point that enforces AuthN/AuthZ, Security, Rate limting, etc. The Beer API is constructed from various Beer microservices (Details, Reviews, etc.) that run in a Kubernetes (K8s) cluster. 

These are the initial deployment patterns:

* **Self-contained application environment:** The Beer API and services reside in a K8s environment (private or public cloud) and is proxied directly from the API Management platform.

<details>
  <summary>Graphviz Source</summary>
  <pre><code>
![alt text]('https://g.gravizo.com/svg?
  digraph G {
    rankdir=LR;
    edge [dir=both];
    {rank=same; idp, proxy};
    {rank=same; };

    subgraph cluster_ms {
      api; ms1; ms2; db1; db2;
      label="private/public";
    }

    client [label="client", shape=box];
    idp [label="identity"];
    proxy [label="proxy"];
    api [label="api"];
    ms1 [label="service"];
    ms2 [label="service"];
    db1  [label="data", shape=box];
    db2  [label="data", shape=box];

    spacing [label="", style=invisible];
    client -> proxy;
    proxy -> idp [style=dotted, dir=none];
    proxy -> api [style=dotted, dir=none];
    api -> ms1 [style=dotted, dir=none];
    api -> ms2 [style=dotted, dir=none];
    ms1 -> db1 [style=dotted, dir=none];
    ms2 -> db2 [style=dotted,  dir=none];
  }
  </pre></code>
</details>
![alt text](https://g.gravizo.com/svg?%20digraph%20G%20{%20rankdir=LR;%20edge%20[dir=both];%20{rank=same;%20idp,%20proxy};%20{rank=same;%20};%20subgraph%20cluster_ms%20{%20api;%20ms1;%20ms2;%20db1;%20db2;%20label=%22private/public%22;%20}%20client%20[label=%22client%22,%20shape=box];%20idp%20[label=%22identity%22];%20proxy%20[label=%22proxy%22];%20api%20[label=%22api%22];%20ms1%20[label=%22service%22];%20ms2%20[label=%22service%22];%20db1%20[label=%22data%22,%20shape=box];%20db2%20[label=%22data%22,%20shape=box];%20spacing%20[label=%22%22,%20style=invisible];%20client%20-%3E%20proxy;%20proxy%20-%3E%20idp%20[style=dotted,%20dir=none];%20proxy%20-%3E%20api%20[style=dotted,%20dir=none];%20api%20-%3E%20ms1%20[style=dotted,%20dir=none];%20api%20-%3E%20ms2%20[style=dotted,%20dir=none];%20ms1%20-%3E%20db1%20[style=dotted,%20dir=none];%20ms2%20-%3E%20db2%20[style=dotted,%20dir=none];%20})

* **Hybrid private and public application environment:** The Beer API services reside in separate or hybrid K8s environment(s) (private and public cloud) and the Beer API is orchestrated and proxied from the API Management platform.

<details>
  <summary>Graphviz Source</summary>
  <pre><code>
![alt text]('https://g.gravizo.com/svg?
  digraph G {
    rankdir=LR;
    edge [dir=both];
    {rank=same; idp, proxy};
    {rank=same; };

    subgraph cluster_ms1 {
      ms1; db1;
      label="public";
    }

    subgraph cluster_ms2 {
      ms2; db2;
      label="private";
    }

    client [label="client", shape=box];
    idp [label="identity"];
    proxy [label="proxy"];
    ms1 [label="service"];
    ms2 [label="service"];
    db1  [label="data", shape=box];
    db2  [label="data", shape=box];
 
    spacing [label="", style=invisible];
    client -> proxy;
    proxy -> idp [style=dotted, dir=none];
    proxy -> ms1 [style=dotted, dir=none];
    proxy -> ms2 [style=dotted, dir=none];
    ms1 -> db1 [style=dotted, dir=none];
    ms2 -> db2 [style=dotted,  dir=none];
  }
  </pre></code>
</details>
![alt text](https://g.gravizo.com/svg?%20digraph%20G%20{%20rankdir=LR;%20edge%20[dir=both];%20{rank=same;%20idp,%20proxy};%20{rank=same;%20};%20subgraph%20cluster_ms1%20{%20ms1;%20db1;%20label=%22public%22;%20}%20subgraph%20cluster_ms2%20{%20ms2;%20db2;%20label=%22private%22;%20}%20client%20[label=%22client%22,%20shape=box];%20idp%20[label=%22identity%22];%20proxy%20[label=%22proxy%22];%20ms1%20[label=%22service%22];%20ms2%20[label=%22service%22];%20db1%20[label=%22data%22,%20shape=box];%20db2%20[label=%22data%22,%20shape=box];%20spacing%20[label=%22%22,%20style=invisible];%20client%20-%3E%20proxy;%20proxy%20-%3E%20idp%20[style=dotted,%20dir=none];%20proxy%20-%3E%20ms1%20[style=dotted,%20dir=none];%20proxy%20-%3E%20ms2%20[style=dotted,%20dir=none];%20ms1%20-%3E%20db1%20[style=dotted,%20dir=none];%20ms2%20-%3E%20db2%20[style=dotted,%20dir=none];%20})

The initial example, **Self-contained**, focuses on running the Beer App in [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/). Additional examples will be provided for Minikube, Pivotal Cloud Foundry, etc. 

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Quickstart](#quickstart)
* [Development](DEVELOPMENT.md)
* [To-Do](#todo)


## <a name="prerequisites"></a>Prerequisites:
* [Google Cloud Platform](https://cloud.google.com/) project created
* [Google Cloud Platform SDK](https://cloud.google.com/sdk/) installed and configured
* [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/) cluster knowledge

* [Node](https://nodejs.org/en/) installed
* [Npm](https://www.npmjs.com/) installed


## <a name="setup"></a>Setup:
Frontend:
Install the Node packages via NPM (This will be added to a Docker development image in the future)

        cd frontend
        npm install

Backend:
Set your **PROJECT_ID** environment variable

        export PROJECT_ID="$(gcloud config get-value project -q)"

Set your **CLUSTER_NAME** environment variable

        export CLUSTER_NAME=beer-app

Create a GKE multi-zone cluster with GKE alpha versions enabled:

        gcloud container clusters create $CLUSTER_NAME --zone=us-east4-a --additional-zones us-east4-b,us-east4-c --num-nodes=1 --cluster-version=1.9.2-gke.1 --enable-kubernetes-alpha

        gcloud compute instances list

Get the credentials for Kubectl:

        gcloud container clusters get-credentials $CLUSTER_NAME


## <a name="quickstart">Quickstart</a>
Frontend:
Build and run the development environment as a Node instance and Docker application locally. You can specify configuration variables if needed via command line.I.E. `CLIENT_ID=1234 npm run dev`. Make changes accordingly.

        npm run dev

Launch browser to UI:

        http://localhost:8080

Backend:
Create the application and dependencies in the GKE cluster:

        kubectl create -f manifests/beer-app.yaml

Check the status:

        kubectl get deploy,po,svc -o wide

Get the external IP:

        kubectl get svc -l app=beer-api

Launch browser to view the API and OpenAPI Spec:

        http://{EXTERNAL-IP}:80/openapi_spec

You can now add an A/CNAME DNS record to the EXTERNAL-IP in Cloud DNS. _Integration of Cloud DNS into kubectl ToDo_


## <a name="todo">To Do!</a>
* Frontend has not been containerized and ported to K8s yet. Manual installation required for now...
* Add Cloud DNS A/CNAME record creation in app 
