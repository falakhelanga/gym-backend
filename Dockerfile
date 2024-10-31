# Build stage
FROM python:3.12-slim AS build-stage

WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev \  
    # Add this line to install PostgreSQL development package 
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
ENV POETRY_VERSION=1.4.2
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

# Copy project files
COPY poetry.lock pyproject.toml /app/


# Install dependencies with Poetry
RUN poetry install --no-dev --no-interaction --no-ansi

# Generate requirements.txt
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

COPY . .

# Final stage
FROM python:3.12-slim

LABEL maintainer="BigBrave"

ENV DJANGO_ENV=${DJANGO_ENV} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Copy scripts
COPY ./scripts /scripts

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libffi-dev libssl-dev cargo postgresql-client libpq-dev \
     # Add this line to install PostgreSQL client 
    && rm -rf /var/lib/apt/lists/*

# Create app user
RUN useradd -m app

WORKDIR /app

# Copy project files and requirements.txt from build stage
COPY --from=build-stage /app .
COPY --from=build-stage /app/requirements.txt .

# Create a virtual environment and install dependencies
RUN python3 -m venv /venv
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# Setup directories and permissions
RUN mkdir -p /vol/web/static /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

# Update PATH
ENV PATH="/scripts:/venv/bin:$PATH"

USER app

EXPOSE 8000

CMD ["/scripts/entrypoint.sh"]