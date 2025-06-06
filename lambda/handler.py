def lambda_handler(event, context):
    print("Event:", event)

    # Extract file name
    try:
        file_name = event['Records'][0]['s3']['object']['key']
        print(f"File uploaded: {file_name}")
        print(f"Bucket: {event['Records'][0]['s3']['bucket']['name']}")
        print(f"Size: {event['Records'][0]['s3']['object']['size']} bytes")

    except KeyError:
        print("No file info found in event.")

    return {
        'statusCode': 200,
        'body': 'S3 trigger worked!'
    }

