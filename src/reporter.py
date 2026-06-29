"""
Reporter module.

Coordinates all report outputs.
"""

from src.report_terminal import TerminalReporter
from src.report_json import save_json_report


class Reporter:

    def __init__(self):

        self.results = []

        self.terminal = TerminalReporter()

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

        self.terminal.print_banner()

        for index, item in enumerate(self.results, start=1):

            finding = item["finding"]
            analysis = item["analysis"]

            if analysis.classification == "TRUE_POSITIVE":
                tp += 1

            elif analysis.classification == "FALSE_POSITIVE":
                fp += 1

            else:
                review += 1

            self.terminal.print_finding(
                index,
                finding,
                analysis,
            )

        self.terminal.print_summary(
            total,
            tp,
            fp,
            review,
        )

    def save_json(self, output_file):

        save_json_report(
            self.results,
            output_file,
        )
