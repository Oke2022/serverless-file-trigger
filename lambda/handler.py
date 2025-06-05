import json

def lambda_handler(event, context):
    print("Event:", event)
    file_name = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    return {
        'statusCode': 200,
        'body': json.dumps(f"File {file_name} uploaded to {bucket}")
    }

