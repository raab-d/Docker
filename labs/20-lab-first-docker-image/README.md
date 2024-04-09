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
2125b32b2f9d87c466c39197e67966eaea109729fb7b6da57ed1034f46c12c16

2. Check that the nginx page (localhost:80)

J'ai ouvert le navigateur et il y avait une page d'accueil nginx à l'adresse "http://localhost:80"

3. Run a shell without stopping the Container

docker exec -it mynginx1 /bin/bash

4. Update the file `/usr/share/nginx/html/index.html` in the container

root@2125b32b2f9d:/# echo "Inspecteur Modification attention !!!" > /usr/share/nginx/html/index.html
bash: !!: event not found
root@2125b32b2f9d:/# echo "Inspecteur Modification attention !" > /usr/share/nginx/html/index.html
root@2125b32b2f9d:/# exit
exit

5. Check that the nginx page has been updated (localhost:80)

Inspecteur Modification attention !

6. Create a transitive image named `my_awsome_image`

docker commit mynginx1 my_awesome_image
sha256:d107e72bdeaebdbf33d69760e07407a509dcf3b91b56e91bd5176392292b9c0c

7. Run the new image

docker run -d -p 81:80 --name mynginx2 my_awesome_image
23bb683d94b2dcf733fe43fc5121ab98d1247c9d9ad069d25dc14130017b8b27

8. Check that the modifications are still present (localhost:80)

Nous avons toujours le message "Inspecteur Modification attention !"

9. Check the layer with the `docker history` command

docker history my_awesome_image
IMAGE          CREATED              CREATED BY                                      SIZE      COMMENT
d107e72bdeae   About a minute ago   nginx -g daemon off;                            1.21kB
92b11f67642b   7 weeks ago          CMD ["nginx" "-g" "daemon off;"]                0B        buildkit.dockerfile.v0
<missing>      7 weeks ago          STOPSIGNAL SIGQUIT                              0B        buildkit.dockerfile.v0
<missing>      7 weeks ago          EXPOSE map[80/tcp:{}]                           0B        buildkit.dockerfile.v0
<missing>      7 weeks ago          ENTRYPOINT ["/docker-entrypoint.sh"]            0B        buildkit.dockerfile.v0
<missing>      7 weeks ago          COPY 30-tune-worker-processes.sh /docker-ent…   4.62kB    buildkit.dockerfile.v0
<missing>      7 weeks ago          COPY 20-envsubst-on-templates.sh /docker-ent…   3.02kB    buildkit.dockerfile.v0
<missing>      7 weeks ago          COPY 15-local-resolvers.envsh /docker-entryp…   336B      buildkit.dockerfile.v0
<missing>      7 weeks ago          COPY 10-listen-on-ipv6-by-default.sh /docker…   2.12kB    buildkit.dockerfile.v0
<missing>      7 weeks ago          COPY docker-entrypoint.sh / # buildkit          1.62kB    buildkit.dockerfile.v0
<missing>      7 weeks ago          RUN /bin/sh -c set -x     && groupadd --syst…   112MB     buildkit.dockerfile.v0
<missing>      7 weeks ago          ENV PKG_RELEASE=1~bookworm                      0B        buildkit.dockerfile.v0
<missing>      7 weeks ago          ENV NJS_VERSION=0.8.3                           0B        buildkit.dockerfile.v0
<missing>      7 weeks ago          ENV NGINX_VERSION=1.25.4                        0B        buildkit.dockerfile.v0
<missing>      7 weeks ago          LABEL maintainer=NGINX Docker Maintainers <d…   0B        buildkit.dockerfile.v0
<missing>      7 weeks ago          /bin/sh -c #(nop)  CMD ["bash"]                 0B
<missing>      7 weeks ago          /bin/sh -c #(nop) ADD file:b86ae1c7ca3586d8f…   74.8MB


### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`

docker tag my_awesome_image zhoupinou/my_awsome_image:1.0

2. List your docker images
   1. What do you see ?

   docker images
   REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
   my_awesome_image            latest    d107e72bdeae   7 minutes ago   187MB
   zhoupinou/my_awsome_image   1.0       d107e72bdeae   7 minutes ago   187MB
   nginx                       latest    92b11f67642b   7 weeks ago     187MB

   On voit l'image nginx, my_awesome_image et la nouvelle image dont le tag a été modifié. De plus, sous la colonne TAG, il y a la version 1.0. Les IMAGE ID sont identiques aussi. 

3. Use the CLI to log into your docker account

docker login dckr_pat_e3LW5ERvWe4wHOsAvtAL-5MqhHE
Username: zhoupinou
Password:

Error response from daemon: Get "https://dckr_pat_e3LW5ERvWe4wHOsAvtAL-5MqhHE/v2/": dialing dckr_pat_e3LW5ERvWe4wHOsAvtAL-5MqhHE:443 container via direct connection because  has no HTTPS proxy: resolving host dckr_pat_e3LW5ERvWe4wHOsAvtAL-5MqhHE: lookup dckr_pat_e3LW5ERvWe4wHOsAvtAL-5MqhHE: no such host

4. Push your image

Push effectué manuellement sur le client.

5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`

6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`