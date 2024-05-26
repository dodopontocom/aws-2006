resource "aws_sqs_queue" "myQ" {
  name                      = var.queue_name
}
