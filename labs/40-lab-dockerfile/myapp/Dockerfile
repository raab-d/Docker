FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 9090

LABEL maintainer="divino <monteiro.hugo2001@icloud.com>"
LABEL version="1.0"

ENTRYPOINT ["python"]
CMD [ "app.py" ]
