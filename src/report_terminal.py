"""
Terminal report renderer.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.rule import Rule


console = Console()


class TerminalReporter:

    def print_banner(self):

        console.print()

        console.print(
            Panel.fit(
                "[bold cyan]AI SAST TRIAGE REPORT[/bold cyan]",
                border_style="cyan",
            )
        )

        console.print()

    def print_finding(
        self,
        index,
        finding,
        analysis,
    ):

        console.print(
            Rule(f"[bold yellow]Finding #{index}[/bold yellow]")
        )

        table = Table(
            show_header=False,
            box=None,
        )

        table.add_column(style="cyan", width=22)
        table.add_column()

        table.add_row(
            "Rule ID",
            finding.rule_id,
        )

        table.add_row(
            "Severity",
            finding.severity,
        )

        table.add_row(
            "File",
            finding.file_path,
        )

        table.add_row(
            "Lines",
            f"{finding.start_line}-{finding.end_line}",
        )

        table.add_row(
            "Classification",
            analysis.classification,
        )

        table.add_row(
            "Confidence",
            f"{analysis.confidence}%",
        )

        table.add_row(
            "Vulnerability",
            analysis.vulnerability,
        )

        table.add_row(
            "Source",
            analysis.source,
        )

        table.add_row(
            "Sink",
            analysis.sink,
        )

        table.add_row(
            "Sanitized",
            "Yes" if analysis.sanitized else "No",
        )

        table.add_row(
            "Exploitable",
            "Yes" if analysis.exploitable else "No",
        )

        table.add_row(
            "CWE Match",
            "Yes" if analysis.cwe_match else "No",
        )

        table.add_row(
            "OWASP Match",
            "Yes" if analysis.owasp_match else "No",
        )

        console.print(table)

        console.print()

        console.print(
            Panel(
                analysis.reasoning,
                title="Reasoning",
                border_style="green",
            )
        )

        console.print()

        console.print(
            Panel(
                analysis.developer_action,
                title="Recommended Fix",
                border_style="red",
            )
        )

        console.print()

    def print_summary(
        self,
        total,
        tp,
        fp,
        review,
    ):

        table = Table(
            title="Summary",
        )

        table.add_column("Metric")
        table.add_column("Value")

        table.add_row(
            "Total Findings",
            str(total),
        )

        table.add_row(
            "True Positives",
            str(tp),
        )

        table.add_row(
            "False Positives",
            str(fp),
        )

        table.add_row(
            "Needs Review",
            str(review),
        )

        console.print(table)
