pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            dir 'jenkins'
        }
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://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@github.com/avihaycognyte/WorldOfGames2.git'
            }
        }
        stage('Build Application Docker Image') {
            steps {
                script {
                    sh 'echo Building Application Docker Image...'
                    sh 'docker build -t avihaycognyte/WorldOfGames2:1.0 apps/'
                    sh 'docker images avihaycognyte/WorldOfGames2:1.0'
                }
            }
        }
        stage('Run Application') {
            steps {
                script {
                    sh 'echo Running Application...'
                    sh 'docker run --name WorldOfGames2 --detach --rm --publish 8777:8777 --env FLASK_APP=MainScores.py --env FLASK_RUN_HOST=0.0.0.0 --env FLASK_RUN_PORT=8777 avihaycognyte/WorldOfGames2:1.0'
                    sh 'docker ps -f "name=WorldOfGames2"'
                }
            }
        }
        stage('Test Application') {
            steps {
                script {
                    sh 'echo Testing Application...'
                    sh 'docker exec -i WorldOfGames2 sh -c "python e2e.py"'
                }
            }
        }
        stage('Push Docker Image') {
            environment {
                DOCKER_TOKEN = credentials('docker_hub_token')
            }
            steps {
                script {
                    sh 'echo Pushing Docker Image...'
                    sh 'docker login -u avihaycognyte -p $DOCKER_TOKEN'
                    sh 'docker push avihaycognyte/WorldOfGames2:1.0'
                }
            }
        }
        stage('Clear Environment') {
            steps {
                script {
                    sh 'echo Clearing Environment...'
                    sh 'docker stop WorldOfGames2'
                    sh 'docker rmi avihaycognyte/WorldOfGames2:1.0'
                }
            }
        }
    }
}
