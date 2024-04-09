# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`
<br> docker run -d -p 80:80 --name mynginx1 nginx <br> Cette commande télécharge l'image nginx si nécessaire, puis lance un conteneur nommé mynginx1 en mode détaché (-d) en mappant le port 80 de l'hôte sur le port 80 du conteneur.
2. Check that the nginx page (localhost:80)
<br> L'adresse localhost:80 donne bien un résultat avec un front par default
3. Run a shell without stopping the Container
<br> docker exec -it mynginx1 /bin/bash
4. Update the file `/usr/share/nginx/html/index.html` in the container
echo "Nouvelle page de fou car c'est la vie 42!!" > /usr/share/nginx/html/index.html  , cela permet de modifier le fichier indiqué en rajoutant la ligne ce qui va remplacer le front par défaut.
5. Check that the nginx page has been updated (localhost:80)
<br> Cela fonctionne correctement avec le new front
6. Create a transitive image named `my_awsome_image`
<br> docker commit mynginx1 my_awsome_image
7. Run the new image
<br> docker run -d -p 81:80 my_awsome_image
8. Check that the modifications are still present (localhost:80)
<br> Cela montre que l'image transitoire a conservé les changements toutefois si je n'avais pas changé le port de la nouvelle image (81) cela m'aurait donnée une erreur, car on ne peut pas le faire une image de transitions sur le même port.
9. Check the layer with the `docker history` command
<br> docker history my_awsome_image   , cela permet de montré les layers de l'image

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`
<br> docker tag my_awsome_image julianalz42esgi/my_awsome_image:1.0
2. List your docker images
<br> docker images
   1. What do you see ? <br> On voit l'image my_awsome_image ainsi que son tag. <br> 
REPOSITORY                        TAG       IMAGE ID       CREATED          SIZE
julianalz42esgi/my_awsome_image   1.0       85e1fe04e728   10 minutes ago   187MB
my_awsome_image                   latest    85e1fe04e728   10 minutes ago   187MB
nginx                             latest    92b11f67642b   7 weeks ago      187MB

3. Use the CLI to log into your docker account
<br> docker login (pas besoins de donner mes ids car il a automatique détecter docker hub ou je suis deja connecter et donc les infos était dans le cache de mon ordinateur.)
4. Push your image
<br> docker push julianalz42esgi/my_awsome_image:1.0   Cela à push mon image sur Docker hub.
5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
<br> voici l'url: https://hub.docker.com/repository/docker/julianalz42esgi/my_awsome_image/general
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`