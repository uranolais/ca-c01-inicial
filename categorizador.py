import anthropic
import dotenv 
import os

dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
modelo = "claude-3-5-sonnet-20240620"
prompt_sistema = f"""
Você é um categorizador de alimentos.
Você deve assumir as categorias presentes na lista abaixo.

# Lista de Categorias Válidas
    - Frutas
    - Vegetais
    - Carnes
    - Grãos e Cereais
    - Laticínios
    - Bebidas
    - Doces e Sobremesas
    - Alimentos Processados

# Formato da Saída
Produto: Nome do Produto
Categoria: apresente a categoria do produto

# Exemplo de Saída
Produto: Maçã
Categoria: Frutas
"""
prompt_usuario = input("Forneça um alimento: ")

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
print(conteudo_texto)