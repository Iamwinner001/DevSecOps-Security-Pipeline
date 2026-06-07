# Configure these backend resources before running terraform init.
# The S3 bucket should have versioning, encryption, access logging, and public access blocks enabled.
terraform {
  backend "s3" {
    bucket         = "devsecops-security-pipeline-tfstate"
    key            = "dev/devsecops-security-pipeline.tfstate"
    region         = "us-east-1"
    dynamodb_table = "devsecops-security-pipeline-locks"
    encrypt        = true
  }
}
