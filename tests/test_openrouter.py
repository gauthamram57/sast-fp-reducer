from src.ai.client import OpenRouterClient


def main():
    client = OpenRouterClient()

    response = client.chat(
        "Reply ONLY with this JSON: {\"status\":\"working\"}"
    )

    print(response)


if __name__ == "__main__":
    main()
