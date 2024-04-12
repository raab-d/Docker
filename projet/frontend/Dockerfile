# Build stage
FROM node:16-alpine as build
WORKDIR /app

# Nettoyer le cache npm
RUN npm cache clean --force

# Copier les fichiers package.json et package-lock.json dans le répertoire de travail
COPY package.json package-lock.json ./

# Installer les dépendances
RUN npm install

# Copier le reste du répertoire frontend dans le répertoire de travail
COPY . ./

# Construire l'application React
RUN npm run build

# Serve stage
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
