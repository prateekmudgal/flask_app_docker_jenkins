pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from GitHub using credentials
                git credentialsId: 'github-credentials-id',
                    url: 'https://github.com/prateekmudgal/flask_app_docker_jenkins_sonarqube.git',
                    branch: 'main'
                    }
                  }
       
        
        
    }
}
