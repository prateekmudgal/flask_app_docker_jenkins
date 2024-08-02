pipeline {
    agent any
    
    stages {
        stage('Git Checkout'){
            steps{
                 git branch: 'main', credentialsId: 'github', url: 'https://github.com/prateekmudgal/flask_app_docker_jenkins_sonarqube.git'
           }
        }
        stage("build & SonarQube analysis")steps {
              withSonarQubeEnv('My SonarQube Server') {
                sh 'mvn clean package sonar:sonar'
              }
        }
        stage("Quality Gate") {
            steps {
              timeout(time: 1, unit: 'HOURS') {
                waitForQualityGate abortPipeline: true
              }
            }
          }
    }
}



