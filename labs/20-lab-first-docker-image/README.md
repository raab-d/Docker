# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1` <br>
   docker run -d -p 80:80 --name mynginx1 nginx
2. Check that the nginx page (localhost:80) <br>
   http://localhost:80
3. Run a shell without stopping the Container <br>
   docker exec -it mynginx1 /bin/bash
4. Update the file `/usr/share/nginx/html/index.html` in the container <br>
   apt-get update <br>
   apt-get install nano <br>
   nano /usr/share/nginx/html/index.html
5. Check that the nginx page has been updated (localhost:80) <br>
   Welcome to nginx Erwan Duprey!
6. Create a transitive image named `my_awsome_image` <br>
   docker commit mynginx1 nanoerwanduprey
7. Run the new image <br>
   Need to close the first container first ! <br>
8. Check that the modifications are still present (localhost:80)
9. Check the layer with the `docker history` command <br>
   docker history nanoerwanduprey <br>
   C:\Users\erwan\Desktop\ESGI\S10\Docker-Kubernetes\Docker\labs\10-lab-hands-on-docker>docker history nanoerwanduprey <br>
   IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT <br>
   ad4ce547ac22   9 minutes ago   nginx -g daemon off;                            61.9MB 

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0` <br>
   docker tag nanoerwanduprey erwanduprey/nanoerwanduprey:1.0
2. List your docker images <br>
   docker images
   1. What do you see ? <br>
   C:\Users\erwan\Desktop\ESGI\S10\Docker-Kubernetes\Docker\labs\10-lab-hands-on-docker>docker images <br>
   REPOSITORY                                      TAG              IMAGE ID       CREATED          SIZE <br>
   erwanduprey/nanoerwanduprey                     1.0              ad4ce547ac22   16 minutes ago   249MB <br>
   nanoerwanduprey                                 latest           ad4ce547ac22   16 minutes ago   249MB
3. Use the CLI to log into your docker account <br>
   docker login
4. Push your image <br>
   docker push erwanduprey/nanoerwanduprey:1.0
5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/` <br>
   https://hub.docker.com/repository/docker/erwanduprey/nanoerwanduprey/
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings` <br>
   https://hub.docker.com/repository/docker/erwanduprey/nanoerwanduprey/settings <br>
   Please type the name of your repository to confirm deletion: nanoerwanduprey