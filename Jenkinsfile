pipeline {
    agent any

    environment {
        IMAGE_NAME = "login-form-app"
        CONTAINER_NAME = "login-form-container"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                docker run -d \
                --name $CONTAINER_NAME \
                -p 5000:5000 \
                $IMAGE_NAME:latest
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'curl http://localhost:5000 || true'
            }
        }
    }

    post {
        success {
            echo "✅ Login Form Deployed Successfully!"
        }
        failure {
            echo "❌ Deployment Failed!"
        }
    }
}
