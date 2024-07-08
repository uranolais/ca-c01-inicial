import anthropic
import dotenv 
import os

dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
modelo = "claude-3-5-sonnet-20240620"
prompt_sistema = "Classifique o produto abaixo em uma das categorias: Bebida, Comida Salgada e Comida Doce. Dê uma descrição da categoria."

message = client.messages.create(
    model= modelo,
    max_tokens=1000, #100
    temperature=0,
    # stop_sequences = ["Descrição"],
    system=prompt_sistema,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Sorvete de Chocolate"
                }
            ]
        }
    ]
)
conteudo_texto = message.content[0].text 
print(conteudo_texto)