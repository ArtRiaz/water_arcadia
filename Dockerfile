FROM python:3.9
COPY requirements.txt requirements.txt
COPY . .
CMD ["python", "main.py"]
