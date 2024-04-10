# Image python de base
FROM python:3.9

# Répertoire de travail
WORKDIR /app

# Copier le fichier des dépendances dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers du répertoire courant dans le répertoire de travail
COPY . .

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 9090

# Définir la commande pour exécuter l'application
CMD ["python", "app.py"]
