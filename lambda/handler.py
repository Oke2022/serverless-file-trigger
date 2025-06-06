def lambda_handler(event, context):
    print("Event:", event)

    # Extract file name
    try:
        file_name = event['Records'][0]['s3']['object']['key']
        print(f"File uploaded: {file_name}")
    except KeyError:
        print("No file info found in event.")

    return {
        'statusCode': 200,
        'body': 'S3 trigger worked!'
    }

