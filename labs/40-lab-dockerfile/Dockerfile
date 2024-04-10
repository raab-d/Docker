# 1. Use a python image as base
FROM python:3.8

# 2. Copy `requirement.txt` in `/app/requirements.txt`
COPY requirements.txt /app/requirements.txt

# 3. Define `/app` as working directory
WORKDIR /app

# 4. Install python dependencies using `pip install -r <file>`
RUN pip install -r requirements.txt

# 5. Copy `app.py` inside `/app`
COPY app.py /app

# 6. Specify that the container use the port `9090`
EXPOSE 9090

# 7. Specify the maintainer and the version of the dockerfile
LABEL maintainer="nadya.dorosenco@gmail.com"
LABEL version="1.0"

# 8. Make sure the container will run the command `python app.py`
CMD ["python", "app.py"]
