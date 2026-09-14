# Pāṇini Engine v3 API — one process, no database, no state.
FROM python:3.12-slim
WORKDIR /app
COPY requirements-api.txt .
RUN pip install --no-cache-dir -r requirements-api.txt
# Only what the engine needs at runtime (~40 MB); tests/docs/web UI stay out.
COPY engine/ engine/
COPY sutras/ sutras/
COPY pipelines/ pipelines/
COPY phonology/ phonology/
COPY core/ core/
COPY data/ data/
COPY api/ api/
ENV PYTHONUNBUFFERED=1 PORT=8000
CMD ["sh", "-c", "uvicorn api.main:app --host 0.0.0.0 --port ${PORT}"]
