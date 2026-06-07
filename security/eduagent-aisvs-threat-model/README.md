# EduAgent AISVS Threat Model and Evidence Profile

This repository packages a contribution-ready threat model and assurance profile for an agentic education system: an AI tutor connected to a learning management system, course content, student records, grading workflows, notifications, retrieval stores, and governed tool access.

The goal is to provide a concrete reference architecture for education and training systems that need to satisfy security verification expectations from OWASP AISVS, OWASP GenAI guidance, OWASP Top 10 for Agentic Applications, and OWASP MCP Top 10.

## Contents

- `threat-models/ai-ml-systems/agentic-ai-tutor-lms-threat-model.json` - OWASP Threat Model Library compatible JSON model.
- `docs/evidence-profile.md` - Evidence-as-code profile for audits, assessments, and implementation reviews.
- `docs/control-crosswalk.md` - Crosswalk from threats and controls to AISVS control families and related OWASP risk areas.
- `labs/scenarios/README.md` - Reproducible defensive lab scenarios for validation and training.
- `tools/validate_threat_model.py` - Local validator for the OWASP Threat Model Library schema.
- `docs/owasp-pr-plan.md` - Suggested upstream contribution path and PR text.
- `SECURITY.md` - Responsible-use boundaries for authorized defensive work.
- `DISCLAIMER.md` - Independent-reference and no-endorsement notice.

## Intended Upstream Path

Primary target:

- `OWASP/www-project-threat-model-library`
- Proposed file path: `threat-models/ai-ml-systems/agentic-ai-tutor-lms-threat-model.json`

Secondary follow-up:

- `OWASP/AISVS`
- Proposed topic: an education-sector evidence profile for agentic systems and LMS integrations.

## Validate

```powershell
python tools/validate_threat_model.py threat-models/ai-ml-systems/agentic-ai-tutor-lms-threat-model.json
```

The validator fetches the current OWASP Threat Model Library schema from GitHub and validates the local JSON model against it.

## Responsible Use

Use this material only for defensive security review, education, architecture analysis, and authorized testing. Lab exercises should use synthetic data and local or mocked services.

This repository is an independent contribution package. It does not imply endorsement by OWASP, any institution, or any vendor unless formally accepted by the relevant project.

## Scope

The model covers:

- Prompt and instruction injection through course content, chat, assignments, and retrieved documents.
- Retrieval corpus poisoning and unsafe memory writes.
- Gradebook and enrollment action hijacking.
- Excessive tool permissions and unsafe MCP tool exposure.
- Student privacy leakage and cross-tenant context exposure.
- Human approval bypass for consequential education actions.
- Tamper-evident audit, evidence collection, incident replay, and review records.

## License

Documentation, threat-model content, control mappings, and lab scenario descriptions are offered under CC BY-SA 4.0. The validation utility under `tools/` is offered under MIT. Contributions intended for upstream OWASP repositories should remain compatible with the license and contribution requirements of the target OWASP project.
