import os
import re
import PyPDF2

def extrair_texto_pdf(caminho_arquivo):
    """Extrai texto de um arquivo PDF."""
    texto = ""
    try:
        with open(caminho_arquivo, 'rb') as arquivo:
            leitor = PyPDF2.PdfReader(arquivo)
            for pagina in leitor.pages:
                texto += pagina.extract_text() or ""
    except Exception as e:
        print(f"Erro ao ler {caminho_arquivo}: {e}")
    return texto

def buscar_palavras_chave(texto, palavras_chave):
    """Busca palavras-chave no texto."""
    encontrados = [palavra for palavra in palavras_chave if palavra.lower() in texto.lower()]
    return encontrados

def extrair_numeros_whatsapp(texto):
    """Extrai números de telefone (WhatsApp) do texto."""
    padrao = r"\(?\d{2,3}\)?[-.\s]?\d{4,5}[-.\s]?\d{4}"
    return re.findall(padrao, texto)

def identificar_nome(texto):
    """Tenta identificar o nome do candidato no início do texto."""
    linhas = texto.split('\n')
    for linha in linhas[:10]:  # Buscar nas primeiras 10 linhas
        palavras = linha.split()
        if 1 < len(palavras) <= 10:  # Supõe que um nome tem entre 2 a 10 palavras
            return linha.strip()
    return "Nome não identificado"

def analisar_curriculos(pasta_curriculos, palavras_chave):
    """Análise de currículos na pasta."""
    if not os.path.exists(pasta_curriculos):
        print(f"Erro: A pasta '{pasta_curriculos}' não foi encontrada.")
        return
    
    print(f"Analisando currículos na pasta: {pasta_curriculos}")
    for arquivo in os.listdir(pasta_curriculos):
        if arquivo.endswith('.pdf'):
            caminho = os.path.join(pasta_curriculos, arquivo)
            print(f"Lendo arquivo: {arquivo}")  # Log de depuração
            
            texto = extrair_texto_pdf(caminho)
            if not texto.strip():
                print(f"Arquivo {arquivo} está vazio ou não foi possível extrair texto.")
                continue
            
            print(f"Texto extraído de {arquivo}:\n{texto[:300]}...\n")  # Imprime os primeiros 300 caracteres
            
            # Buscar palavras-chave
            palavras_encontradas = buscar_palavras_chave(texto, palavras_chave)
            
            # Extrair números de WhatsApp
            numeros = extrair_numeros_whatsapp(texto)
            
            # Identificar nome do candidato
            nome_candidato = identificar_nome(texto)
            
            if palavras_encontradas and numeros:
                print(f"Currículo encontrado: {arquivo}")
                print(f"Nome do candidato: {nome_candidato}")
                print(f"Palavras-chave encontradas: {palavras_encontradas}")
                print(f"Números de WhatsApp encontrados: {numeros}")
                print("-" * 50)
            else:
                print(f"Nenhuma palavra-chave ou número de WhatsApp encontrado no arquivo: {arquivo}")

# Configurações
pasta_curriculos = os.path.join(os.path.dirname(__file__), 'curriculo')
palavras_chave = [".NET"]

# Execução
analisar_curriculos(pasta_curriculos, palavras_chave)
