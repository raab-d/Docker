# Utilise une image Python comme base
FROM python:3.9

# Copie requirement.txt dans /app/requirements.txt
COPY requirements.txt /app/requirements.txt

# Définit /app comme répertoire de travail
WORKDIR /app

# Installe les dépendances Python en utilisant pip install -r <file>
RUN pip install -r requirements.txt

# Copie app.py à l'intérieur de /app
COPY app.py /app

# Spécifie que le conteneur utilise le port 9090
EXPOSE 9090

# Spécifie le mainteneur et la version du Dockerfile
LABEL maintainer="adem"
LABEL version="1.0"

# Assurez-vous que le conteneur exécute la commande `python app.py`
CMD ["python", "app.py"]
