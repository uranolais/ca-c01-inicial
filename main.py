import anthropic
import dotenv 
import os
import time

# Marca o início do tempo
start_time = time.time()

dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
    # api_key=''
)
modelo = "claude-3-5-sonnet-20240620"
message = client.messages.create(
    model=modelo,
    max_tokens=1000,
    temperature=0,
    system="Listar apenas os nomes dos alimentos, sem considerar descrição.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "liste 3 alimentos veganos\n" # 3 produtos sustentáveis | 3 alimentos veganos | 3 alimentos com brócolis
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

# Marca o fim do tempo
end_time = time.time()

# Calcula o tempo de execução
execution_time = end_time - start_time

print(f"Tempo de execução: {execution_time} segundos")