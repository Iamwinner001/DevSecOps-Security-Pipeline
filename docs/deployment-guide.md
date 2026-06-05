# Deployment Guide

## 1. Prepare Jenkins

Install required tools on Jenkins agents:

- Terraform 1.6 or newer
- Python 3.11
- Docker
- Checkov
- Bandit
- OWASP Dependency Check CLI
- SonarScanner CLI

Install Jenkins plugins:

- Pipeline
- HTML Publisher
- SonarQube Scanner
- Pipeline Utility Steps
- AWS Credentials
- Slack Notification or Email Extension

## 2. Configure Credentials

Create these Jenkins credentials:

| Credential ID | Type | Purpose |
| --- | --- | --- |
| `aws-devsecops-deploy` | AWS access key | Terraform plan/apply and application deployment |
| `sonarqube-token` | Secret text | SonarQube scanner authentication |

The AWS principal should be limited to the target account and deployment role permissions required for VPC, EC2, S3, IAM, and security group management.

## 3. Configure Terraform Backend

Before running the pipeline, create the remote state bucket and lock table:

```bash
aws s3api create-bucket \
  --bucket devsecops-security-pipeline-tfstate \
  --region us-east-1

aws dynamodb create-table \
  --table-name devsecops-security-pipeline-locks \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```

Enable bucket versioning, encryption, and public access blocks for the backend bucket.

## 4. Configure SonarQube

Create a SonarQube project:

- Project key: `devsecops-security-pipeline`
- Quality gate: fail on blocker/critical issues, security hotspot review required
- Token stored as Jenkins credential `sonarqube-token`

In Jenkins global configuration, create a SonarQube server named `SonarQube`.

## 5. Run the Pipeline

1. Push the repository to GitHub.
2. Create a Jenkins multibranch pipeline or pipeline job.
3. Point Jenkins to `jenkins/Jenkinsfile`.
4. Run the build.
5. Review published HTML reports.
6. Approve Terraform Apply when running on `main`.

## 6. Expected Behavior

- Pull request builds run validation and scanning.
- Deployments are blocked if critical or high findings are present.
- Medium findings above threshold mark the build unstable.
- Reports are archived for audit and interview demonstration.

## 7. Production Hardening Recommendations

- Replace default AMI with a hardened enterprise golden AMI.
- Deploy the application to ECS or EKS instead of a demo EC2 host.
- Add container image scanning before deployment.
- Use AWS KMS customer-managed keys for S3 and EBS encryption.
- Send findings to Security Hub or a SIEM.
- Add branch protection requiring Jenkins success before merge.
