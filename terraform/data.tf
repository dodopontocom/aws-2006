data "archive_file" "python_lambda_package" {
  depends_on = [null_resource.install_dependencies]
  excludes   = [
    "__pycache__",
    "venv",
  ]
  type        = "zip"
  source_dir  = "./files/"
  output_path = "./files/lambda.zip"
}