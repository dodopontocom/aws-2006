import json

def lambda_handler(event, context):
    for record in event['Records']:
        # Process each message
        body = record['body']
        print(f"Received message: {body}")

    return {
        'statusCode': 200,
        'body': json.dumps('Messages processed successfully!')
    }