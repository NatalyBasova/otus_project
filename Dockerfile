FROM python:3.10-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --editable .

ENTRYPOINT [ "docker-entrypoint.sh" ]

EXPOSE 8000
