FROM python:3.14.4-slim-trixie

WORKDIR /app

COPY ./requirements.txt ./

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir --upgrade  -r requirements.txt

COPY . .

CMD ["fastapi", "run", "main.py", "--port", "80"]