pipeline {
  agent any

  environment {
    ORDER_SERVICE_TAG = "${BUILD_NUMBER}"
    USER_SERVICE_TAG = "${BUILD_NUMBER}"
  }

  stages {
    
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Test') {
      steps {
        sh 'python /services/order-service/test/test.py'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t order-service:${ORDER_SERVICE_TAG} ./services/order-service/'
        sh 'docker build -t user-service:${USER_SERVICE_TAG} ./services/user-service/'
      }
    }

    stage('Deploy to k8s') {
      steps {
        sh """
          kubectl set image deployment/order-deployment \
          order-service=order-service:${ORDER_SERVICE_TAG}
          kubectl set image deployment/user-deployment \
          user-service=user-service:${USER_SERVICE_TAG}
          """
      }
    }

    }

  }
}
