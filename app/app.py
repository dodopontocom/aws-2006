import boto3, os

region = os.environ['TF_VAR_region']
account_id = os.environ['aws_account_id']
queue_name = os.environ['TF_VAR_queue_name']
queue_url = 'https://sqs.'+ region +'.amazonaws.com/' + account_id + '/' + queue_name

sqs = boto3.client('sqs', region_name=region)

message_body = '{"nome":"Elisa","idade":03}'

response = sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)
print(f'Mensagem enviada com sucesso! ID da mensagem: {response["MessageId"]}')