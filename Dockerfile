# On utilise le même serveur Nginx que sur ton ordi
FROM nginx:alpine

# On copie tes fichiers de CV dans le dossier du serveur
COPY . /usr/share/nginx/html

# On expose le port 80 (standard pour le web)
EXPOSE 80