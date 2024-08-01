pipeline {
    agent any
    
    environment {
        // Define environment variables
        DOCKERHUB_CREDENTIALS = 'dockerhub-creds'
        SONARQUBE_SERVER = 'SonarQubeServer' // Use the ID you set in Jenkins
        DOCKER_IMAGE = 'your-dockerhub-username/your-image-name'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                git url: 'https://github.com/your-username/your-repo.git', branch: 'main'
            }
        }
        
        stage('Code Analysis') {
            steps {
                // Run SonarQube analysis
                script {
                    def scannerHome = tool 'SonarQube Scanner'
                    withSonarQubeEnv('SonarQubeServer') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                // Wait for SonarQube Quality Gate result
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Build Docker image
                script {
                    docker.build("$DOCKER_IMAGE:${env.BUILD_NUMBER}")
                }
            }
        }
        
        stage('Push Docker Image') {
            steps {
                // Push Docker image to Docker Hub
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKERHUB_CREDENTIALS) {
                        def image = docker.build("$DOCKER_IMAGE:${env.BUILD_NUMBER}")
                        image.push()
                        image.push('latest')
                    }
                }
            }
        }
        
        stage('Run Docker Container') {
            steps {
                // Run Docker container
                script {
                    sh "docker run -d -p 8080:80 $DOCKER_IMAGE:${env.BUILD_NUMBER}"
                }
            }
        }
    }
    
    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }
}
