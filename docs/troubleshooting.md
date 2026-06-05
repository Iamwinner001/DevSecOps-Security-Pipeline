# Troubleshooting

## Jenkins Cannot Find Checkov

Install Checkov on the Jenkins agent:

```bash
pip install checkov
```

Then confirm:

```bash
checkov --version
```

## Jenkins Cannot Find Dependency Check

Install OWASP Dependency Check CLI and add it to the agent `PATH`.

Confirm:

```bash
dependency-check.sh --version
```

## SonarQube Quality Gate Times Out

Check:

- Jenkins has a configured SonarQube server named `SonarQube`.
- The SonarQube webhook points back to Jenkins.
- The project key matches `devsecops-security-pipeline`.
- The token credential is valid.

## Terraform Backend Fails During Init

Common causes:

- S3 backend bucket does not exist.
- DynamoDB lock table does not exist.
- Jenkins AWS credentials lack backend permissions.
- Region mismatch between backend and AWS provider.

## Checkov Fails on Expected Demo Findings

This is expected when intentionally insecure infrastructure is added for testing. For production, fix the control violation instead of suppressing the check. Suppressions should require security team approval and include a compensating control.

## Bandit Fails on `app/app.py`

This is expected. The file intentionally contains vulnerabilities for demonstration. Use `app/secure_app.py` for production deployment. The Dockerfile starts the secure version by default.

## Dependency Check Database Download Fails

Dependency Check requires CVE database access. In a locked-down enterprise network:

- configure a proxy
- mirror the NVD data feed internally
- cache `.dependency-check-data` on Jenkins agents
- allow the required outbound endpoints through egress controls

## Terraform Apply Requires Manual Approval

This is intentional. The Jenkinsfile requires human approval before applying infrastructure changes on `main`.
