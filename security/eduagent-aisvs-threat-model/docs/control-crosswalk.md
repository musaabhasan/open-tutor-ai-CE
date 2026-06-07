# Control Crosswalk

This crosswalk links the education-agent threat model to verification families and OWASP risk areas. Exact AISVS row identifiers should be finalized against the released chapter files before opening an AISVS change request. The threat model itself remains valid without relying on extension-specific identifiers.

## Summary

| Threat | Primary control | AISVS control family | Related OWASP risk area |
| --- | --- | --- | --- |
| `prompt-injection-course-content` | `untrusted-content-isolation` | C02 Input Validation, C07 Output Control, C09 Agentic Action Security | Prompt injection, goal hijack, unsafe output handling |
| `rag-corpus-poisoning` | `retrieval-provenance-and-quarantine` | C01 Training Data Integrity, C08 Memory and Embeddings, C13 Monitoring | Data poisoning, vector weakness, supply chain |
| `gradebook-action-hijack` | `gradebook-two-person-approval` | C05 Access Control, C09 Agentic Action Security, C14 Human Oversight | Excessive agency, unauthorized action |
| `excessive-tool-permission` | `tool-allowlist-and-scope-binding` | C05 Access Control, C09 Agentic Action Security, C10 MCP Security | Excessive agency, insecure plugin or tool design |
| `memory-poisoning-session` | `memory-write-gates` | C08 Memory and Embeddings, C13 Monitoring | Memory poisoning, persistent prompt injection |
| `student-pii-disclosure` | `pii-redaction-and-purpose-limiting` | C02 Input Validation, C05 Access Control, C12 Privacy | Sensitive information disclosure |
| `unsafe-mcp-tool-output` | `mcp-tool-contract-validation` | C10 MCP Security, C09 Agentic Action Security | Tool poisoning, context injection |
| `audit-log-tampering` | `immutable-audit-chain` | C13 Monitoring, C09 Identity and Audit | Lack of audit and telemetry |
| `human-approval-bypass` | `human-review-failsafe` | C14 Human Oversight, C09 Agentic Action Security | Overreliance, excessive agency |
| `cross-tenant-context-leakage` | `tenant-context-boundaries` | C05 Access Control, C08 Memory and Embeddings, C12 Privacy | Context over-sharing, information disclosure |
| `runaway-agent-loop-resource-abuse` | `budget-and-loop-limits` | C09 Agentic Action Security, C13 Monitoring | Unbounded consumption, cascading failures |
| `provider-data-overexposure` | `provider-data-minimization` | C06 Supply Chain, C12 Privacy | Supply chain, sensitive information disclosure |

## Evidence Classes

| Evidence class | Examples | Integrity expectation |
| --- | --- | --- |
| Design evidence | DFD, trust-zone model, tool permission register, approval matrix | Version controlled and reviewed |
| Deterministic artifact | Policy file, tool manifest, prompt template, retrieval allowlist, signing key config | Hash recorded at release |
| Runtime record | Tool call receipt, retrieval provenance record, approval decision, memory write decision | Append-only storage or hash chain |
| Test result | Prompt injection regression, poisoned corpus replay, gradebook action denial test | Linked to build, commit, and scenario |
| Review record | Human approval, exception decision, post-incident review | Named owner, timestamp, retention period |

## Minimum Viable Contribution

For the first upstream PR, the JSON model should be sufficient. The evidence and lab documents are included to make the contribution more useful, but the Threat Model Library should receive the model first because it is compatible with the existing schema.

## Follow-Up AISVS Proposal

The strongest follow-up is an evidence profile rather than a new scanner:

1. Add an education-sector implementation note for AISVS chapters C08, C09, C10, C13, and C14.
2. Define expected evidence artifacts for agentic LMS systems.
3. Link high-risk actions such as grading, enrollment, assessment recommendations, and student data disclosure to mandatory human review and tamper-evident logs.
4. Provide a small test matrix that implementers can reproduce during security assessment.
