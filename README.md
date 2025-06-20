# Local Kubernetes ETL Setup

This example shows how to run a simple ETL job on a local Kubernetes cluster using a `hostPath` volume to read an input CSV from your machine.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) or another local Kubernetes cluster

## Build the ETL Image

```bash
# From this directory
docker build -t my-etl-job:latest .
# Load the image into Minikube
minikube image load my-etl-job:latest
```

## Prepare the Data Mount

Assuming your sales data is located at `/home/you/data/sales.csv`:

```bash
minikube mount /home/you/data:/host-data
```

This command makes the local directory available inside the Minikube VM at `/host-data`.
A sample `sales.csv` is provided in the `data/` directory if you want to test quickly.

## Run the Job

Deploy the Kubernetes Job manifest:

```bash
kubectl apply -f etl-job.yaml
```

Monitor the job status and stream the logs while it runs:

```bash
kubectl get pods -w          # watch the pod status
kubectl logs -f job/etl-job  # follow the job logs
```

Exit the log stream with `Ctrl+C`. To check the final job status:

```bash
kubectl get jobs
kubectl describe job/etl-job
```

The container expects the file at `/data/sales.csv` (mounted from the host). After the job completes, you can unmount:

```bash
minikube mount --unmount /home/you/data:/host-data
```

## Cleaning Up

```bash
kubectl delete -f etl-job.yaml
```

