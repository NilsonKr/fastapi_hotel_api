FROM python:3.14.4-slim-trixie AS base

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade  -r requirements.txt

## Dev env
FROM base AS dev

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0" ,"--port", "80"]

## Prod env
FROM base AS prod

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./app ./

CMD ["fastapi", "run", "main.py", "--port", "80"]
