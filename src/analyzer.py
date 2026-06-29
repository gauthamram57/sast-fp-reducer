"""
Coordinates the complete AI analysis pipeline.
"""

from src.ai.manager import AIManager
from src.context import extract_code_context
from src.models import AnalysisResult
from src.prompts import build_prompt


class FindingAnalyzer:
    """
    Main orchestrator for analyzing a Semgrep finding.
    """

    def __init__(self, project_root: str):
        self.client = AIManager()
        self.project_root = project_root

    def analyze(self, finding) -> AnalysisResult:
        """
        Analyze a single Semgrep finding.
        """

        # Step 1: Extract surrounding source code
        context = extract_code_context(
            file_path=f"{self.project_root}/{finding.file_path}",
            start_line=finding.start_line,
            end_line=finding.end_line,
        )

        # Step 2: Build the AI prompt
        prompt = build_prompt(
            finding=finding,
            context=context,
        )

        # Step 3: Ask the AI manager (OpenRouter + Groq + Consensus)
        result = self.client.analyze(prompt)

        # Step 4: Validate the result
        result.validate()

        return result
