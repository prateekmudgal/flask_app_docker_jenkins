

---

# Flask App Dockerized with Jenkins and SonarQube

This repository contains a sample Flask application that is fully Dockerized and integrated with Jenkins for automated CI/CD pipelines. Additionally, it uses SonarQube for static code analysis, ensuring code quality and maintainability. This project also demonstrates a Jenkins master-slave architecture where all stages are executed on the agent node.

## Table of Contents

- [Flask App Dockerized with Jenkins and SonarQube](#flask-app-dockerized-with-jenkins-and-sonarqube)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Setup and Installation](#setup-and-installation)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
      - [Clone the Repository](#clone-the-repository)
  - [Manual Docker Operations](#manual-docker-operations)
    - [Build Docker Image Manually](#build-docker-image-manually)
    - [Run Docker Container Manually](#run-docker-container-manually)
  - [Jenkins Pipeline](#jenkins-pipeline)
    - [Jenkins Master-Slave Architecture](#jenkins-master-slave-architecture)
    - [Pipeline Stages](#pipeline-stages)
      - [Jenkinsfile Configuration](#jenkinsfile-configuration)
    - [Stage Descriptions](#stage-descriptions)

## Project Overview

This Proof of Concept (POC) demonstrates the deployment of a sample Flask application using Docker containers. The application leverages Jenkins for Continuous Integration and Continuous Deployment (CI/CD), with SonarQube integrated for continuous code quality analysis.

The objective of this project is to showcase the integration of Jenkins, Docker, and SonarQube, and how they can be used together to automate the build, test, and deployment processes.

## Features

- **Flask Application**: A basic web application built with Flask.
- **Dockerized Environment**: Containerization of the Flask app using Docker.
- **Jenkins Integration**: Automated CI/CD pipeline utilizing Jenkins.
- **SonarQube Analysis**: Integration with SonarQube for static code analysis.
- **Jenkins Master-Slave Architecture**: Distributed build environment with Jenkins agents.
- **Manual Docker Operations**: Option to manually build and run Docker containers.



## Setup and Installation

### Prerequisites

Before starting, ensure you have the following installed:

- **Docker**: [Installation Guide](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Installation Guide](https://docs.docker.com/compose/install/)
- **Jenkins**: [Installation Guide](https://www.jenkins.io/doc/book/installing/)
- **SonarQube**: [Installation Guide](https://docs.sonarqube.org/latest/setup/get-started-2-minutes/)
- **Git**: [Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Installation

#### Clone the Repository

```bash
git clone https://github.com/prateekmudgal/flask_app_docker_jenkins_sonarqube.git
cd flask_app_docker_jenkins_sonarqube
```


- **Access the Application**

  Open your browser and navigate to `http://localhost:7077` to see the Flask application in action.

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

## Jenkins Pipeline

The Jenkins pipeline automates the entire build and deployment process. It is designed to pull the latest code from GitHub, analyze it using SonarQube, build a Docker image, push it to Docker Hub, and finally launch the application in a Docker container.

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

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeScanner') {
                    sh 'sonar-scanner \
                       -Dsonar.projectKey=my_project \
                       -Dsonar.sources=. \
                       -Dsonar.host.url=http://3.20.232.183:9990'
                }
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
                    sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASS}"
                    sh 'docker push prateek0912/sample-python:latest'
                }
            }
        }

        stage('Container Launch') {
            agent {
                label 'dockerengine'
            }
            steps {
                sh 'docker run -d -p 7077:5000 prateek0912/sample-python'
            }
        }
    }
}
```

### Stage Descriptions

- **Stage 1: Git Checkout**
  - **Purpose**: Fetches the latest code from the GitHub repository.
  - **Action**: 
    - Clones the `main` branch using the specified GitHub credentials.
    - Ensures that the latest code is always used for the build process.

- **Stage 2: SonarQube Analysis**
  - **Purpose**: Performs static code analysis using SonarQube.
  - **Action**: 
    - Uses `sonar-scanner` to analyze the code.
    - Configured with a project key (`my_project`) and SonarQube server URL.
    - Provides feedback on code quality and vulnerabilities.
  
- **Stage 3: Docker Build**
  - **Purpose**: Builds the Docker image for the Flask application.
  - **Agent**: Executes on the Jenkins Agent node labeled `dockerengine`.
  - **Action**: 
    - Runs `docker build` to create the Docker image.
    - Tags the image as `prateek0912/sample-python:latest`.

- **Stage 4: Docker Push**
  - **Purpose**: Pushes the Docker image to Docker Hub.
  - **Agent**: Executes on the Jenkins Agent node labeled `dockerengine`.
  - **Action**: 
    - Authenticates with Docker Hub using Jenkins credentials.
    - Pushes the image to the repository `prateek0912/sample-python`.

- **Stage 5: Container Launch**
  - **Purpose**: Launches the Flask application in a Docker container.
  - **Agent**: Executes on the Jenkins Agent node labeled `dockerengine`.
  - **Action**: 
    - Runs `docker run` to start the container.
    - Maps port `7077` on the host to port `5000` in the container.

