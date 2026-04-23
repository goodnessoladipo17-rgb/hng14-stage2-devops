FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
RUN useradd -m appuser
COPY --from=builder /root/.local /home/appuser/.local
COPY worker.py .
USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379
CMD ["python", "worker.py"]