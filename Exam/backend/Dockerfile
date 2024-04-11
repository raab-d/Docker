# Utiliser une image Python officielle
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances et installer les dépendances
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port utilisé par l'API
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["uvicorn", "back_end:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]