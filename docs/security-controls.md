# Security Controls

## Control Summary

| Area | Control | Implementation |
| --- | --- | --- |
| IaC | Terraform validation | `terraform fmt`, `terraform validate` |
| IaC security | Checkov | Scans `terraform/` and publishes reports |
| SAST | Bandit | Scans Python files under `app/` |
| SCA | OWASP Dependency Check | Scans dependency manifests and installed packages |
| Quality | SonarQube | Enforces quality gate and security hotspot review |
| Deployment | Terraform | Provisions AWS with encryption and least privilege |
| Reporting | Jenkins | Archives security reports and publishes HTML |

## Security Gate Policy

The Jenkins security gate uses this policy:

| Severity | Action |
| --- | --- |
| Critical findings > 0 | Fail build |
| High findings > 0 | Fail build |
| Medium findings > 5 | Mark unstable and warn |
| Low findings | Report only |

This aligns with enterprise risk management practices: critical and high issues block production, medium findings require triage, and low findings remain visible for continuous improvement.

## Checkov

Checkov scans Terraform code for common AWS misconfigurations:

- public S3 buckets
- missing encryption
- overly permissive security groups
- disabled versioning
- insecure IAM policies
- weak EC2 metadata settings

The configuration is stored in `security/checkov.yml`.

## Bandit

Bandit scans Python source for insecure coding patterns. The intentionally vulnerable app demonstrates:

- hardcoded secrets
- shell command execution with user input
- Flask debug mode

The corrected version in `app/secure_app.py` removes those patterns.

## OWASP Dependency Check

Dependency Check identifies known CVEs in dependencies and fails builds when CVSS is equal to or above 7.

The configuration is stored in `security/dependency-check.properties`.

## SonarQube

SonarQube provides:

- code quality gate
- maintainability checks
- security hotspot workflow
- issue trend tracking
- branch and pull request analysis

The Jenkinsfile waits for the quality gate and aborts the pipeline on failure.

## AWS Security Best Practices

Terraform includes:

- encrypted EBS root volume
- S3 server-side encryption
- S3 versioning
- S3 public access blocking
- TLS-only S3 bucket policy
- IMDSv2 enforcement
- least-privilege IAM role for EC2
- restricted SSH access through a configurable CIDR
- resource tagging for ownership and auditability
