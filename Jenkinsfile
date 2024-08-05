pipeline {
    agent any

    environment {     
        DOCKERHUB_CREDENTIALS = credentials('prateek0912')     
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

        stage('Login to Docker Hub') {
            agent {
                label 'dockerengine'
            }
            steps {       
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'                		
                echo 'Login Completed'      
            }           
        }

        stage('Push Image to Docker Hub') {
            agent {
                label 'dockerengine'
            }
            steps {                            
                sh 'sudo docker push prateek0912/sample-python:$BUILD_NUMBER'           
                echo 'Push Image Completed'       
            }            
        }
    }
}
