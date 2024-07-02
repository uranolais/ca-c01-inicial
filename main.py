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
    model="claude-3-opus-20240229",# 4.545861721038818 segundos | 2.9456045627593994 segundos
    # model="claude-3-5-sonnet-20240620",#1.962998628616333 segundos | 1.775184154510498 segundos
    # model= "claude-3-sonnet-20240229", #4.803567171096802 segundos | 3.022520065307617 segundos
    # model="claude-3-haiku-20240307",#2.4997713565826416 segundos | 1.327709436416626 segundos
    max_tokens=1000,
    temperature=0,
    system="Listar apenas os nomes dos alimentos, sem considerar descrição.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "liste 3 alimentos veganos\n"
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