# Architecture Diagram

This architecture shows a shift-left DevSecOps workflow where Jenkins orchestrates source checkout, security scanning, security gate enforcement, Terraform deployment, application packaging, report publishing, and team notifications.

```mermaid
flowchart LR
    Dev["Developer Workstation"] --> PR["Pull Request"]
    PR --> GitHub["GitHub Repository"]
    GitHub --> Jenkins["Jenkins Controller/Agent"]

    subgraph CI["CI Security Validation"]
        Jenkins --> TFValidate["Terraform Validate"]
        Jenkins --> Checkov["Checkov IaC Security Scan"]
        Jenkins --> PyLint["Python Lint"]
        Jenkins --> Bandit["Bandit SAST"]
        Jenkins --> DependencyCheck["OWASP Dependency Check"]
        Jenkins --> SonarQube["SonarQube Code Quality and Security Hotspots"]
    end

    TFValidate --> SecurityGate["Security Gate Policy"]
    Checkov --> SecurityGate
    PyLint --> SecurityGate
    Bandit --> SecurityGate
    DependencyCheck --> SecurityGate
    SonarQube --> SecurityGate

    SecurityGate -->|Critical findings or High findings found| Blocked["Deployment Blocked"]
    SecurityGate -->|Passed| TFPlan["Terraform Plan"]
    TFPlan --> Approval["Manual Production Approval"]
    Approval --> TFApply["Terraform Apply"]

    subgraph AWS["AWS Landing Zone"]
        TFApply --> VPC["Encrypted and Tagged VPC Resources"]
        VPC --> PublicSubnet["Public Subnet"]
        VPC --> PrivateSubnet["Private Subnet"]
        PublicSubnet --> EC2["Hardened EC2 App Host"]
        PrivateSubnet --> S3["Encrypted S3 Logs Bucket"]
        EC2 --> IAM["Least-Privilege IAM Role"]
        EC2 --> SG["Restricted Security Groups"]
    end

    Jenkins --> Reports["Archived Security Reports"]
    Jenkins --> Notify["Slack and Email Notifications"]
```

## Design Notes

- GitHub is the source of truth for application and infrastructure code.
- Jenkins agents run all security scans before deployment.
- Checkov validates Terraform against cloud security policies.
- Bandit detects insecure Python implementation patterns.
- OWASP Dependency Check detects vulnerable open-source packages.
- SonarQube enforces quality gates and tracks maintainability/security hotspots.
- Terraform provisions AWS infrastructure with encryption, logging, tagging, and least privilege.
- Jenkins publishes reports regardless of pass/fail outcome so failed builds remain auditable.
