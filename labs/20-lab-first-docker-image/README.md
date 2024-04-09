# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`
docker run -d -p 80:80 --name mynginx1 nginx
2. Check that the nginx page (localhost:80)
Welcome to nginx!
If you see this page, the nginx web server is successfully installed and working. Further configuration is required.

For online documentation and support please refer to nginx.org.
Commercial support is available at nginx.com.

Thank you for using nginx.
3. Run a shell without stopping the Container
$ winpty docker exec -it mynginx1 /bin/bash (ca n'a pas marché a cause de chemin spécifier )

r (rabah_AZI/docker/labs)
$ winpty docker exec -it mynginx1 sh


4. Update the file `/usr/share/nginx/html/index.html` in the container

echo "Hello, this is my custom Nginx home page!" > /usr/share/nginx/html/index.html

5. Check that the nginx page has been updated (localhost:80)
Hello, this is my custom Nginx home page! est ecrit dans la page 

6. Create a transitive image named `my_awsome_image`
abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker (rabah_AZI/docker/labs)
$ docker commit mynginx1 my_awesome_image
sha256:8b2f24f49dfa3f8fa1e02d07f4085148f6b802d391e4f8f58430f9c00310ea4b

abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker (rabah_AZI/docker/labs)
$

7. Run the new image
abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker (rabah_AZI/docker/labs)
$ docker run -d -p 8080:80 --name customnginx my_awesome_image
14c7c7a8285955994cb7fb5da5db9af51a01a3c886a2c348c225d84b81f74ebc

le conteneur basé sur l'image my_awesome_image a été démarré avec succès, comme indiqué par l'ID du conteneur retourné (14c7c7a8285955994cb7fb5da5db9af51a01a3c886a2c348c225d84b81f74ebc). Ce conteneur est maintenant en cours d'exécution en arrière-plan, avec le port 8080 de ma machine mappé sur le port 80 du conteneur. Cela signifie que'on peut' accéder à mon Nginx personnalisé en allant à http://localhost:8080 depuis un navigateur web.
8. Check that the modifications are still present (localhost:80)
9. Check the layer with the `docker history` command
abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker (rabah_AZI/docker/labs)
$ docker history my_awesome_image
IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
8b2f24f49dfa   7 minutes ago   nginx -g daemon off;                            1.14kB
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

Dans ce cas, l'entrée la plus récente (8b2f24f49dfa) représente les modifications que j'ai apportées à l'image originale nginx, avec la commande nginx -g daemon off; indiquée dans le champ CREATED BY. Cette commande semble un peu hors contexte, probablement due à une interprétation automatique de Docker sur le dernier état du conteneur. Normalement, cette commande devrait refléter la dernière action effectuée dans le conteneur avant le commit, mais ici, elle répète simplement la commande par défaut pour exécuter nginx. La taille ajoutée (1.14kB) est la modification du fichier index.html.

Les autres couches sont celles héritées de l'image nginx d'origine, montrant les différentes étapes de construction de l'image nginx, comme l'ajout de fichiers, l'exécution de commandes, et la définition d'environnements ou d'autres métadonnées.

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`
2. List your docker images
   1. What do you see ?
3. Use the CLI to log into your docker account
4. Push your image
5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`