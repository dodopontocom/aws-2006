import boto3

region = 'sa-east-1'
sqs = boto3.client('sqs', region_name=region)
queue_url = 'https://sqs.sa-east-1.amazonaws.com/654654328943/q2'
message_body = '{"nome":"Thais","idade":22}'
response = sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)
print(f'Mensagem enviada com sucesso! ID da mensagem: {response["MessageId"]}')