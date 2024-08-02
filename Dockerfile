FROM python:3.10-buster

WORKDIR /app

COPY . .

RUN pip install --upgrade --no-cache-dir pip \
    && pip install --no-cache-dir --editable . \
    && pip list

RUN python app/manage.py collectstatic --noinput

ENTRYPOINT [ "python", "app/manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000
