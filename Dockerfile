# Use a imagem base do Python
FROM python:3.12.4

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo requirements.txt e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o restante do projeto para o container
COPY . .

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Rodar as migrações e o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
