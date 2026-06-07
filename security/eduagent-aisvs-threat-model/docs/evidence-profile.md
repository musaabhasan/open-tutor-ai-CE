# Evidence Profile for Agentic Education Systems

## Purpose

This profile defines what evidence a security reviewer should expect from an AI tutor or education support service that can retrieve course content, interact with an LMS, access student records, invoke tools, store memory, and recommend or initiate consequential education actions.

It is intended to make control verification concrete. A control is stronger when the reviewer can point to an artifact, inspect how it was produced, verify its integrity, and replay the relevant decision path.

## Evidence Object Format

Each evidence item should contain:

| Field | Description |
| --- | --- |
| `evidence_id` | Stable identifier for the artifact or record. |
| `control_id` | Internal control or policy identifier. |
| `control_family` | AISVS chapter or control family covered by the artifact. |
| `source_system` | System that produced the artifact. |
| `collection_method` | Automated collector, manual review, test harness, or runtime ledger. |
| `subject` | User, agent session, data source, tool, memory key, or workflow affected. |
| `decision` | Allowed, denied, redacted, quarantined, approved, expired, or escalated. |
| `integrity` | Hash, signature, append-only log pointer, or immutable storage reference. |
| `redaction` | Data removed before review or export. |
| `freshness` | Timestamp and maximum acceptable artifact age. |
| `owner` | Role responsible for the artifact. |
| `retention` | Retention period and disposal rule. |

## Required Evidence Sets

### 1. Architecture and Trust Boundaries

Required artifacts:

- System DFD with student, educator, LMS, tutor runtime, retrieval store, tool broker, model provider, audit store, and approval console.
- Trust-zone register with identity provider, LMS, runtime, data stores, third-party service boundary, and operations boundary.
- Data-flow register stating protocol, authentication mechanism, sensitive data flag, encryption status, and owner.

Review questions:

- Are grading, enrollment, assessment, and disciplinary actions separated from ordinary tutoring responses?
- Are student records and tutoring memory treated as separate data sets?
- Can untrusted course content or submitted files reach a tool call without a policy checkpoint?

### 2. Retrieval and Memory Integrity

Required artifacts:

- Source inventory for course content, policy documents, assignment text, and uploaded material.
- Retrieval provenance record for every response that used external content.
- Memory write log with source, reason, TTL, risk score, and policy decision.
- Quarantine queue for untrusted or suspicious memory writes.

Review questions:

- Can a hostile assignment, forum post, or course document alter the tutor's system behavior?
- Are memory writes blocked when the source is untrusted or contains instruction-like content?
- Can reviewers reconstruct which content influenced a specific answer or action?

### 3. Tool Access and Consequential Actions

Required artifacts:

- Tool allowlist with purpose, input schema, output schema, data classification, and allowed user roles.
- Tool execution receipt with request hash, response hash, user/session, policy version, and decision.
- Human approval record for grade changes, enrollment changes, assessment-level recommendations, and bulk student notifications.
- Denial records for attempted action escalation.

Review questions:

- Are tool calls bound to the student's current course, tenant, and role?
- Are high-impact LMS actions denied unless a human approval record exists?
- Can a tool response inject new instructions into the tutor runtime?

### 4. Privacy and Data Minimization

Required artifacts:

- Student data classification map.
- Provider request log showing minimized prompt and context fields.
- PII redaction report for logs, retrieval snippets, and third-party requests.
- Retention schedule for chat history, tutoring memory, evidence records, and analytics.

Review questions:

- Is student PII excluded from third-party requests unless explicitly required?
- Are grade, disability accommodation, conduct, and demographic fields handled as high-sensitivity data?
- Are logs safe to export to a reviewer without exposing unnecessary student data?

### 5. Audit, Monitoring, and Replay

Required artifacts:

- Append-only audit log or hash-chain proof for agent sessions and tool calls.
- Security event taxonomy covering prompt injection, memory poisoning, tool misuse, approval bypass, excessive retries, and cross-tenant context access.
- Incident replay bundle containing request, retrieval provenance, selected tool, policy version, approval state, output, and evidence references.
- Post-incident review template with control gap, root cause, remediation, and regression test.

Review questions:

- Can an investigator replay why the system took or denied an action?
- Is the audit trail tamper-evident?
- Are repeated denials, loop storms, suspicious memory writes, and privacy redactions monitored?

## Evidence Freshness

| Artifact | Freshness expectation |
| --- | --- |
| Tool allowlist | Reviewed at every release and after new LMS integration |
| Retrieval source inventory | Reviewed after content import and at least monthly |
| Prompt and policy templates | Reviewed at every release |
| High-impact approval matrix | Reviewed at least quarterly |
| Audit integrity proof | Generated continuously or daily |
| Regression test suite | Run at every release and after incident remediation |

## Reviewer Output

A complete review should produce:

- Threat-model coverage statement.
- Control coverage matrix.
- Evidence register.
- Open findings with severity and affected workflow.
- Replay bundle for at least one allowed action, one denied action, and one human-approved action.
