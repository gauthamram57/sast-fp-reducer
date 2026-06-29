"""
Main CLI entry point for the SAST FP Reducer.
"""

import argparse

from src.analyzer import FindingAnalyzer
from src.parser import load_semgrep_results
from src.reporter import Reporter


def main():

    parser = argparse.ArgumentParser(
        description="SAST False Positive Reducer"
    )

    parser.add_argument(
        "--scan",
        required=True,
        help="Project directory that was scanned",
    )

    parser.add_argument(
        "--report",
        default="examples/semgrep_output.json",
        help="Semgrep JSON report",
    )

    parser.add_argument(
        "--output",
        default="reports/report.json",
        help="Output report",
    )

    args = parser.parse_args()

    findings = load_semgrep_results(args.report)

    analyzer = FindingAnalyzer(args.scan)

    reporter = Reporter()

    print(f"\nLoaded {len(findings)} findings\n")

    for finding in findings:

        print(f"Analyzing: {finding.rule_id}")

        analysis = analyzer.analyze(finding)

        reporter.add_result(
            finding,
            analysis,
        )

    print()

    reporter.print_summary()

    reporter.save_json(args.output)


if __name__ == "__main__":
    main()

