FROM python:3.8-slim

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app

EXPOSE 9090

LABEL maintainer="Leonardo <enzoleonardo@hotmail.fr>"
LABEL version="1.0"

CMD ["python", "app.py"]