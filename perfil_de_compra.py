import anthropic
import dotenv 
import os

dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

# def carrega(nome_do_arquivo):
#     try:
#         with open(nome_do_arquivo, "r") as arquivo:
#             dados = arquivo.read()
#             return dados
#     except IOError as e:
#         print(f"Erro: {e}")

prompt_sistema = f"""
Identifique o perfil de compra de comida para cada cliente a seguir

# Formato da Saída

cliente - perfil do cliente em um paragrafo
"""
prompt_usuario = f"""
cliente01: come sushi, tempura e sorvete mochi. 
cliente02: come hambúrguer, batata frita e milkshake de baunilha. 
cliente03: come pizza margherita, bruschetta e tiramisù. 
cliente04: come tacos, guacamole e churros. 
cliente05: come falafel, homus e baklava. 
"""

# prompt_usuario = carrega("./dados/lista_de_compras_100_clientes.csv")

modelo = "claude-3-5-sonnet-20240620"
message = client.messages.create(
    model=modelo,
    max_tokens=4096,
    temperature=0,
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

conteudo_texto = message.content[0].text
print(conteudo_texto)

quantidade_de_tokens = message.usage
# print(quantidade_de_tokens)
print(f"Tokens de Entrada: {quantidade_de_tokens.input_tokens}")
print(f"Tokens de Saída: {quantidade_de_tokens.output_tokens}")