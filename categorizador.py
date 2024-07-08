import anthropic
import dotenv 
import os

dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000, #100
    temperature=0,
    # stop_sequences = ["Descrição"],
    system="Classifique o produto abaixo em uma das categorias: Bebida, Comida Salgada e Comida Doce. Dê uma descrição da categoria.",
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