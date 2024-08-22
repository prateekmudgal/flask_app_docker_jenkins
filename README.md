

---

# Flask App Dockerized with Jenkins

This repository contains a sample Flask application that is fully Dockerized and integrated with Jenkins for automated CI/CD pipelines. This project also demonstrates a Jenkins master-slave architecture where all stages are executed on the agent node.

## Table of Contents

- [Flask App Dockerized with Jenkins](#flask-app-dockerized-with-jenkins)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Setup and Installation](#setup-and-installation)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
      - [Clone the Repository](#clone-the-repository)
  - [Dockerfile](#dockerfile)
    - [Explanation](#explanation)
  - [Manual Docker Operations](#manual-docker-operations)
    - [Build Docker Image Manually](#build-docker-image-manually)
    - [Run Docker Container Manually](#run-docker-container-manually)
  - [Running Jenkins Agent as a Service](#running-jenkins-agent-as-a-service)
    - [Instructions](#instructions)
  - [Jenkins Pipeline](#jenkins-pipeline)
    - [Adding a Docker Build Job in Jenkins](#adding-a-docker-build-job-in-jenkins)
    - [Jenkins Master-Slave Architecture](#jenkins-master-slave-architecture)
    - [Pipeline Stages](#pipeline-stages)
      - [Jenkinsfile Configuration](#jenkinsfile-configuration)
      - [Stage Descriptions](#stage-descriptions)
  - [Conclusion](#conclusion)

## Project Overview

This Proof of Concept (POC) demonstrates the deployment of a sample Flask application using Docker containers. The application leverages Jenkins for Continuous Integration and Continuous Deployment (CI/CD).

The objective of this project is to showcase the integration of Jenkins and Docker, and how they can be used together to automate the build, test, and deployment processes.

## Features

- **Flask Application**: A basic web application built with Flask.
- **Dockerized Environment**: Containerization of the Flask app using Docker.
- **Jenkins Integration**: Automated CI/CD pipeline utilizing Jenkins.
- **Jenkins Master-Slave Architecture**: Distributed build environment with Jenkins agents.
- **Manual Docker Operations**: Option to manually build and run Docker containers.
- **Running Jenkins Agent as a Service**: Ensures the Jenkins agent node remains online even if the instance restarts.
- **Docker Build Job in Jenkins**: Automates Docker image creation within Jenkins.

## Setup and Installation

### Prerequisites

Before starting, ensure you have the following installed:

- **Docker**: [Installation Guide](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Installation Guide](https://docs.docker.com/compose/install/)
- **Jenkins**: [Installation Guide](https://www.jenkins.io/doc/book/installing/)
- **Git**: [Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Installation

#### Clone the Repository

```bash
git clone https://github.com/prateekmudgal/flask_app_docker_jenkins_sonarqube.git
cd flask_app_docker_jenkins_sonarqube
docker build -t prateek0912/sample-python:latest .
```

- **Access the Application**

  Open your browser and navigate to `http://localhost:7077` to see the Flask application in action.

## Dockerfile

The Dockerfile for this project is designed to create a lightweight and efficient Docker image for the Flask application. Below is the content of the Dockerfile used:

```dockerfile
FROM python:3.6

MAINTAINER Prateek Mudgal "mudgalprateek00@gmail.com"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
```

### Explanation

- **FROM python:3.6**: Specifies the base image, which is Python version 3.6.
- **MAINTAINER Prateek Mudgal**: Specifies the maintainer of the Docker image.
- **COPY . /app**: Copies the entire current directory (`.`) to the `/app` directory in the Docker image.
- **WORKDIR /app**: Sets the working directory inside the Docker image to `/app`.
- **RUN pip install -r requirements.txt**: Installs the required Python packages specified in the `requirements.txt` file.
- **ENTRYPOINT ["python"]**: Sets the entry point for the Docker container to run Python.
- **CMD ["app.py"]**: Specifies the default command to run when the container starts, which is executing `app.py`.

## Manual Docker Operations

While this project is primarily automated through Jenkins, you can perform manual Docker operations as follows:

### Build Docker Image Manually

```bash
docker build -t prateek0912/sample-python:latest .
```

### Run Docker Container Manually

```bash
docker run -d -p 7077:5000 prateek0912/sample-python
```

## Running Jenkins Agent as a Service

To ensure that the Jenkins agent (node) remains online even if the instance restarts or shuts down, you can run the Jenkins agent as a service using the following script. This script configures the Jenkins agent to automatically restart if it goes down.

Create a file named `node_script.sh` in the repository with the following configuration:

```bash
[Unit]
Description=Jenkins Agent

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu
ExecStart=/usr/bin/java -jar /home/ubuntu/agent.jar -url http://3.15.9.194:8080/ -secret 7acc512dbb34dec0e7d5641ad8a725dd226cc220e8bbefc51150996d91804d94 -name dockerengine -workDir "/home/ubuntu"
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### Instructions

1. **Create the Script**: Add the above script to your repository.
2. **Install the Service**:
   - Copy the script to the `/etc/systemd/system/` directory.
   - Enable the service to start on boot with the following commands:
   
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable node_script.sh
   sudo systemctl start node_script.sh
   ```
3. **Monitor the Service**: Ensure that the Jenkins agent service is running with the following command:
   
   ```bash
   sudo systemctl status node_script.sh
   ```

This configuration ensures that the Jenkins agent is always online and ready to execute pipeline stages, even if the instance restarts.

## Jenkins Pipeline

The Jenkins pipeline automates the entire build and deployment process. It is designed to pull the latest code from GitHub, build a Docker image, push it to Docker Hub, and finally launch the application in a Docker container.

### Adding a Docker Build Job in Jenkins

To automate the Docker image creation within Jenkins, follow these steps to set up a Docker build job:

1. **Access Jenkins Dashboard**: Log in to your Jenkins dashboard.
2. **Create a New Job**:
   - Click on "New Item" on the Jenkins dashboard.
   - Enter a name for your job, e.g., `flask-docker-build`.
   - Select "Pipeline" as the project type and click "OK."
3. **Configure the Job**:
   - In the "Pipeline" section, select "Pipeline script from SCM."
   - Choose "Git" as the SCM and provide the repository URL: `https://github.com/prateekmudgal/flask_app_docker_jenkins_sonarqube.git`.
   - Set the branch to `main` or any specific branch you want to track.
   - Ensure the "Jenkinsfile" path is correct (it should be at the root of the repository).
4. **Add Build Trigger**:
   - Optionally, you can set up a trigger under "Build Triggers" to automatically start the job when changes are detected in the repository.
5. **Save and Run the Job**:
   - Save the configuration and manually trigger the job by clicking "Build Now."
   - Monitor the console output to verify the Docker image is built successfully.

### Jenkins Master-Slave Architecture

In this setup, Jenkins is configured in a master-slave (master-agent) architecture:

- **Jenkins Master**: The control node that schedules builds.
- **Jenkins Slave (Agent)**: The node where all stages of the pipeline are executed. This node runs the Docker engine and handles building and deploying the application.

### Pipeline Stages

Here's a detailed description of each stage in the Jenkins pipeline:

#### Jenkinsfile Configuration

Below is the complete Jenkinsfile configuration, including all the stages:

```groovy
pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github',
                    url: 'https://github.com/prateekmudgal/flask_app_docker_jenkins_sonarqube.git'
            }
        }

        stage('Docker Build') {
            agent {
                label 'dockerengine'
            }
            steps {
                sh 'docker build -t prateek0912/sample-python:latest .'
            }
        }

        stage('Docker Push') {
            agent {
                label 'dockerengine'
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh "docker login -u ${DOCKER_USERNAME

} -p ${DOCKER_PASS}"
                    sh 'docker push prateek0912/sample-python:latest'
                }
            }
        }

        stage('Container Launch') {
            agent {
                label 'dockerengine'
            }
            steps {
                sh 'docker run -d -p 7077:5000 prateek0912/sample-python:latest'
            }
        }
    }
}
```

#### Stage Descriptions

- **Git Checkout**
  - **Purpose**: Clones the latest code from the GitHub repository.
  - **Agent**: Executes on the Jenkins master node.
  - **Action**: Clones the repository and checks out the `main` branch.

- **Docker Build**
  - **Purpose**: Builds the Docker image for the Flask application.
  - **Agent**: Executes on the Jenkins Agent node labeled `dockerengine`.
  - **Action**: Runs `docker build` to create the Docker image tagged as `prateek0912/sample-python:latest`.

- **Docker Push**
  - **Purpose**: Pushes the built Docker image to Docker Hub.
  - **Agent**: Executes on the Jenkins Agent node labeled `dockerengine`.
  - **Action**:
    - Logs into Docker Hub using provided credentials.
    - Pushes the Docker image `prateek0912/sample-python:latest` to Docker Hub.

- **Container Launch**
  - **Purpose**: Launches the Docker container with the Flask application.
  - **Agent**: Executes on the Jenkins Agent node labeled `dockerengine`.
  - **Action**:
    - Runs `docker run` to launch the container, mapping the host port `7077` to the container port `5000`.![Screenshot (248)](https://github.com/user-attachments/assets/a4ad840d-87f7-4e74-91be-c8b07a264a1e)

    - ![image](https://github.com/user-attachments/assets/06fd2c95-0888-4bc2-871e-2d90106e8ae8)

    - 
      

## Conclusion

This project successfully demonstrates a fully automated CI/CD pipeline using Jenkins and Docker. By configuring the Jenkins agent as a service, it ensures continuous availability and resilience, even in the event of system restarts. Additionally, by incorporating the Docker build job directly into Jenkins, the process is streamlined, making deployment more efficient and less prone to errors.

---

This revised README now includes details on setting up a Docker build job in Jenkins, as well as the previous addition of running the Jenkins agent as a service. The document provides a comprehensive guide to setting up the project and automating the build and deployment processes.
