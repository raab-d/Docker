# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`

$ docker run -d -p 80:80 --name mynginx1 nginx
ou
$ docker run -d -p 8080:80 --name mynginx1 nginx (CAR PROBLEME DE PORT 80)
1ba77814e86e447ac16a1c1f234f7a59f116b10bb7d4b96b71d732ab4a962d64

** -d : Exécuter le conteneur en arrière-plan (mode détaché). **
** -p 80:80 : Rediriger le port 80 de l'hôte vers le port 80 du conteneur. **
** --name mynginx1 : Nommer le conteneur mynginx1. **
** nginx : L'image à utiliser (tirée depuis Docker Hub si elle n'est pas déjà présente localement). **

2. Check that the nginx page (localhost:80) -> (http://localhost:8080/)

- Sur un navigateur et allez à http://localhost:80. La page d'accueil par défaut de nginx.

3. Run a shell without stopping the Container

$ docker exec -it mynginx1 bash


4. Update the file `/usr/share/nginx/html/index.html` in the container


Une fois dans le shell du conteneur, j'exécute :
$ echo "Hello from my awesome image" > /usr/share/nginx/html/index.html


5. Check that the nginx page has been updated (localhost:80)

-> Refresh le navigateur sur http://localhost:80 pour voir les modifications.


6. Create a transitive image named `my_awsome_image`

$ docker commit mynginx1 my_awesome_image


7. Run the new image

$ docker run -d -p 81:80 --name mynginx2 my_awesome_image


8. Check that the modifications are still present (localhost:80)

-> Check sur : 'http://localhost:81'

9. Check the layer with the `docker history` command
$ docker history my_awesome_image


### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`

-> docker tag my_awesome_image <dockerHubId>/my_awesome_image:1.0


2. List your docker images
$ docker images

   1. What do you see ?
   ->  'my_awesome_image' ainsi que le tag nouvellement créé.


3. Use the CLI to log into your docker account
$ docker login


4. Push your image
$ docker push <dockerHubId>/my_awesome_image:1.0


5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
-> Ok

6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`

-> Pour des raisons de sécurité et de nettoyage, il est suggéré de supprimer les images de test ou 
les dépôts non nécessaires de Docker Hub. Il faut aller sur
(https://hub.docker.com/repository/docker/<dockerHubId>/my_awesome_image/settings) et 
suivre les instructions pour supprimer le dépôt.