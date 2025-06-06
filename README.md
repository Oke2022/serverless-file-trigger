# serverless-file-trigger

📁 Serverless File Upload Trigger with AWS Lambda, S3, API Gateway, Terraform & Jenkins
This project demonstrates a serverless architecture where a Lambda function is triggered when a file is uploaded to an S3 bucket. Additionally, the Lambda function is accessible via a public HTTP endpoint using API Gateway. All infrastructure is provisioned using Terraform, and the Lambda deployment is automated with Jenkins or GitHub Actions.

🛠️ Features
🗂️ S3 Bucket: Stores uploaded files and triggers events.

🧠 Lambda Function: Executes on file upload or HTTP request.

🛡️ IAM Roles: Secure permissions for Lambda and S3 access.

🌐 API Gateway: Provides a public HTTP endpoint to invoke the Lambda.

⚙️ Terraform: Manages the full infrastructure as code.

🚀 CI/CD: Lambda is deployed automatically via Jenkins or GitHub Actions.

🧪 Use Cases
Triggering automated processing or alerts when a file is uploaded to S3

Serverless file ingestion pipelines

Exposing a lightweight API without provisioning EC2 instances

📦 Folder Structure

serverless-file-trigger/
│
├── terraform/                # Terraform IAC code for S3, Lambda, IAM, API Gateway
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│
│
├── lambda/                   # Lambda source code
│   └── handler.py
│
├── jenkins/ or .github/      # CI/CD config (Jenkinsfile or GitHub Actions workflow)
│
└── README.md
⚙️ Setup & Deployment
1. Clone the Repository

git clone https://github.com/Oke2022/serverless-file-trigger.git
cd serverless-file-trigger/terraform
2. Configure AWS Credentials
Ensure AWS credentials are configured (via CLI, environment variables, or an IAM role).

3. Initialize Terraform

terraform init
4. Deploy Infrastructure

terraform apply
This provisions:

S3 bucket

Lambda function with correct permissions

API Gateway endpoint

IAM roles

5. Upload a File to Trigger Lambda
Upload a file to the created S3 bucket manually or via CLI:

aws s3 cp lambdaTest.txt s3://<your-bucket-name>/
6. Access Lambda via HTTP
Visit the API Gateway endpoint:

https://<api-id>.execute-api.<region>.amazonaws.com/prod/invoke
✅ Example Output
S3 Trigger
When a file is uploaded, the Lambda logs:


File uploaded: lambdaTest.txt
Bucket: my-serverless-bucket
Size: 29 bytes
API Gateway Call
Calling the public URL returns:

Hello from Lambda via API Gateway!
🚀 CI/CD with Jenkins or GitHub Actions
Set up a Jenkins pipeline or GitHub Actions workflow to zip and deploy lambda/handler.py to the function.

Use the AWS CLI or Terraform for updates.

Example step:

zip function.zip handler.py
aws lambda update-function-code --function-name myLambda --zip-file fileb://function.zip
📚 Technologies Used
AWS S3

AWS Lambda

AWS API Gateway

AWS IAM

Terraform

Jenkins / GitHub Actions

Python 3.11

🙌 Author
Joshua Oke

Feel free to connect or reach out if you want to collaborate or learn more about this project!
