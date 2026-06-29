"""
JSON report exporter.
"""

import json
from pathlib import Path


def save_json_report(results, output_file):

    report = []

    for item in results:

        finding = item["finding"]
        analysis = item["analysis"]

        report.append(
            {
                "rule_id": finding.rule_id,
                "file": finding.file_path,
                "severity": finding.severity,
                "start_line": finding.start_line,
                "end_line": finding.end_line,
                "classification": analysis.classification,
                "confidence": analysis.confidence,
                "vulnerability": analysis.vulnerability,
                "source": analysis.source,
                "sink": analysis.sink,
                "sanitized": analysis.sanitized,
                "exploitable": analysis.exploitable,
                "cwe_match": analysis.cwe_match,
                "owasp_match": analysis.owasp_match,
                "reasoning": analysis.reasoning,
                "developer_action": analysis.developer_action,
            }
        )

    Path(output_file).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(output_file, "w", encoding="utf-8") as file:

        json.dump(
            report,
            file,
            indent=4,
        )

    print(f"\n✓ JSON report saved to {output_file}")
