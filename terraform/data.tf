data "archive_file" "python_lambda_package" {
  type        = "zip"
  source_dir  = "./files/"
  output_path = "./files/lambda.zip"
}