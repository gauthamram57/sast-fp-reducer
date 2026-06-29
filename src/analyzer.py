"""
Coordinates the complete AI analysis pipeline.

This module is responsible for orchestrating the entire workflow:

Semgrep Finding
        │
        ▼
Code Context Extraction
        │
        ▼
Prompt Generation
        │
        ▼
LLM Analysis
        │
        ▼
JSON Extraction
        │
        ▼
AnalysisResult Object
"""

from src.ai.client import OpenRouterClient
from src.context import extract_code_context
from src.models import AnalysisResult
from src.prompts import build_prompt
from src.utils import extract_json


class FindingAnalyzer:
    """
    Main orchestrator for analyzing a Semgrep finding.
    """

    def __init__(self):
        self.client = OpenRouterClient()

    def analyze(self, finding) -> AnalysisResult:
        """
        Analyze a single Semgrep finding using the configured LLM.

        Args:
            finding: SemgrepFinding object.

        Returns:
            AnalysisResult
        """

        # ----------------------------------------
        # Step 1: Extract source code context
        # ----------------------------------------

        context = extract_code_context(
            file_path=f"examples/vulnerable_app/{finding.file_path}",
            start_line=finding.start_line,
            end_line=finding.end_line,
        )

        # ----------------------------------------
        # Step 2: Build LLM Prompt
        # ----------------------------------------

        prompt = build_prompt(
            finding=finding,
            context=context,
        )

        # ----------------------------------------
        # Step 3: Send Prompt to AI
        # ----------------------------------------

        response = self.client.chat(prompt)

        # ----------------------------------------
        # Step 4: Extract JSON
        # ----------------------------------------

        data = extract_json(response)

        # ----------------------------------------
        # Step 5: Convert JSON -> AnalysisResult
        # ----------------------------------------

        result = AnalysisResult(
            classification=data["classification"],
            confidence=data["confidence"],
            reasoning=data["reasoning"],
            developer_action=data["developer_action"],
        )

        # ----------------------------------------
        # Step 6: Validate Result
        # ----------------------------------------

        result.validate()

        return result
