pipeline {
  agent any

  environment {
    AWS_REGION = 'us-east-2'
    AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
    AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
  }

  stages {
    stage('Checkout Code') {
      steps {
        checkout scm
      }
    }

    stage('Zip Lambda Function') {
      steps {
        dir('lambda') {
          sh 'zip function.zip handler.py'
          sh 'mv function.zip ../terraform/'
        }
      }
    }

    stage('Terraform Init') {
      steps {
        dir('terraform') {
          sh 'terraform init'
        }
      }
    }

    stage('Terraform Apply') {
      steps {
        dir('terraform') {
          sh 'terraform apply -auto-approve'
        }
      }
    }
  }

  post {
    success {
      echo "✅ Terraform applied successfully!"
    }
    failure {
      echo "❌ Terraform apply failed."
    }
  }
}

