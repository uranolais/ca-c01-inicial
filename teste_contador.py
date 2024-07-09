import requests
import os
import dotenv 

dotenv.load_dotenv()
api_key = os.environ.get("ANTHROPIC_API_KEY")
modelo = "claude-3-5-sonnet-20240620"
def conta_tokens(modelo):
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers=headers,
        json={
            "model": modelo,
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": "Hello, Claude"}]
        }
    )

    # Acessar os cabeçalhos relevantes
    tokens_limit = response.headers.get('anthropic-ratelimit-tokens-limit')
    tokens_remaining = response.headers.get('anthropic-ratelimit-tokens-remaining')
    tokens_reset = response.headers.get('anthropic-ratelimit-tokens-reset')

    # print(f"Limite de tokens: {tokens_limit}")
    # print(f"Tokens restantes: {tokens_remaining}")
    # print(f"Reset do limite: {tokens_reset}")

    return tokens_limit

conta_tokens(modelo=modelo)