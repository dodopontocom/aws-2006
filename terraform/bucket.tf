data "terraform_remote_state" "existing_bucket" {
  backend = "s3"
  config = {
    bucket = var.tf_bucket_name
    key    = "terraform"
    region = var.region
  }
}

resource "aws_s3_bucket" "tf-bucket" {
  count  = data.terraform_remote_state.existing_bucket ? 0 : 1
  bucket = var.tf_bucket_name
}

resource "aws_s3_bucket_acl" "bucket_acl" {
  bucket = var.tf_bucket_name
  acl    = "private"
}