"""
AI Provider Manager
"""

from src.ai.consensus import ConsensusEngine
from src.ai.groq_client import GroqClient
from src.ai.openrouter_client import OpenRouterClient
from src.models import AnalysisResult
from src.utils import extract_json


class AIManager:
    """
    Handles multiple AI providers and combines their results.
    """

    def __init__(self):
        self.openrouter = OpenRouterClient()
        self.groq = GroqClient()
        self.consensus = ConsensusEngine()

    def _build_result(self, data: dict) -> AnalysisResult:
        return AnalysisResult(
            classification=data["classification"],
            confidence=data["confidence"],
            reasoning=data["reasoning"],
            developer_action=data["developer_action"],
            vulnerability=data.get("vulnerability", ""),
            source=data.get("source", ""),
            sink=data.get("sink", ""),
            sanitized=data.get("sanitized", False),
            exploitable=data.get("exploitable", False),
            cwe_match=data.get("cwe_match", False),
            owasp_match=data.get("owasp_match", False),
        )

    def analyze(self, prompt: str) -> AnalysisResult:

        # ---------- OpenRouter ----------
        openrouter_response = self.openrouter.chat(prompt)

        print("\n========== OPENROUTER RESPONSE ==========")
        print(openrouter_response)
        print("=========================================\n")

        openrouter_data = extract_json(openrouter_response)
        openrouter_result = self._build_result(openrouter_data)

        # ---------- Groq ----------
        groq_response = self.groq.chat(prompt)

        print("\n============= GROQ RESPONSE =============")
        print(groq_response)
        print("=========================================\n")

        groq_data = extract_json(groq_response)
        groq_result = self._build_result(groq_data)

        # ---------- Consensus ----------
        return self.consensus.combine(
            openrouter_result,
            groq_result,
        )
