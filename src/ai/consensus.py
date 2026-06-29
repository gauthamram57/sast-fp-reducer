"""
Consensus Engine

Combines the outputs from multiple AI providers into a single result.
"""

from src.models import AnalysisResult


class ConsensusEngine:
    """
    Combines multiple AI analyses into one final decision.
    """

    def combine(
        self,
        openrouter: AnalysisResult,
        groq: AnalysisResult,
    ) -> AnalysisResult:

        # -----------------------------
        # Classification
        # -----------------------------

        if openrouter.classification == groq.classification:
            classification = openrouter.classification
        else:
            classification = "NEEDS_REVIEW"

        # -----------------------------
        # Confidence
        # -----------------------------

        confidence = int(
            (
                openrouter.confidence +
                groq.confidence
            ) / 2
        )

        # -----------------------------
        # Merge evidence
        # Prefer OpenRouter, fallback to Groq
        # -----------------------------

        vulnerability = (
            openrouter.vulnerability
            or groq.vulnerability
        )

        source = (
            openrouter.source
            or groq.source
        )

        sink = (
            openrouter.sink
            or groq.sink
        )

        sanitized = (
            openrouter.sanitized
            or groq.sanitized
        )

        exploitable = (
            openrouter.exploitable
            or groq.exploitable
        )

        cwe_match = (
            openrouter.cwe_match
            or groq.cwe_match
        )

        owasp_match = (
            openrouter.owasp_match
            or groq.owasp_match
        )

        # -----------------------------
        # Reasoning
        # -----------------------------

        reasoning = (
            "Consensus reached.\n\n"
            "OpenRouter:\n"
            f"{openrouter.reasoning}\n\n"
            "Groq:\n"
            f"{groq.reasoning}"
        )

        # -----------------------------
        # Developer Action
        # -----------------------------

        developer_action = (
            openrouter.developer_action
            or groq.developer_action
        )

        return AnalysisResult(
            classification=classification,
            confidence=confidence,
            reasoning=reasoning,
            developer_action=developer_action,
            vulnerability=vulnerability,
            source=source,
            sink=sink,
            sanitized=sanitized,
            exploitable=exploitable,
            cwe_match=cwe_match,
            owasp_match=owasp_match,
        )
