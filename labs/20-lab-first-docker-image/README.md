# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`
docker run -d -p 80:80 --name mynginx1 nginx

2. Check that the nginx page (localhost:80)
3. Run a shell without stopping the Container
docker exec -it mynginx1 bash

4. Update the file `/usr/share/nginx/html/index.html` in the container
5. Check that the nginx page has been updated (localhost:80)
6. Create a transitive image named `my_awsome_image`
docker commit mynginx1 my_awesome_image

7. Run the new image
docker run -d -p 81:80 --name myawesomecontainer my_awesome_image

8. Check that the modifications are still present (localhost:80)
9. Check the layer with the `docker history` command
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
9091f56347cd   44 seconds ago   nginx -g daemon off;                            1.23kB

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`

docker tag my_awesome_image <dockerHubId>/my_awesome_image:1.0
2. List your docker images
   1. What do you see ?
3. Use the CLI to log into your docker account
4. Push your image
The push refers to repository [docker.io/saids017/my_awesome_iamge]
619d337d85c0: Pushed
fd31601f0be4: Mounted from library/nginx
93b4c8c4ac05: Mounted from library/nginx
b7df9f234b50: Mounted from library/nginx
ab75a0b61bd1: Mounted from library/nginx
c1b1bf2f95dc: Mounted from library/nginx
4d99aab1eed4: Mounted from library/nginx
a483da8ab3e9: Mounted from library/nginx
1.0: digest: sha256:04b6b3c200aee04245e9c76dc498fa5a7b0dd42b83763c2f9b83a6ecea29ccaf size: 1986
5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`