pipeline {
    agent any
    
    stages {
        stage('Fetch Code') {
            steps {
                git 'https://github.com/prateekmudgal/flask_app_docker_jenkins_sonarqube.git'
            }
        }
        stage('Code Analysis') {
            environment {
                scannerHome = tool 'Sonar'
            }
            steps {
                script {
                    withSonarQubeEnv('Sonar') {
                        sh "${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey= 'flask_app_docker_jenkins_sonarqube' \
                            -Dsonar.projectName= 'flask_app_docker_jenkins_sonarqube' \
                            -Dsonar.sources:"
                    }
                }
            }
        }
    }
}
