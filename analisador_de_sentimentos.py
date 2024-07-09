import anthropic
import dotenv 
import os
import time

dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")

def analisador_sentimentos(produto):
    prompt_sistema = f"""
            Você é um analisador de sentimentos de avaliações de produtos.
            Escreva um parágrafo com até 50 palavras resumindo as avaliações e 
            depois atribua qual o sentimento geral para o produto.
            Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

            # Formato de Saída

            Nome do Restaurante:
            Resumo das Avaliações:
            Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
            Ponto fortes: lista com três bullets
            Pontos fracos: lista com três bullets
    """
    prompt_usuario = carrega(f"./dados/avaliacoes-{produto}.txt")
    print(f"Inicou a análise de sentimentos do produto {produto}")
    modelo = "claude-3-5-sonnet-20240620"

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
    conteudo_texto = lista_mensagens.content[0].text 
    # print(conteudo_texto)
    salva(f"./dados/analise-{produto}.txt", conteudo_texto)

analisador_sentimentos(produto="Restaurante de Comida Chinesa")