"""
Data models used throughout the SAST FP Reducer project.
"""

from dataclasses import dataclass, field


@dataclass
class SemgrepFinding:
    """Represents a normalized Semgrep finding."""

    rule_id: str
    message: str
    severity: str

    file_path: str

    start_line: int
    end_line: int

    confidence: str = ""

    cwe: list[str] = field(default_factory=list)
    owasp: list[str] = field(default_factory=list)

    references: list[str] = field(default_factory=list)
    technology: list[str] = field(default_factory=list)

    vulnerability_class: list[str] = field(default_factory=list)

    code: str = ""


@dataclass
class CodeContext:
    """Represents source code surrounding a finding."""

    before: str
    target: str
    after: str


@dataclass
class AnalysisResult:
    """Represents the AI analysis for a finding."""

    classification: str
    confidence: int
    reasoning: str
    developer_action: str


@dataclass
class ReportSummary:
    """Statistics for the final report."""

    total_findings: int
    true_positives: int
    false_positives: int
    needs_review: int
