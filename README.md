# Microservices Fault Prediction - Local Setup Guide

This repository is a research workspace for forecasting microservice failures from telemetry. Start with [AGENTS.md](AGENTS.md) for agent navigation, [docs/PROJECT_SCOPE.md](docs/PROJECT_SCOPE.md) for the research question, [docs/BASELINE_AUDIT.md](docs/BASELINE_AUDIT.md) for current data readiness, and [docs/LITERATURE_MAP.md](docs/LITERATURE_MAP.md) for the initial paper map. The hand-maintained [ICM system map](map/CONTEXT.md) and generated [graphify report](graphify-out/GRAPH_REPORT.md) describe the present code and research structure. The baseline capture is all zero and must not be used to train a failure predictor.

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


## Telemetry capture and quality audit (Phase 04)

Use the existing project Python environment (`venv`, which includes Parquet support), or provision `google_boutique/requirements.txt` in your chosen environment. The collector defaults to `http://localhost:9090`; pass `--prometheus-url` to match the actual forwarded endpoint. No command overwrites `baseline_run_01`. Exact API/provenance changes are documented in [the Phase 04 audit](docs/telemetry/2026-10-10-phase04.md).

Prepare a filled JSON provenance file from [the capture template](docs/_templates/capture-manifest.json): actual cluster/config revisions, observed workload bounds/evidence, target scrape intervals, and pod/service metadata. `REQUIRED:` placeholders are rejected by the CLI. Start from the repository root, using your recorded UTC capture bounds aligned to five seconds:

```powershell
.\venv\Scripts\python.exe google_boutique/extract_telemetry.py --start "2026-10-11T02:01:30Z" --end "2026-10-11T02:11:30Z" --output-dir "google_boutique/runs/your-new-run" --prometheus-url "http://127.0.0.1:9095" --provenance "your-filled-provenance.json"
.\venv\Scripts\python.exe google_boutique/telemetry_quality.py "google_boutique/runs/your-new-run"
```

Replace the example bounds and paths with your own observed workload interval; historical samples may no longer be retained. A capture exports raw API responses, unfilled values, observed masks, source timestamps, receipt times, source snapshots/dependency versions and hashed manifest. The quality command saves JSON/Markdown and exits 2 when readiness fails. Naive timestamps, existing output directories and incomplete provenance are rejected. The compatibility `extract_dataset` API now treats its output argument as a new directory and retains NaN; tensor construction explicitly selects four primary feature columns and is not performed automatically during capture.

The [canonical Phase 04 run](google_boutique/runs/phase04-20261011T021200Z-audited/QUALITY.md) contains real measurements, but fails the proposed freshness requirement: actual cAdvisor scrapes are ten seconds and source ages exceed ten seconds. HTTP-error series are absent. Historical receipt times do not prove online availability; event-oracle/episode evidence and topology acceptance remain missing. This capture is diagnostic evidence and cannot enable training.
