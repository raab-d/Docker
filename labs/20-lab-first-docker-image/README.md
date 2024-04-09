# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`  
docker run -d -p 80:80 --name mynginx1 nginx  
Unable to find image 'nginx:latest' locally  
latest: Pulling from library/nginx  
8a1e25ce7c4f: Pull complete  
e78b137be355: Pull complete  
39fc875bd2b2: Pull complete  
035788421403: Pull complete  
87c3fb37cbf2: Pull complete  
c5cdd1ce752d: Pull complete  
33952c599532: Pull complete  
Digest: sha256:6db391d1c0cfb30588ba0bf72ea999404f2764febf0f1f196acd5867ac7efa7e  
Status: Downloaded newer image for nginx:latest  
26cd5b5d35fc6d5119330e5530672030f25e08b4eabfde766524ba0bf8eb2217  
2. Check that the nginx page (localhost:80)  
Welcome to nginx!  
If you see this page, the nginx web server is successfully installed and working. Further configuration is required.  
3. Run a shell without stopping the Container  
docker exec -it mynginx1 /bin/bash  
root@26cd5b5d35fc:/# ls  
bin   dev                  docker-entrypoint.sh  home  lib64  mnt  proc  run   srv  tmp  var
boot  docker-entrypoint.d  etc  
4. Update the file `/usr/share/nginx/html/index.html` in the container  
root@26cd5b5d35fc:/# echo "Test maj nginx" > /usr/share/nginx/html/index.html  
5. Check that the nginx page has been updated (localhost:80)  
Test maj nginx  
6. Create a transitive image named `my_awsome_image`  
docker commit mynginx1 my_awesome_image  
7. Run the new image  
docker run -d -p 80:80 --name newnginx my_awesome_image
c446468c32451c1830c7731e90a27ee455b7596f11f0e6bd46715311d978c062
8. Check that the modifications are still present (localhost:80)  
Test maj nginx
9. Check the layer with the `docker history` command  
docker history my_awesome_image  
IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT  
0a7d100c2708   2 minutes ago   nginx -g daemon off;                            1.17kB  
92b11f67642b   7 weeks ago     CMD ["nginx" "-g" "daemon off;"]                0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     STOPSIGNAL SIGQUIT                              0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     EXPOSE map[80/tcp:{}]                           0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     ENTRYPOINT ["/docker-entrypoint.sh"]            0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     COPY 30-tune-worker-processes.sh /docker-ent…   4.62kB    buildkit.dockerfile.v0  
<missing>      7 weeks ago     COPY 20-envsubst-on-templates.sh /docker-ent…   3.02kB    buildkit.dockerfile.v0  
<missing>      7 weeks ago     COPY 15-local-resolvers.envsh /docker-entryp…   336B      buildkit.dockerfile.v0  
<missing>      7 weeks ago     COPY 10-listen-on-ipv6-by-default.sh /docker…   2.12kB    buildkit.dockerfile.v0  
<missing>      7 weeks ago     COPY docker-entrypoint.sh / # buildkit          1.62kB    buildkit.dockerfile.v0  
<missing>      7 weeks ago     RUN /bin/sh -c set -x     && groupadd --syst…   112MB     buildkit.dockerfile.v0  
<missing>      7 weeks ago     ENV PKG_RELEASE=1~bookworm                      0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     ENV NJS_VERSION=0.8.3                           0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     ENV NGINX_VERSION=1.25.4                        0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     LABEL maintainer=NGINX Docker Maintainers <d…   0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     /bin/sh -c #(nop)  CMD ["bash"]                 0B  
<missing>      7 weeks ago     /bin/sh -c #(nop) ADD file:b86ae1c7ca3586d8f…   74.8MB  

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`  
docker commit mynginx1 davidzer/my_awesome_image:1.0  
ccc7bb151f237502804c99fc6b2585b593410e80717d39c2a5c1339d5de8830b
2. List your docker images
   1. What do you see ?  
   REPOSITORY         TAG       IMAGE ID       CREATED         SIZE  
   my_awesome_image   1.0       7c81e4aac041   8 seconds ago   187MB  
   my_awesome_image   latest    0a7d100c2708   4 minutes ago   187MB  
   nginx              latest    92b11f67642b   7 weeks ago     187MB  
3. Use the CLI to log into your docker account
4. Push your image
5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
https://hub.docker.com/r/davidzer/my_awesome_image
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`
repository supprimer depuis le hub