pipeline {
    agent any  // Use this if you want to run on any agent

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id') // Replace with your DockerHub credentials ID in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://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@github.com/avihaycognyte/WorldOfGames2.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build('flask-scores-app', '.')
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    def flaskApp = docker.image('flask-scores-app')
                    flaskApp.run('-p 8777:5000 -v ${WORKSPACE}/Scores.txt:/Scores.txt')
                    sleep 10 // Wait for the service to start
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    def status = sh(script: "python3 e2e.py http://localhost:8777", returnStatus: true)
                    if (status != 0) {
                        error('End-to-end tests failed')
                    }
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'DOCKERHUB_CREDENTIALS') {
                        def flaskApp = docker.image('flask-scores-app')
                        flaskApp.push('avihaycognyte/flask-scores-app:latest')
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                sh "docker ps -q --filter 'ancestor=flask-scores-app' | xargs -r docker stop"
                sh "docker ps -a -q --filter 'ancestor=flask-scores-app' | xargs -r docker rm"
            }
        }
        cleanup {
            cleanWs()  // Clean workspace without requiring a specific agent
        }
    }
}
