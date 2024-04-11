# Image Python
FROM python:3.8

# Maintainer et version
LABEL maintainer="jeanmarc.zhou@gmail.com"
LABEL version="1.0"

# Copier requirements.txt vers /app/requirements.txt
COPY requirements.txt /app/requirements.txt

# Working directory
WORKDIR /app

# Installer les packages contenus dans requirements.txt
RUN pip install -r requirements.txt

# Copier app.py dans /app
COPY app.py /app

# Port 9090 
EXPOSE 9090

# Exécution app.py au lancement du container
CMD ["python", "app.py"]



