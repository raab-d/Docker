# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`
- docker run -d -p 80:80 --name mynginx1 nginx

2. Check that the nginx page (localhost:80)

3. Run a shell without stopping the Container
- docker exec -it mynginx1 /bin/bash

4. Update the file `/usr/share/nginx/html/index.html` in the container
- echo "Ma page Nginx personnalisée" > /usr/share/nginx/html/index.html

5. Check that the nginx page has been updated (localhost:80)
- Oui la page est à jour, on voit bien "Ma page Nginx personalisee"

6. Create a transitive image named `my_awsome_image`
- docker commit mynginx1 my_awesome_image

7. Run the new image
- docker run -d -p 81:80 --name mynginx2 my_awesome_image

8. Check that the modifications are still present (localhost:80)
- Oui, on voit bien affiché la même chose comme dans la 1ère image

9. Check the layer with the `docker history` command
- docker history my_awesome_image


### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`
- docker tag my_awesome_image amineould98/my_awesome_image:1.0

2. List your docker images
- docker images

   1. What do you see ?
   - On voit apparaître my_awesome_image et amineould98/my_awesome_image:1.0.

3. Use the CLI to log into your docker account
- docker login

4. Push your image
- docker push amineould98/my_awesome_image:1.0

5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`