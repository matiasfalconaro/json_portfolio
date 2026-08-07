FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl git unzip netcat-openbsd && \
    rm -rf /var/lib/apt/lists/* && \
    curl -fsSL https://bun.sh/install | bash && \
    mv /root/.bun/bin/bun /usr/local/bin/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Make initialization script executable
RUN chmod +x scripts/docker_init.sh

ENV LOGLEVEL=debug
ENV FRONTEND_PORT=3000
ENV BACKEND_PORT=8000
ENV PYTHONPATH=/app

EXPOSE 3000
EXPOSE 8000

# Use the initialization script as the entrypoint
CMD ["bash", "scripts/docker_init.sh"]
