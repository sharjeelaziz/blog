
# Setting Up a Test Jenkins Instance

## Introduction

Setting up a test Jenkins instance is great for experimenting with and testing your CI/CD processes without affecting your main work. It's like having a sandbox where you can understand how Jenkins works and try out new things without any risks.

## Deploying Jenkins

- **Get Ready**: We’ll use a Docker image we prepared earlier, stored in the `jenkins-test-instance` folder.
- **Build the Image**: First, let's build our Jenkins Docker image with this command:

   ```bash
   cd jenkins-test-instance
   docker build -t myjenkins-blueocean:2.440.3-1 .
   ```

- **Run Jenkins**: Next, start the Jenkins container:

   ```bash
   docker run --name jenkins-blueocean --restart=always \
    --detach --network jenkins \
    --env DOCKER_HOST=tcp://docker:2376 \
    --env DOCKER_CERT_PATH=/certs/client \
    --env DOCKER_TLS_VERIFY=1 \
    --publish 8080:8080 --publish 50000:50000 \
    --volume $HOME/jenkins/jenkins_home:/var/jenkins_home \
    --volume jenkins-docker-certs:/certs/client:ro \
      myjenkins-blueocean:2.440.3-1
   ```

- **Access Jenkins**: You can access your Jenkins by going to `http://localhost:8080` in your web browser.

## Configuring the Jenkins Job

- **Set Up the Job**: In Jenkins, create a new job and name it "Hello World".

- **Job Script**: We’ll use a simple script [hello-world-job.sh](hello-world-job/hello-world-job.sh) that randomly succeeds or fails to show how Jenkins handles different outcomes. Also, it takes variable amount of time to complete. You can modify to your liking but it is helful in populating jenkins with builds for us. Here’s what the script looks like:

    ```bash
    #!/bin/bash

    execution_time=$((RANDOM % 5 + 1))

    execution_time_seconds=$((execution_time * 60))

    failure_chance=$((RANDOM % 100 + 1))

    echo "Deployment will take will $execution_time minutes."
    sleep $execution_time_seconds

    # Check if deployment should fail (10% chance)
    if [ $failure_chance -le 10 ]; then
    echo "Tests failed!"
    exit 1
    else
    echo "All tests passed!"
    exit 0
    fi
    ```

- **Put the Script to Work**: Add this script as an "Execute Shell" step in the "Build Steps" section of your job settings in Jenkins.

## Generating Build Data

- **Start Building**: Either trigger builds manually or set up a schedule to automatically start builds.

- **Check Results**: Go to the build history in Jenkins to see the results, tracking how often the builds succeed or fail.
