FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 9090
LABEL maintainer="David Degaugue"
LABEL version=1.0.0
ENTRYPOINT ["python"]
CMD ["app.py"]
