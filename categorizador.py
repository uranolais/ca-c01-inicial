import anthropic
import dotenv 
import os

dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
modelo = "claude-3-5-sonnet-20240620"

def categoriza_alimento(nome_do_alimento,lista_de_categorias):
    prompt_sistema = f"""
    Você é um categorizador de alimentos.
    Você deve assumir as categorias presentes na lista abaixo.

    # Lista de Categorias Válidas
    {lista_de_categorias.split(",")}

    # Formato da Saída
    Produto: Nome do Produto
    Categoria: apresente a categoria do produto

    # Exemplo de Saída
    Produto: Maçã
    Categoria: Frutas
    """
    prompt_usuario = nome_do_alimento

    message = client.messages.create(
        model= modelo,
        max_tokens=500, #100
        temperature=0,
        # stop_sequences = ["Descrição"],
        system=prompt_sistema,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt_usuario,
                    }
                ]
            }
        ]
    )
    conteudo_texto = message.content[0].text 
    return conteudo_texto


categorias_validas = input("Informe as categorias válidas, separando por virgula: ")

while True:
    nome_do_alimento = input("Digite o nome do alimento: ")
    texto_resposta = categoriza_alimento(nome_do_alimento,categorias_validas)
    print(texto_resposta)