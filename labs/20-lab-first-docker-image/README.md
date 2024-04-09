# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`
# docker run --name mynginx1 -d -p 80:80 nginx

2. Check that the nginx page (localhost:80)
# http://localhost:80 shows welcome to nginx

3. Run a shell without stopping the Container
# docker exec -it mynginx1 /bin/bash

4. Update the file `/usr/share/nginx/html/index.html` in the container
# echo 'Hello, this is my custom Nginx page!' > /usr/share/nginx/html/index.html

5. Check that the nginx page has been updated (localhost:80)
#  i see a blank page with the text written "Hello, this is my custom Nginx page!"

6. Create a transitive image named `my_awsome_image`
# docker commit mynginx1 my_awsome_image 
# sha256:854adbbb1ebbf74204c8255a24c131b2da27be8dea8edf5c1134d578ea82f9f0

7. Run the new image
# docker run --name mynginx2 -d -p 81:80 my_awsome_image
# d744600d12273141b5e689d426b2cbb12083b6f8e35b7aecc14a18814e864b83

8. Check that the modifications are still present (localhost:80)
# Changes still present on the page

9. Check the layer with the `docker history` command
# docker history my_awsome_image
# 854adbbb1ebb   About a minute ago   nginx -g daemon off;                            1.38kB
# 92b11f67642b   7 weeks ago          CMD ["nginx" "-g" "daemon off;"]                0B        buildkit.dockerfile.v0        
# <missing>      7 weeks ago          STOPSIGNAL SIGQUIT                              0B        buildkit.dockerfile.v0        
# <missing>      7 weeks ago          EXPOSE map[80/tcp:{}]                           0B        buildkit.dockerfile.v0        
# <missing>      7 weeks ago          ENTRYPOINT ["/docker-entrypoint.sh"]            0B        buildkit.dockerfile.v0      



### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`
# docker tag my_awsome_image nadim1/my_awsome_image:1.0

2. List your docker images
# docker images

   1. What do you see ?
   # REPOSITORY               TAG       IMAGE ID       CREATED         SIZE
   # my_awsome_image          latest    854adbbb1ebb   4 minutes ago   187MB
   # nadim1/my_awsome_image   1.0       854adbbb1ebb   4 minutes ago   187MB
   # nginx                    latest    92b11f67642b   7 weeks ago     187MB

3. Use the CLI to log into your docker account
# docker login
# Authenticating with existing credentials...
# Login Succeeded

4. Push your image
# The push refers to repository [docker.io/nadim1/my_awsome_image]
# 900f312d12da: Pushed
# fd31601f0be4: Mounted from library/nginx
# 93b4c8c4ac05: Mounted from library/nginx
# b7df9f234b50: Mounted from library/nginx
# ab75a0b61bd1: Mounted from library/nginx
# c1b1bf2f95dc: Mounted from library/nginx
# 4d99aab1eed4: Mounted from library/nginx
# a483da8ab3e9: Mounted from library/nginx
# 1.0: digest: sha256:47a41449f4280965d5d363b723c9d2a575731f72bd5a91f106e98e830c77f9c7 size: 1986

5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
# i found my image "nadim1/my_awsome_image Updated less than a minute ago"
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`
# deleted