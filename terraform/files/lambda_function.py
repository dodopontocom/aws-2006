import json, telegram, os

def lambda_handler(event, context):
    for record in event['Records']:
        body = record['body']
        print(f"Mensagem recebida: {body}")
    
    bot_token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(token=bot_token)

    bot.send_message(chat_id=chat_id, text=f"Processamento bem-sucedido: {body}")

    return {
        'statusCode': 200,
        'body': json.dumps('Messages processed com sucesso!')
    }
#
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