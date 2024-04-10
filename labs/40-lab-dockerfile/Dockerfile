# Utiliser une image Python comme base
FROM python:3.8

# Définir le mainteneur et la version du Dockerfile
LABEL maintainer="lroque6@myges.com"
LABEL version="1.0"

# Copier requirement.txt dans /app/requirements.txt
COPY requirements.txt /app/requirements.txt

# Définir /app comme répertoire de travail
WORKDIR /app

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Copier app.py à l'intérieur de /app
COPY app.py /app

# Spécifier que le conteneur utilise le port 9090
EXPOSE 9090

# S'assurer que le conteneur exécute la commande python app.py
CMD ["python", "app.py"]
