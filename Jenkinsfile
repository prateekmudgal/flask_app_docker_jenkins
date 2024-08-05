pipeline {
    agent any

    environment {     
        DOCKERHUB_CREDENTIALS = credentials('eafdc5b6-6653-4c0b-b069-d05e5819220e')     
    } 

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

        

       
    }
}
