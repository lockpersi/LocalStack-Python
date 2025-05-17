FROM mcr.microsoft.com/devcontainers/python:3.11

# Atualiza pacotes base e instala dependências úteis
RUN apt-get update && apt-get install -y curl unzip

# Garante que ~/.local/bin (onde pip --user instala) esteja no PATH
ENV PATH="${PATH}:/root/.local/bin"