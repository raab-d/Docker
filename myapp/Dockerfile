FROM python:3.8-slim
LABEL maintainer="Erwan Duprey"
LABEL version="1.0"
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py /app/
EXPOSE 9090
CMD ["python", "app.py"]
LABEL version="1.0"