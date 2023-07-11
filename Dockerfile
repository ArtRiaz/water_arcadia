FROM python:3.9

WORKDIR /src
COPY requirements.txt /src
COPY . /src
