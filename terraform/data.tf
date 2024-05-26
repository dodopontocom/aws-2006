data "archive_file" "python_lambda_package" {  
  type = "zip"  
  source_file = "./files/lambda_function.py" 
  output_path = "./files/lambda.zip"
}