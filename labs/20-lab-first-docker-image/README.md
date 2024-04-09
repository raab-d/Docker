# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`
docker run --name mynginx1 -d -p 80:80 nginx
bf6d6eb721c2fc92b84316ec9c2f119cc9dad5293c251913bec651b7246cd69d

2. Check that the nginx page (localhost:80)
http://localhost:80

3. Run a shell without stopping the Container
docker exec -it mynginx1 bash

4. Update the file `/usr/share/nginx/html/index.html` in the container
   /# echo "NGINX Page" > /usr/share/nginx/html/index.html

5. Check that the nginx page has been updated (localhost:80)
http://localhost:80

6. Create a transitive image named `my_awsome_image`
docker commit mynginx1 my_awsome_image
sha256:f13dd1e3fa8cbafe8cd5364da74711a1b8b3896568569554e4abbdac19b30b92

7. Run the new image
docker run --name mynginx2 -d -p 80:80 my_awsome_image
23072d11bee0deb0fba90e094a34a6315b28ef7535847f867160ae2c58afb323
docker: Error response from daemon: driver failed programming external connectivity on endpoint mynginx2 (313c986fa8a828693d912e0ba4be3b6ecf67bfe9e534112da94aa33b020e94be): Bind for 0.0.0.0:80 failed: port is already allocated.
Il faut allouer sur un nouveau port

8. Check that the modifications are still present (localhost:80)

9. Check the layer with the `docker history` command
docker history my_awsome_image

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`
   docker tag my_awsome_image nadya77/my_awsome_image:1.0

2. List your docker images
   docker images
   1. What do you see ?
      docker images                                         
      REPOSITORY                                      TAG                    IMAGE ID       CREATED          SIZE
      desktop/my_awsome_image                         1.0                    0b0be652d2bb   7 minutes ago    192MB
3. Use the CLI to log into your docker account
   docker login
   Authenticating with existing credentials...
   Login Succeeded
4. Push your image
   docker push nadya77/my_awesome_image:1.0
5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
https://hub.docker.com/repository/docker/nadya77/my_awesome_image/
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`
https://hub.docker.com/repository/docker/nadya77/my_awesome_image/settings