pipeline {
  agent any
  environment {
    IMAGE_NAME = "my-flask-app:${env.BUILD_NUMBER}"
  }
  stages {
    stage('Checkout SCM') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        // Use sh on Linux nodes
        script {
          if (isUnix()) {
            echo "Building Docker image on Unix node..."
            sh "docker build -t ${IMAGE_NAME} ."
          } else {
            echo "Building Docker image on Windows node..."
            bat "docker build -t ${IMAGE_NAME} ."
          }
        }
      }
    }

    stage('Stop Old Container') {
      steps {
        script {
          if (isUnix()) {
            // stop previous container if exists
            sh '''
              if docker ps -a --format '{{.Names}}' | grep -q '^my-flask-app$'; then
                docker stop my-flask-app || true
                docker rm my-flask-app || true
              fi
            '''
          } else {
            bat '''
              powershell -Command "if (docker ps -a --format '{{.Names}}' | Select-String '^my-flask-app$') { docker stop my-flask-app; docker rm my-flask-app }"
            '''
          }
        }
      }
    }

    stage('Run New Container') {
      steps {
        script {
          if (isUnix()) {
            sh "docker run -d --name login-form -p 5000:5000 ${IMAGE_NAME}"
          } else {
            bat "docker run -d --name login-form -p 5000:5000 ${IMAGE_NAME}"
          }
        }
      }
    }

    stage('Test Application') {
      steps {
        script {
          if (isUnix()) {
            // simple health-check; adjust path/port as needed
            sh 'sleep 3; curl -f http://localhost:5000/ || (echo "Health check failed" && exit 1)'
          } else {
            bat 'powershell -Command "Start-Sleep -s 3; Invoke-WebRequest -UseBasicParsing http://localhost:5000/ -ErrorAction Stop"'
          }
        }
      }
    }

    stage('Deploy Success') {
      steps {
        echo "Deployment completed. Image: ${IMAGE_NAME}"
      }
    }
  }

  post {
    failure {
      echo "Pipeline failed. Please check logs."
    }
    always {
      // Optional: cleanup older images
      script {
        if (isUnix()) {
          sh "docker image prune -f || true"
        } else {
          bat "docker image prune -f"
        }
      }
    }
  }
}
