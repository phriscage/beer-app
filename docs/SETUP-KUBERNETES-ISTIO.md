# Beer App - Setup Kubernetes and Istio 
This documentation provides details for how to setup Setup Kubernetes and Istio.

[Setup Kubernetes and Istio](#setup_kubernetes_and_istio)

## <a name="setup_kubernetes_and_istio">Setup Kubernetes and Istio</a>
_CLUSTER_NAME should be already defined_

Create a GKE cluster via *gcloud* or GCP *console*

        gcloud container clusters create $CLUSTER_NAME --zone=us-east4-a --num-nodes=4 --cluster-version=1.10 

        gcloud compute instances list

Enable cluster-admin-binding clusterrolebinding in the cluster:

        kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value core/account)

Install Istio with mTLS:

        kubectl apply -f install/kubernetes/istio-demo-auth.yaml
