FROM python:3.9-alpine

RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev libffi-dev openssl-dev redis

WORKDIR /app

RUN git clone https://github.com/duver00/management.git


RUN pip install --update pip
RUN pip install-r repo/requirements.txt

COPY . .