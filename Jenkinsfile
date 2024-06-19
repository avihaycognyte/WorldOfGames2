pipeline {
    agent {
        dockerfile {
            filename 'jenkins/Dockerfile'
            dir 'jenkins'
        }
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'github.com/avihaycognyte/WorldOfGames2.git'
            }
        }
        stage('Build Application Docker Image') {
            steps {
                script {
                    sh 'echo Building Application Docker Image...'
                    sh 'docker build -t your_dockerhub_username/your_project:1.0 app/'
                    sh 'docker images your_dockerhub_username/your_project:1.0'
                }
            }
        }
        stage('Run Application') {
            steps {
                script {
                    sh 'echo Running Application...'
                    sh 'docker run --name your_project --detach --rm --publish 8777:8777 --env FLASK_APP=your_flask_app --env FLASK_RUN_HOST=0.0.0.0 --env FLASK_RUN_PORT=8777 your_dockerhub_username/your_project:1.0'
                    sh 'docker ps -f "name=your_project"'
                }
            }
        }
        stage('Test Application') {
            steps {
                script {
                    sh 'echo Testing Application...'
                    sh 'docker exec -i your_project sh -c "python your_test_script.py"'
                }
            }
        }
        stage('Push Docker Image') {
            environment {
                DOCKER_TOKEN = 'your_docker_hub_token'
            }
            steps {
                script {
                    sh 'echo Pushing Docker Image...'
                    sh 'docker login -u your_dockerhub_username -p $DOCKER_TOKEN'
                    sh 'docker push your_dockerhub_username/your_project:1.0'
                }
            }
        }
        stage('Clear Environment') {
            steps {
                script {
                    sh 'echo Clearing Environment...'
                    sh 'docker stop your_project'
                    sh 'docker rmi your_dockerhub_username/your_project:1.0'
                }
            }
        }
    }
}
