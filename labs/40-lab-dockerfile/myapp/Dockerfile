# Utiliser une image Python comme image de base
FROM python:3.8-slim

# Définir le mainteneur et la version du Dockerfile
LABEL maintainer="your-email@example.com"
LABEL version="1.0"

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier requirement.txt dans le répertoire de travail
COPY requirements.txt /app/requirements.txt

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier app.py dans le répertoire de travail
COPY app.py /app

# Spécifier que le conteneur écoute sur le port 9090
EXPOSE 9090

# Commande pour exécuter l'application
CMD ["python", "app.py"]
