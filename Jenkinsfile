pipeline {
  agent any

  environment {
    AWS_REGION = 'us-east-2'
    AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
    AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
  }

  parameters {
    booleanParam(name: 'DESTROY_INFRA', defaultValue: false, description: 'Destroy Terraform Infrastructure?')
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
          sh 'zip ../terraform/function.zip handler.py'
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
      when {
        expression { !params.DESTROY_INFRA }
      }
      steps {
        dir('terraform') {
          sh 'terraform apply -auto-approve'
        }
      }
    }

    stage('Terraform Destroy') {
      when {
        expression { params.DESTROY_INFRA }
      }
      steps {
        dir('terraform') {
          sh 'terraform destroy -auto-approve'
        }
      }
    }
  }

  post {
    success {
      script {
        if (params.DESTROY_INFRA) {
          echo "✅ Terraform resources destroyed successfully!"
        } else {
          echo "✅ Terraform applied successfully!"
        }
      }
    }
    failure {
      echo "❌ Terraform operation failed."
    }
  }
}

