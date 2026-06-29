"""
Prompt builder for the AI-assisted SAST triage engine.
"""

from src.models import CodeContext, SemgrepFinding


def build_prompt(
    finding: SemgrepFinding,
    context: CodeContext,
) -> str:

    return f"""
You are a Principal Application Security Engineer.

You are reviewing a Semgrep SAST finding.

Your task is NOT to blindly trust the scanner.

Analyze the finding like a human AppSec engineer.

========================
Finding Metadata
========================

Rule ID:
{finding.rule_id}

Severity:
{finding.severity}

Message:
{finding.message}

CWE:
{", ".join(finding.cwe)}

OWASP:
{", ".join(finding.owasp)}

Technology:
{", ".join(finding.technology)}

========================
Source Code
========================

----- BEFORE -----

{context.before}

----- TARGET -----

{context.target}

----- AFTER -----

{context.after}

========================
Instructions
========================

Perform a security review.

Determine:

1. Vulnerability type.

2. User-controlled source.

3. Dangerous sink.

4. Is the input sanitized?

5. Is the vulnerability realistically exploitable?

6. Does it match the reported CWE?

7. Does it match the OWASP category?

8. Explain your reasoning.

9. Recommend the best remediation.

10. Final classification.

Return ONLY valid JSON.

{{
    "vulnerability":"",

    "source":"",

    "sink":"",

    "sanitized":false,

    "exploitable":true,

    "cwe_match":true,

    "owasp_match":true,

    "classification":"TRUE_POSITIVE",

    "confidence":95,

    "reasoning":"",

    "developer_action":""
}}
"""
