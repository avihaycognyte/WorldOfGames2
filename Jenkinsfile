pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('your-dockerhub-credentials-id') // Replace with your DockerHub credentials ID
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://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@github.com/avihaycognyte/WorldOfGames2.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                sh 'echo Building Docker image...'
                sh 'docker build -t flask-scores-app .'
            }
        }

        stage('Run') {
            steps {
                sh 'echo Running Docker container...'
                sh '''
                    docker run --name flask-scores-app --detach --rm --publish 8777:5000 \
                    -v $WORKSPACE/Scores.txt:/app/Scores.txt \
                    flask-scores-app sh -c '
                    if [ ! -f /app/Scores.txt ]; then
                        echo 0 > /app/Scores.txt;
                    fi;
                    exec flask run --host=0.0.0.0'
                '''
                // Wait for the container to start
                sleep 10
            }
        }

        stage('Test') {
            steps {
                sh 'echo Running end-to-end tests...'
                script {
                    def status = sh(script: "docker exec flask-scores-app python3 e2e.py http://localhost:8777", returnStatus: true)
                    if (status != 0) {
                        error('End-to-end tests failed')
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                sh 'echo Finalizing...'
                sh 'docker stop flask-scores-app'
                sh 'docker tag flask-scores-app:latest your-dockerhub-username/flask-scores-app:latest' // Replace with your DockerHub username
                sh 'docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW'
                sh 'docker push your-dockerhub-username/flask-scores-app:latest' // Replace with your DockerHub username
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
