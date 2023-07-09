FROM python:3.9

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN chmod 755 .

COPY . .

