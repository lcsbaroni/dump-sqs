FROM python:3.9.13-slim-bullseye

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app
