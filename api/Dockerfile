FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim AS runner
WORKDIR /app
RUN useradd --create-home --shell /bin/bash appuser
COPY --from=builder /root/.local /home/appuser/.local
COPY . .
USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/docs')" || exit 1
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]