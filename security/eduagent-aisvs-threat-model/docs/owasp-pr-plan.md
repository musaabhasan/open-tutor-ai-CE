# Upstream Contribution Plan

## Primary PR

Repository:

`OWASP/www-project-threat-model-library`

Proposed title:

`Add agentic AI tutor and LMS integration threat model`

Proposed file:

`threat-models/ai-ml-systems/agentic-ai-tutor-lms-threat-model.json`

Proposed PR body:

```text
This PR adds a threat model for an agentic education system: an AI tutor connected to an LMS, course content, student records, retrieval memory, tool access, notifications, evidence collection, and human review workflows.

The model covers education-specific risks such as course-content prompt injection, retrieval corpus poisoning, memory poisoning, gradebook action hijack, excessive tool permissions, unsafe MCP tool output, cross-tenant context leakage, student PII disclosure, approval bypass, resource abuse, and audit-log tampering.

The JSON model validates against the current OWASP Threat Model Library schema and keeps richer protocol/auth and data-flow threat detail in descriptions so the model remains compatible with the existing schema.

Related schema gaps:
- #46: Threats cannot be associated with data flows
- #47: Data flows lack protocol and auth_mechanism properties
```

## Secondary AISVS Discussion

Repository:

`OWASP/AISVS`

Suggested title:

`Education-sector evidence profile for agentic LMS and tutor systems`

Suggested discussion body:

```text
I would like to propose an education-sector evidence profile for systems where an AI tutor or education support service can retrieve course content, access student records, use memory, invoke tools, and recommend or initiate consequential LMS actions.

The profile focuses on verifiable evidence artifacts rather than product recommendations:
- trust-zone and data-flow register
- retrieval provenance records
- memory write gates and quarantine records
- tool allowlist and execution receipts
- human approval records for grade, enrollment, assessment, and notification actions
- provider data-minimization logs
- tamper-evident audit trail
- incident replay bundle

This could be useful as an AISVS implementation note for C08, C09, C10, C13, and C14, and as a practical example for high-risk education workflows.
```

## Why This Contribution Is Distinct

Most current work in the space focuses on generic scanners, generic agent policy, or generic memory defense. This contribution is sector-specific, evidence-oriented, and directly useful for security assessment of education systems where privacy, student welfare, and high-impact institutional actions matter.
