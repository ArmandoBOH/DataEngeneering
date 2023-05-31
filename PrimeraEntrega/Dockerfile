FROM python:3.8.0-slim

COPY ./app/requirements.txt /app/
WORKDIR /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/src /app/src/
WORKDIR /app/src/

CMD ["python", "main.py"]