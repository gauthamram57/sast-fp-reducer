from src.ai.groq_client import GroqClient


def main():

    client = GroqClient()

    response = client.chat(
        """
Reply ONLY with this JSON:

{
    "status": "working"
}
"""
    )

    print(response)


if __name__ == "__main__":
    main()
