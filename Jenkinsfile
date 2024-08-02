pipeline {
    agent any
     environment {
        SONARQUBE_SERVER = 'sonarqube-api' 
        GIT_REPO = 'https://github.com/prateekmudgal/flask_app_docker_jenkins_sonarqube.git' 
        SONARQUBE_PROJECT_KEY = 'flask_app_docker_jenkins_sonarqube'
        SONARQUBE_PROJECT_NAME = 'flask_app_docker_jenkins_sonarqube' 
        SONARQUBE_PROJECT_VERSION = '1.0'
    }
    
    stages {
        stage('Git Checkout'){
            steps{
                 git branch: 'main', credentialsId: 'github', url: 'https://github.com/prateekmudgal/flask_app_docker_jenkins_sonarqube.git'
           }
        }
         stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv("${"sonarqube-api"}) {
                        sh "sonar-scanner \
                            -Dsonar.projectKey=${'flask_app_docker_jenkins_sonarqube'} \
                            -Dsonar.projectName=${'flask_app_docker_jenkins_sonarqube'} \
                            -Dsonar.sources=. \
                            -Dsonar.language=python \
                            -Dsonar.sourceEncoding=UTF-8"
                    }
                }
            }
        }
       
    }
}



