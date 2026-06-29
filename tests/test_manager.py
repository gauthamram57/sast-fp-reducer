from src.ai.manager import AIManager


def main():

    manager = AIManager()

    prompt = """
Reply ONLY with this JSON:

{
    "status":"working"
}
"""

    print("\n===== OpenRouter =====\n")

    print(
        manager.analyze_with_openrouter(
            prompt
        )
    )

    print("\n===== Groq =====\n")

    print(
        manager.analyze_with_groq(
            prompt
        )
    )


if __name__ == "__main__":
    main()
