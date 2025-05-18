FROM mcr.microsoft.com/devcontainers/python:3.11

# Instala dependências básicas
RUN apt-get update && apt-get install -y curl unzip

# Instala localstack e boto3 globalmente (sem --user)
RUN pip install localstack boto3