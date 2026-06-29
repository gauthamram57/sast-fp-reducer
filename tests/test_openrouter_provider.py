from src.ai.openrouter_client import OpenRouterClient


def main():

    client = OpenRouterClient()

    response = client.chat(
        'Reply ONLY with {"status":"ok"}'
    )

    print()
    print(response)


if __name__ == "__main__":
    main()
