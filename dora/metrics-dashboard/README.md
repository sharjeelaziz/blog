# Metrics Dashboard

## Build the Docker Image

Navigate to the `metric-dashboard` directory containing the Dockerfile and build the Docker image:

```bash
docker build -t jenkins-metrics-dashboard:latest .
```

## Run the Dashboard

Run the Docker container to start the dashboard:

```bash
docker run --env JENKINS_BASE_URL="http://192.168.85.235:8080" --env JENKINS_JOB_NAME="Hello World" --name jenkins-metrics-dashboard -p 5000:5000 -d jenkins-metrics-dashboard:latest
```
