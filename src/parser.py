"""
Parser for Semgrep JSON output.
"""

import json
from pathlib import Path

from src.models import SemgrepFinding


def load_semgrep_results(json_file: str) -> list[SemgrepFinding]:
    """
    Load Semgrep findings from a JSON report.
    """

    json_path = Path(json_file)

    if not json_path.exists():
        raise FileNotFoundError(f"File not found: {json_file}")

    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    findings = []

    for result in data.get("results", []):

        metadata = result.get("extra", {}).get("metadata", {})

        finding = SemgrepFinding(
            rule_id=result.get("check_id", ""),
            message=result.get("extra", {}).get("message", ""),
            severity=result.get("extra", {}).get("severity", ""),

            file_path=result.get("path", ""),

            start_line=result.get("start", {}).get("line", 0),
            end_line=result.get("end", {}).get("line", 0),

            confidence=metadata.get("confidence", ""),

            cwe=metadata.get("cwe", []),
            owasp=metadata.get("owasp", []),

            references=metadata.get("references", []),
            technology=metadata.get("technology", []),

            vulnerability_class=metadata.get(
                "vulnerability_class",
                [],
            ),
        )

        findings.append(finding)

    return findings
