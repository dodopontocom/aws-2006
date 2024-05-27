import json

def lambda_handler(event, context):
    for record in event['Records']:
        # Process each message
        body = record['body']
        print(f"Mensagem recebida: {body}")

    return {
        'statusCode': 200,
        'body': json.dumps('Messages processed com sucesso!')
    }

# def lambda_handler(event, context):
#     for message in event['Records']:
#         process_message(message)
#     print("done")

# def process_message(message):
#     try:
#         print(f"Processed message {message['body']}")
#         # TODO: Do interesting work based on the new message
#     except Exception as err:
#         print("An error occurred")
#         raise err