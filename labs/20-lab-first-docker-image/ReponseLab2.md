# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`
 docker run --name mynginx1 -d -p 80:80 nginx

2. Check that the nginx page (localhost:80)
http://localhost:80

3. Run a shell without stopping the Container
winpty docker exec -it mynginx1 /bin/bash

4. Update the file `/usr/share/nginx/html/index.html` in the container
echo 'Salut tous le monde' > /usr/share/nginx/html/index.html

5. Check that the nginx page has been updated (localhost:80)
repartir sur le lien http://localhost:80
6. Create a transitive image named `my_awsome_image`
   $ docker commit mynginx1 my_awesome_image
      sha256:6e9444f8a9858d2f16521a007486af35a058a0ac900893594833440c3dccf390
7. Run the new image
docker run --name myawesomecontainer -d -p 8o:80 my_awesome_image

8. Check that the modifications are still present (localhost:80)
on ne peux pas créer sur le même port que Nginx car cela créer un conflit

9. Check the layer with the `docker history` command
docker history my_awesome_image

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`
docker tag my_awesome_image kinsley94/my_awesome_image:1.0

2. List your docker images
docker images
   1. What do you see ?
   je voie l'image que j'ai créer 
3. Use the CLI to log into your docker account
   $ docker login
   Authenticating with existing credentials...
   Login Succeeded

4. Push your image
docker push kinsley94/my_awesome_image:1.0


5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
https://hub.docker.com/repository/docker/<dockerHubId>/my_awesome_image/
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`
https://hub.docker.com/repository/docker/<dockerHubId>/my_awesome_image/settings