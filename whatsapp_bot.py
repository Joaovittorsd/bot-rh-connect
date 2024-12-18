import pywhatkit as kit

def enviar_mensagem(numero, mensagem):
    try:
        kit.sendwhatmsg_instantly("+55" + numero, mensagem)
        print(f"Mensagem enviada com sucesso para {numero}")
    except Exception as e:
        print(f"Erro ao enviar mensagem para {numero}: {e}")