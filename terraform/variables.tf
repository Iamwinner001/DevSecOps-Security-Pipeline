variable "project_name" {
  description = "Name used for AWS resource naming and tagging."
  type        = string
  default     = "devsecops-security-pipeline"
}

variable "environment" {
  description = "Deployment environment name."
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "test", "stage", "prod"], var.environment)
    error_message = "Environment must be one of dev, test, stage, or prod."
  }
}

variable "aws_region" {
  description = "AWS region for deployment."
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC."
  type        = string
  default     = "10.20.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR block for public subnet."
  type        = string
  default     = "10.20.1.0/24"
}

variable "private_subnet_cidr" {
  description = "CIDR block for private subnet."
  type        = string
  default     = "10.20.2.0/24"
}

variable "allowed_ssh_cidr" {
  description = "CIDR allowed to reach SSH. Use a corporate VPN CIDR in production."
  type        = string
  default     = "10.0.0.0/8"
}

variable "instance_type" {
  description = "EC2 instance type."
  type        = string
  default     = "t3.micro"
}

variable "ami_id" {
  description = "Approved hardened AMI ID. Replace with golden AMI from enterprise image pipeline."
  type        = string
  default     = "ami-0c02fb55956c7d316"
}
