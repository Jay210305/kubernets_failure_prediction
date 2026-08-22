# Microservices Fault Prediction - Local Setup Guide

This guide provides step-by-step instructions to set up the local Kubernetes environment using `kind`, deploy Google's Online Boutique microservices demo, and install the Prometheus/Grafana monitoring stack on Windows.

> **Note on Ports:** Standard ports like `8080` may be occupied by Docker Desktop or other Windows background services. This guide uses alternative host ports (e.g., `8085` for the Boutique Frontend).

---

## 🛠️ 1. Prerequisites (Windows)

Ensure **Docker Desktop** is running before proceeding.

### Install Tools via Winget (PowerShell)
```powershell
# Install Kind (Kubernetes in Docker)
winget install Kubernetes.kind

# Install Helm (Kubernetes Package Manager)
winget install Helm.Helm
```

> **Important:** Restart your PowerShell terminal after installing tools so PowerShell reloads updated environment `PATH` variables.

---

## 🚀 2. Create the Kind Cluster

Navigate to the `google_boutique` folder and instantiate the cluster using the configuration file:

```powershell
cd google_boutique
kind create cluster --config kind-cluster.yaml
```

Verify cluster status:
```powershell
kubectl cluster-info --context kind-aiops-cluster
kubectl get nodes
```

---

## 🛍️ 3. Deploy Google Online Boutique

1. Create the application namespace:
   ```powershell
   kubectl create namespace demo-app
   ```

2. Deploy the microservices manifests:
   ```powershell
   kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/main/release/kubernetes-manifests.yaml -n demo-app
   ```

3. Watch until all pods are running (`1/1 Running`):
   ```powershell
   kubectl get pods -n demo-app -w
   ```

---

## 📊 4. Install Prometheus & Grafana Stack

1. Add and update the Prometheus Helm repository:
   ```powershell
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm repo update
   ```

2. Create the `monitoring` namespace:
   ```powershell
   kubectl create namespace monitoring
   ```

3. Install `kube-prometheus-stack` with a 5-second scrape interval:
   ```powershell
   helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --set prometheus.prometheusSpec.scrapeInterval=5s
   ```

4. Watch monitoring pods:
   ```powershell
   kubectl get pods -n monitoring -w
   ```

---

## 🌐 5. Starting & Accessing Services (Port Forwarding)

Open separate PowerShell terminal windows to keep port-forwarding processes running for each service:

### 🏬 Online Boutique Frontend (Port: 8085)
Since port `8080` is occupied by Docker Desktop / background processes, forward to **`8085`**:
```powershell
kubectl port-forward deployment/frontend -n demo-app 8085:8080
```
👉 Access in Browser: **[http://localhost:8085](http://localhost:8085)**

---

### 📈 Prometheus Server UI (Port: 9090)
```powershell
kubectl port-forward svc/prometheus-kube-prometheus-prometheus -n monitoring 9090:9090
```
👉 Access in Browser: **[http://localhost:9090](http://localhost:9090)**

---

### 🎨 Grafana Dashboards (Port: 3000)
```powershell
kubectl port-forward svc/prometheus-grafana -n monitoring 3000:80
```
👉 Access in Browser: **[http://localhost:3000](http://localhost:3000)**  
- **Default Username:** `admin`  
- **Default Password:** `prom-operator`

