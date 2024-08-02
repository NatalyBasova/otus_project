FROM python:3.10-buster

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install --upgrade --no-cache-dir pip \
    && pip install --no-cache-dir --editable . \
    && pip list

RUN python app/manage.py collectstatic --noinput

WORKDIR /app/app

# ENTRYPOINT [ "python", "app/manage.py", "runserver", "0.0.0.0:8000" ]
ENTRYPOINT [ "gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000" ]