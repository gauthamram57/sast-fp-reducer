from src.models import AnalysisResult
from src.ai.consensus import ConsensusEngine


def main():

    engine = ConsensusEngine()

    openrouter = AnalysisResult(
        classification="TRUE_POSITIVE",
        confidence=95,
        reasoning="Command injection is exploitable.",
        developer_action="Remove shell=True.",
    )

    groq = AnalysisResult(
        classification="TRUE_POSITIVE",
        confidence=90,
        reasoning="User-controlled input reaches subprocess.",
        developer_action="Use subprocess.run safely.",
    )

    result = engine.combine(
        openrouter,
        groq,
    )

    print(result)


if __name__ == "__main__":
    main()
