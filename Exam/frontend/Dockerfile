# Utiliser une image Python officielle
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances et installer les dépendances
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port utilisé par Streamlit
EXPOSE 8501

# Commande pour démarrer l'application
CMD ["streamlit", "run", "front_end.py", "--server.port=8501", "--server.address=0.0.0.0"]