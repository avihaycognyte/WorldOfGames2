pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
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
                    docker.image('flask-scores-app').withRun('-p 8777:5000 -v ${WORKSPACE}/Scores.txt:/Scores.txt') { c ->
                        sh 'sleep 10'  // Wait for the service to start
                    }
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

        stage('Finalize') {
            steps {
                script {
                    def img = docker.image('flask-scores-app')
                    img.push('your-dockerhub-username/flask-scores-app:latest')
                }
            }
        }
    }

    post {
        always {
            script {
                docker.image('flask-scores-app').withRun() { c ->
                    sh "docker stop ${c.id}"
                }
            }
        }
    }
}
