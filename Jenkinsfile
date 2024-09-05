pipeline {
    agent {
        label "application"
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
                label "application"
            }
            steps {
                sh 'sudo docker build -t prateek0912/oriserve:latest .'
            }
        }

        stage('Docker Push') {
            agent {
                label "application"
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh "docker login -u ${DOCKER_USERNAME} --password-stdin"
                    sh 'sudo docker push prateek0912/oriserve:latest'
                }
            }
        }

        stage('Container Launch') {
            agent {
                label "application"
            }
            steps {
                sh 'sudo docker run -d -p 7077:5000 prateek0912/oriserve'
            }
        }
    }
}
