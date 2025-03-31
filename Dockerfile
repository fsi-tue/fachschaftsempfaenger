FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN apk upgrade --update && \
    apk add --no-cache build-base libxml2-dev libxslt-dev jpeg-dev zlib-dev curl && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/cache/apk/*

# Create and switch to non-root user
RUN adduser -D appuser
USER appuser

# Copy application code last
COPY --chown=appuser:appuser . .
