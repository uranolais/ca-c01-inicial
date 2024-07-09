import anthropic
import dotenv 
import os
import json 


dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

def carrega (nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro no carregamento de arquivo: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")


def analisar_transacao(lista_de_transacoes):
    print("1. Executando a análise de transação")
    
    prompt_sistema = """
    Analise as transações financeiras a seguir e identifique se cada uma delas é uma "Possível Fraude" ou deve ser "Aprovada". 
    Adicione um atributo "Status" com um dos valores: "Possível Fraude" ou "Aprovado".

    Cada nova transação deve ser inserida dentro da lista do JSON.

    # Possíveis indicações de fraude
    - Transações com valores muito discrepantes
    - Transações que ocorrem em locais muito distantes um do outro
    
        Adote o formato de resposta abaixo para compor sua resposta.
        
    # Formato Saída 
    {
        "transacoes": [
            {
            "id": "id",
            "tipo": "crédito ou débito",
            "estabelecimento": "nome do estabelecimento",
            "horário": "horário da transação",
            "valor": "R$XX,XX",
            "nome_produto": "nome do produto",
            "localização": "cidade - estado (País)"
            "status": ""
            },
        ]
    } 

    """
    prompt_usuario = f"""
    Considere o CSV abaixo, onde cada linha é uma transação diferente: {lista_de_transacoes}. 
    Sua resposta deve adotar o #Formato de Resposta (apenas um json sem outros comentários)"""
    
    modelo = "claude-3-5-sonnet-20240620"
    try:
        
        lista_mensagens = client.messages.create(
            model=modelo,
            max_tokens=4000,
            # temperature=0,
            system=prompt_sistema,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt_usuario
                        }
                    ]
                }
            ]
        )
        conteudo = lista_mensagens.content[0].text.replace("'", '"')
        # print(conteudo)
        print("\nConteúdo:", conteudo)
        json_resultado = json.loads(conteudo)
        print("\nJSON:", json_resultado)
        return json_resultado
    except anthropic.APIConnectionError as e:
        print("Não foi possivel se conectar ao servidor")
        print(e.__cause__)  # an underlying Exception, likely raised within httpx.
    except anthropic.RateLimitError as e:
        print("Espere um tempo! Seu limite foi atingido.")
    except anthropic.APIStatusError as e:
        print("Um status code diferente de 200 foi retornado!")
        print(e.status_code)
        print(e.response)

def gerar_parecer(transacao):
    print("2. Gerando parecer para transacao ", transacao["id"])
    prompt_sistema = f"""
    Para a seguinte transação, forneça um parecer, apenas se o status dela for de "Possível Fraude". Indique no parecer uma justificativa para que você identifique uma fraude.
    Transação: {transacao}

    ## Formato de Resposta
    "id": "id",
    "tipo": "crédito ou débito",
    "estabelecimento": "nome do estabelecimento",
    "horario": "horário da transação",
    "valor": "R$XX,XX",
    "nome_produto": "nome do produto",
    "localizacao": "cidade - estado (País)"
    "status": "",
    "parecer" : "Colocar Não Aplicável se o status for Aprovado"
    """
    modelo = "claude-3-5-sonnet-20240620"
    try:
        
        lista_mensagens = client.messages.create(
            model=modelo,
            max_tokens=4000,
            # temperature=0,
            # system=prompt_sistema,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt_sistema
                        }
                    ]
                }
            ]
        )
        conteudo = lista_mensagens.content[0].text
        print("Finalizou a geração de parecer")
        return conteudo
    except anthropic.APIConnectionError as e:
        print("Não foi possivel se conectar ao servidor")
        print(e.__cause__) 
    except anthropic.RateLimitError as e:
        print("Espere um tempo! Seu limite foi atingido.")
    except anthropic.APIStatusError as e:
        print("Um status code diferente de 200 foi retornado!")
        print(e.status_code)
        print(e.response)

lista_de_transacoes = carrega("transacoes.csv")
transacoes_analisadas = analisar_transacao(lista_de_transacoes)

for uma_transacao in transacoes_analisadas["transacoes"]: 
    if uma_transacao["status"] == "Possível Fraude": 
        um_parecer = gerar_parecer(uma_transacao)
        print(um_parecer)