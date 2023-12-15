# Utiliser une image de base avec Python
FROM python:3.11-slim

# Créer et définir le répertoire de travail
WORKDIR /app

# Copier le fichier des dépendances et installer avant de copier le reste
COPY requirements.txt .

# Installer les dépendances avant de copier le reste du code source
RUN pip install --no-cache-dir -r requirements.txt

# Copier le contenu local dans le conteneur à /app
COPY . .

# Exposer le port sur lequel l'application va écouter
EXPOSE 8000

# Commande pour exécuter l'application lorsque le conteneur démarre
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
