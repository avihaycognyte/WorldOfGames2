pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('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') // Set up your DockerHub credentials in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                sh "echo hello world"
            }
        }
    }
}
