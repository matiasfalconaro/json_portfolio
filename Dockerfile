FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias del sistema y Bun
RUN apt-get update && apt-get install -y --no-install-recommends curl git unzip && rm -rf /var/lib/apt/lists/* && curl -fsSL https://bun.sh/install | bash && mv /root/.bun/bin/bun /usr/local/bin/

# Copiar requirements primero para aprovechar cache de Docker
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Variables de entorno
ENV LOGLEVEL=debug
ENV FRONTEND_PORT=3000
ENV BACKEND_PORT=8000
ENV PYTHONPATH=/app

# Exponer puertos
EXPOSE 3000
EXPOSE 8000

# Comando de ejecución
CMD ["reflex", "run", "--env", "prod", "--loglevel", "debug", "--frontend-host", "0.0.0.0", "--backend-host", "0.0.0.0", "--port", "3000", "--backend-port", "8000"]
