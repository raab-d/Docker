# Définir l'image de base
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances dans le répertoire de travail
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le reste des fichiers de l'application dans le répertoire de travail
COPY . /app/

# Exposer le port sur lequel l'application écoute
EXPOSE 9090

# Commande pour exécuter l'application
CMD ["python", "app.py"]
