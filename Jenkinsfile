pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/prateekmudgal/flask_app_docker_jenkins_sonarqube.git'
            }
        }

        stage('Docker Build') {
            agent { 
                label 'docker'
            }

            steps {
                sh 'docker build -t simple-flask-app:latest .'
            }
        }
    }
}
