FROM python:3.11

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY app.py /app

EXPOSE 9090

LABEL maintainer="Essaid_Sayad_Docker"

LABEL version="1.0"

CMD ["python", "app.py"]