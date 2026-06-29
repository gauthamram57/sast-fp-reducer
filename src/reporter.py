"""
Reporter module.

Responsible for:
- Displaying results
- Calculating statistics
- Saving JSON reports
"""

import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

from src.models import AnalysisResult


console = Console()


class Reporter:

    def __init__(self):

        self.results = []

    def add_result(self, finding, analysis):

        self.results.append(
            {
                "finding": finding,
                "analysis": analysis,
            }
        )

    def print_summary(self):

        total = len(self.results)

        tp = 0
        fp = 0
        review = 0

        table = Table(title="SAST FP Reducer")

        table.add_column("Rule")
        table.add_column("Severity")
        table.add_column("Classification")
        table.add_column("Confidence")

        for item in self.results:

            finding = item["finding"]
            analysis: AnalysisResult = item["analysis"]

            if analysis.classification == "TRUE_POSITIVE":
                tp += 1

            elif analysis.classification == "FALSE_POSITIVE":
                fp += 1

            else:
                review += 1

            table.add_row(
                finding.rule_id,
                finding.severity,
                analysis.classification,
                str(analysis.confidence),
            )

        console.print(table)

        console.print()

        console.print(f"Total Findings : {total}")
        console.print(f"True Positives : {tp}")
        console.print(f"False Positives: {fp}")
        console.print(f"Needs Review   : {review}")

    def save_json(self, output_file):

        report = []

        for item in self.results:

            finding = item["finding"]
            analysis = item["analysis"]

            report.append(
                {
                    "rule_id": finding.rule_id,
                    "file": finding.file_path,
                    "severity": finding.severity,
                    "classification": analysis.classification,
                    "confidence": analysis.confidence,
                    "reasoning": analysis.reasoning,
                    "developer_action": analysis.developer_action,
                }
            )

        Path(output_file).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(output_file, "w") as f:
            json.dump(
                report,
                f,
                indent=4,
            )

        console.print()
        console.print(f"Report saved to {output_file}")
