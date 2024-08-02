pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/prateekmudgal/flask_app_docker_jenkins_sonarqube.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker Image
                    sh 'docker build -t flask-app .'
                }
            }
        }

        stage('Run SonarQube Analysis') {
            environment {
                scannerHome = tool 'SonarQube Scanner'
            }
            steps {
                script {
                    // Run SonarQube analysis
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('Deploy Docker Container') {
            steps {
                script {
                    // Run Docker Container
                    sh 'docker run -d -p 5000:5000 flask-app'
                }
            }
        }
    }

    
}
