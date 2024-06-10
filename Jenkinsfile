pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('your-dockerhub-credentials-id') // Set up your DockerHub credentials in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/avihaycognyte/WorldOfGames2.git', branch: 'master'
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build('flask-scores-app')
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
                        flaskApp.push('your-dockerhub-username/flask-scores-app:latest')
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
            cleanWs()
        }
    }
}
