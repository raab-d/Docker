# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1` ==========> docker run -d -p 80:80 --name mynginx1 nginx
2. Check that the nginx page (localhost:80) =====> bien installé.
3. Run a shell without stopping the Container ========> docker exec -it mynginx1 sh
4. Update the file `/usr/share/nginx/html/index.html` in the container 
5. Check that the nginx page has been updated (localhost:80) =======> Yes 
6. Create a transitive image named `my_awsome_image` ==========> docker commit mynginx1 my_awesome_image
7. Run the new image =====> docker run -d -p 8081:80 --name mynewnginx2 my_awesome_image, on ne peut pas la créer avec le meme port que l'image d'avant.
8. Check that the modifications are still present (localhost:80) ========> oui il y aura toujours les modifications, Il faut créer notre nouvelle image avec un nouveau numéro de port.
9. Check the layer with the `docker history` command ======> docker history my_awesome_image, oui elle existe bien.

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0` ==========>   docker tag my_awesome_image ademaitidir/my_awesome_image:1.0
2. List your docker images ========> docker images
   1. What do you see ? 
   Je vois une liste des images Docker sur mon système, y compris l'image que j'ai récemment taguée. Parmi elles, il y a une entrée pour ademaitidir/my_awesome_image avec le tag 1.0. Cette image a un ID spécifique, une taille, et une date de création. L'image originale my_awesome_image est également listée, potentiellement avec le tag latest. Il pourrait y avoir aussi des images sans tag (<none>).

3. Use the CLI to log into your docker account =======>  docker login
4. Push your image =========> docker push ademaitidir/my_awesome_image:1.0
5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`   ======> fait 
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings` ======> fait





 