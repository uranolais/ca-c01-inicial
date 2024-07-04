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

message = client.messages.create(
    # model="claude-3-opus-20240229",# 3.952160358428955 segundos | 2.9456045627593994 segundos | 3.415724992752075 segundos
    # model="claude-3-5-sonnet-20240620",# 1.9170119762420654 segundos | 1.775184154510498 segundos | 1.838169813156128 segundos
    # model= "claude-3-sonnet-20240229", # 4.4278693199157715 segundos | 3.022520065307617 segundos | 1.8555750846862793 segundos
    model="claude-3-haiku-20240307",# 2.6707873344421387 segundos | 1.327709436416626 segundos | 1.4343557357788086 segundos
    max_tokens=1000,
    temperature=0,
    # system="Listar apenas os nomes dos produtos, sem considerar descrição.",
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