resource "aws_lambda_event_source_mapping" "lambda_trigger" {
  event_source_arn = aws_sqs_queue.myQ.arn
  function_name    = aws_lambda_function.lambda.arn
  batch_size       = 5
}

resource "aws_lambda_permission" "sqs_invoke_lambda" {
  statement_id  = "AllowSQSToInvokeLambda"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda.arn
  principal     = "sqs.amazonaws.com"
  source_arn    = aws_sqs_queue.myQ.arn
}