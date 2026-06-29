"""
Integration test for the parser and context extractor.
"""

from pathlib import Path

from src.context import extract_code_context
from src.parser import load_semgrep_results


def main():
    # Load all Semgrep findings
    findings = load_semgrep_results("examples/semgrep_output.json")

    print("=" * 80)
    print(f"Loaded {len(findings)} findings")
    print("=" * 80)

    for index, finding in enumerate(findings, start=1):
        print(f"\nFinding #{index}")
        print("-" * 80)

        print(f"Rule ID     : {finding.rule_id}")
        print(f"Severity    : {finding.severity}")
        print(f"File        : {finding.file_path}")
        print(f"Start Line  : {finding.start_line}")
        print(f"End Line    : {finding.end_line}")

        source_file = Path("examples/vulnerable_app") / finding.file_path

        context = extract_code_context(
            file_path=str(source_file),
            start_line=finding.start_line,
            end_line=finding.end_line,
        )

        print("\n----- BEFORE -----")
        print(context.before)

        print("----- TARGET -----")
        print(context.target)

        print("----- AFTER ------")
        print(context.after)

        print("=" * 80)


if __name__ == "__main__":
    main()
