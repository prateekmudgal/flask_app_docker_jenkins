pipeline {
    agent any
     
    
    stages {
        stage('Git Checkout'){
            steps{
                 git branch: 'main', credentialsId: 'github', url: 'https://github.com/prateekmudgal/flask_app_docker_jenkins_sonarqube.git'
                 }
             }
        stage('Sonarqube') {
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
    




