FROM python:3.10.14-slim-bullseye

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
