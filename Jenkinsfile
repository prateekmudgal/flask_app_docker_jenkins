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

        stage('Sonarqube') {
            agent {
                label 'dockerengine'
            }
            environment {
                scannerHome = tool 'SonarQubeScanner'
            }
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
    }
}
