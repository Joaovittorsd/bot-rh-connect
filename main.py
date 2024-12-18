from extrator_curriculos import analisar_curriculos
from whatsapp_bot import enviar_mensagem

# Configurações
pasta_curriculos = "curriculo"
palavras_chave = [".NET"]
vaga = "Desenvolvedor .NET"

# Analisar currículos
resultados = analisar_curriculos(pasta_curriculos, palavras_chave)

# Enviar mensagens
for resultado in resultados:
    nome = resultado["nome"]
    for numero in resultado["numeros"]:
        mensagem = f"Olá, {nome} Temos uma vaga para {vaga}. Você tem interesse?"
        print(f"Enviando mensagem para {numero}...")
        enviar_mensagem(numero, mensagem)