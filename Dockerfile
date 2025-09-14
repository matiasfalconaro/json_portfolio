FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl git unzip && rm -rf /var/lib/apt/lists/* && curl -fsSL https://bun.sh/install | bash && mv /root/.bun/bin/bun /usr/local/bin/

COPY portfolio/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/portfolio/assets && \
    cp -r assets/* /app/portfolio/assets/ 2>/dev/null || true && \
    cp -r assets/* /app/ 2>/dev/null || true

ENV LOGLEVEL=debug
ENV FRONTEND_PORT=3000
ENV BACKEND_PORT=8000
ENV PYTHONPATH=/app/portfolio

EXPOSE 3000
EXPOSE 8000

CMD ["python", "-m", "reflex", "run", "--env", "prod", "--loglevel", "debug", "--frontend-host", "0.0.0.0", "--backend-host", "0.0.0.0", "--port", "3000", "--backend-port", "8000"]