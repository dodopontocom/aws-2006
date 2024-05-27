import json, telegram, os

def lambda_handler(event, context):
    sqs_message = json.loads(event['Records'][0]['body'])
    message_body = sqs_message['Message']

    bot_token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(token=bot_token)

    bot.send_message(chat_id=chat_id, text=f"Processamento bem-sucedido: {message_body}")

    return {
        'statusCode': 200,
        'body': json.dumps('Mensagem enviada com sucesso para o bot do Telegram!')
    }

# def lambda_handler(event, context):
#     for record in event['Records']:
#         # Process each message
#         body = record['body']
#         print(f"Mensagem recebida: {body}")

#     return {
#         'statusCode': 200,
#         'body': json.dumps('Messages processed com sucesso!')
#     }

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