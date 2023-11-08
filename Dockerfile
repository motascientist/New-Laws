# Use uma imagem base Python
FROM python:3.9

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt /app/

# Defina o diretório de trabalho
WORKDIR /app

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o arquivo scraper.py para o contêiner
COPY scraper.py /app/
COPY munincipios.txt /app/
COPY teste.txt /app/

# Configure as variáveis de ambiente para as credenciais da AWS

ENV AWS_ENV=dev
ENV AWS_ACCESS_KEY_ID="Your Acess Key ID"
ENV AWS_SECRET_ACCESS_KEY="Your Secret Access Key"
ENV AWS_DEFAULT_REGION="us-east-1" #Example

# Execute o script quando o contêiner for iniciado
CMD ["python", "scraper.py"]

