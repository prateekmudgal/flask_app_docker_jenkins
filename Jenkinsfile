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
                sh 'docker build -t simple-flask-app:latest .'
            }
        }

        stage('Docker Push') {
            agent any
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'Prateek@9', usernameVariable: 'prateek0912')]) {
                    sh "docker login -u ${dockerHubUser} -p ${dockerHubPassword}"
                    sh 'docker push prateek0912/sample-python:latest'
                }
            }
        }
    }
}
