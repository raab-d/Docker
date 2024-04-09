# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1` <br>
   docker run -d -p 80:80 --name mynginx1 nginx
2. Check that the nginx page (localhost:80)
3. Run a shell without stopping the Container <br>
   docker exec -it mynginx1 sh
4. Update the file `/usr/share/nginx/html/index.html` in the container <br>
   echo 'Hello World' > /usr/share/nginx/html/index.html
5. Check that the nginx page has been updated (localhost:80)
6. Create a transitive image named `my_awsome_image` <br>
   docker commit mynginx1 my_awsome_image
7. Run the new image <br>
   Il faut penser à changer le port avant de lancer le nouveau conteneur <br>
   docker container run -d -p 81:80 --name mynginx2 my_awsome_image
8. Check that the modifications are still present (localhost:80)
9. Check the layer with the `docker history` command <br>
   *docker history my_awsome_image* 
   La commande docker history permet de voir quelles sont les couches et quelles instructions ont été exécutées pour les créer.

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0` <br>
   *docker tag my_awsome_image malaiyoo/my_awsome_image:1.0*
2. List your docker images
   1. What do you see ? <br>
      On voit une ligne supplémentaire pour le tag qu'on vient de créer avec la même image id que my_awsome_image. 
3. Use the CLI to log into your docker account <br>
   *docker login*
4. Push your image <br>
   On doit bien renseigner le bon dockerHubId correspondant à notre compte sinon on aura un accès denied <br>
   *docker push malaiyoo/my_awsome_image:1.0*
5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`