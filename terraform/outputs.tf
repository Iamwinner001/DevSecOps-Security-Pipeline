output "vpc_id" {
  description = "ID of the deployed VPC."
  value       = aws_vpc.main.id
}

output "public_subnet_id" {
  description = "ID of the public subnet."
  value       = aws_subnet.public.id
}

output "private_subnet_id" {
  description = "ID of the private subnet."
  value       = aws_subnet.private.id
}

output "app_instance_id" {
  description = "ID of the EC2 application instance."
  value       = aws_instance.app.id
}

output "logs_bucket_name" {
  description = "Encrypted S3 bucket used for application/security logs."
  value       = aws_s3_bucket.logs.bucket
}
