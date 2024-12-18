import os
import re
import PyPDF2

def extrair_texto_pdf(caminho_arquivo):
    texto = ""
    with open(caminho_arquivo, 'rb') as arquivo:
        leitor = PyPDF2.PdfReader(arquivo)
        for pagina in leitor.pages:
            texto += pagina.extract_text() or ""
    return texto

def extrair_numeros_whatsapp(texto):
    padrao = r"\(?\d{2,3}\)?[-.\s]?\d{4,5}[-.\s]?\d{4}"
    return re.findall(padrao, texto)

def buscar_palavras_chave(texto, palavras_chave):
    encontrados = [p for p in palavras_chave if p.lower() in texto.lower()]
    return encontrados

def identificar_nome(texto):
    linhas = texto.split("\n")
    for linha in linhas[:10]:
        if 1 < len(linha.split()) <= 10:
            return linha.strip()
    return "Nome não identificado"

def analisar_curriculos(pasta, palavras_chave):
    resultados = []
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.pdf'):
            caminho = os.path.join(pasta, arquivo)
            texto = extrair_texto_pdf(caminho)
            numeros = extrair_numeros_whatsapp(texto)
            palavras = buscar_palavras_chave(texto, palavras_chave)
            nome = identificar_nome(texto)
            if numeros and palavras:
                resultados.append({
                    "arquivo": arquivo,
                    "nome": nome,
                    "numeros": numeros,
                    "palavras": palavras
                })
    return resultados