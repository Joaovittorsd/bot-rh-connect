# CurrículoBot

**CurrículoBot** é um sistema de automação para análise de currículos e envio de mensagens personalizadas via WhatsApp. Ele foi projetado para facilitar o processo de recrutamento, identificando candidatos com base em palavras-chave e enviando mensagens diretamente para seus números de contato extraídos dos currículos.

---

## 🚀 Funcionalidades

1. **Análise de Currículos**:
   - Lê currículos em formato PDF armazenados em uma pasta específica.
   - Procura por palavras-chave relevantes definidas pelo usuário.
   - Extrai informações como o nome do candidato e número de WhatsApp.

2. **Automação de Mensagens**:
   - Envia mensagens personalizadas via WhatsApp Web para os candidatos encontrados.
   - Mensagens podem incluir o nome do candidato e informações sobre a vaga.

3. **Relatório de Envios**:
   - Exibe no console os currículos analisados e as mensagens enviadas.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **PyPDF2**: Extração de texto de arquivos PDF.
- **re**: Para busca por palavras-chave e extração de números de telefone.
- **pywhatkit**: Integração com WhatsApp Web para envio de mensagens.

---

## 📦 Estrutura do Projeto

bot-rh-connect/ 
├── extrator_curriculos.py # Lê e analisa os currículos 
├── whatsapp_bot.py # Envia mensagens via WhatsApp Web 
├── main.py # Arquivo principal para executar o sistema 
├── curriculo/ # Pasta onde os PDFs dos currículos são armazenados
├── teste.py # Realiza os teste de leitura dos PDFs e apresenta no console
├── README.md # Documentação do projeto

## ⚙️ Como Configurar

### 1. Clone o Repositório
```bash
git clone https://github.com/Joaovittorsd/bot-rh-connect.git
cd bot-rh-connect 
```

### 2. Instale as Dependências
Certifique-se de que o Python 3.10+ está instalado. Em seguida, instale as bibliotecas necessárias:
```bash
pip install PyPDF2 pywhatkit
```

## ▶️ Como Usar

### 1. Coloque os Currículos:
    • Armazene os arquivos PDF na pasta curriculo/.

### 2. Configure o Arquivo Principal:
    • Edite o arquivo `main.py` para definir as palavras-chave e informações da vaga:

    pasta_curriculos = "curriculo"
    palavras_chave = [".NET"]
    vaga = "Desenvolvedor .NET"

### 3. Execute o Sistema:
    • Execute o arquivo `main.py`:
    
```bash
pip install PyPDF2 pywhatkit
```

