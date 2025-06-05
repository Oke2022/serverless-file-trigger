def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello! You reached the API Gateway-triggered Lambda!"
    }

