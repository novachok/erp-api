FROM python:3.10-slim-buster
WORKDIR /src

COPY pyproject.toml poetry.lock /src/

RUN python -m pip install poetry && \
    poetry config virtualenvs.create false && \
    python -m pip install uvicorn
    poetry install --no-dev

COPY src/app /src
EXPOSE 8000

HEALTHCHECK --interval=5m --timeout=1s CMD curl --fail http://localhost:8000/status || exit 1

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]

