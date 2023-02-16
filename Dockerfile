# Reference: https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
FROM python:3.11-alpine3.17


ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.3.2

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "/bin/sh", "/app/entrypoint.sh" ]

