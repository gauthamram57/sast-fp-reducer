"""
Security evidence extracted by AI.
"""

from dataclasses import dataclass


@dataclass
class SecurityEvidence:
    """
    Technical evidence collected from AI reasoning.
    """

    vulnerability: str

    source: str

    sink: str

    sanitized: bool

    exploitable: bool

    cwe_match: bool

    owasp_match: bool
