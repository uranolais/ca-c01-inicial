import anthropic
import dotenv 
import os

dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
    # api_key=''
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0,
    system="Listar apenas os nomes dos produtos, sem considerar descrição.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "liste 3 produtos sustentáveis\n"
                }
            ]
        }
    ]
)
# print(message.content)

# Acessando a informação de "text"
conteudo_texto = message.content[0].text #posição 0 da lista de text

# Exibindo o texto
print(conteudo_texto)