"""
Prompt builder for the SAST False Positive Reducer.
"""

from src.models import CodeContext, SemgrepFinding


def build_prompt(
    finding: SemgrepFinding,
    context: CodeContext,
) -> str:
    """
    Build a structured prompt for the LLM.
    """

    prompt = f"""
You are a Senior Application Security Engineer.

Your task is to review a Semgrep SAST finding.

Determine whether it is:

- TRUE_POSITIVE
- FALSE_POSITIVE
- NEEDS_REVIEW

Return ONLY valid JSON.

Finding Details

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

Source Code

----- BEFORE -----
{context.before}

----- TARGET -----
{context.target}

----- AFTER -----
{context.after}

Respond ONLY in this JSON format:

{{
    "classification": "TRUE_POSITIVE",
    "confidence": 95,
    "reasoning": "...",
    "developer_action": "..."
}}
"""

    return prompt.strip()
