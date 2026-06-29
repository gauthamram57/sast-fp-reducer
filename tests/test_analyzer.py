from src.parser import load_semgrep_results
from src.analyzer import FindingAnalyzer


def main():

    findings = load_semgrep_results(
        "examples/semgrep_output.json"
    )

    analyzer = FindingAnalyzer()

    result = analyzer.analyze(findings[0])

    print()

    print(result)


if __name__ == "__main__":
    main()
