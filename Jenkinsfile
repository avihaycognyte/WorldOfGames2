pipeline {
    agent any

    stages {
        stage('Setup Docker') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            if ! [ -x "$(command -v docker)" ]; then
                                echo "Docker is not installed. Installing Docker..."
                                if [ -x "$(command -v apt-get)" ]; then
                                    apt-get update || true
                                    apt-get install -y docker.io || true
                                elif [ -x "$(command -v yum)" ]; then
                                    yum update -y
                                    yum install -y docker || true
                                    systemctl start docker || true
                                    systemctl enable docker || true
                                else
                                    echo "Package manager not supported. Please install Docker manually."
                                    exit 1
                                fi
                                usermod -aG docker jenkins || true
                            else
                                echo "Docker is already installed."
                            fi
                        '''
                    } else {
                        echo "Docker installation script is not supported on non-Unix systems."
                    }
                }
            }
        }

        stage('Checkout') {
            steps {
                git url: 'https://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@github.com/avihaycognyte/WorldOfGames2.git', branch: 'main'
            }
        }

        stage('Check Scores.txt') {
            steps {
                script {
                    def scoresFile = "${env.WORKSPACE}/Scores.txt"
                    if (!fileExists(scoresFile)) {
                        writeFile file: 'Scores.txt', text: '0'
                    }
                }
            }
        }

        stage('Build') {
            steps {
                sh 'echo Building...'
                sh 'docker build -t flask-scores-app .'
                sh 'docker images flask-scores-app'
            }
        }

        stage('Run') {
            steps {
                sh 'echo Running...'
                sh 'docker run --name flask-scores-app --detach --rm --publish 8777:5000 --volume $WORKSPACE/Scores.txt:/Scores.txt flask-scores-app || { echo "Error running container"; docker logs flask-scores-app; exit 1; }'
                sh 'docker ps -f "name=flask-scores-app"'
                sleep 10 // Wait for the service to start
            }
        }

        stage('Test') {
            steps {
                sh 'echo Testing...'
                script {
                    def status = sh(script: "python3 e2e.py http://localhost:8777", returnStatus: true)
                    if (status != 0) {
                        error('End-to-end tests failed')
                    }
                }
            }
        }

        stage('Clear') {
            steps {
                sh 'echo Clearing...'
                sh 'docker stop flask-scores-app'
                sh 'docker rmi flask-scores-app'
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
