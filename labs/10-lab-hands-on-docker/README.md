# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry  =====> docker pull busybox
- Pull `busybox` from the gitlab registry   =====> docker pull registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox

1. What is the default registry ?
   Docker Hub est le registre par défaut pour Docker, utilisé pour stocker et télécharger des images Docker. Il facilite l'accès aux images officielles et permet aux utilisateurs de partager leurs propres images. Lorsqu'aucun registre n'est spécifié, Docker cherche les images sur Docker Hub par défaut.

2. What is the différence between these images ?
   Le nombre ou les volumes d'images peuvent différer entre les registres, où l'un peut offrir plus d'images ou une plus grande variété que l'autre. Cela peut résulter de contributions spécifiques au registre ou de politiques de stockage différentes.

3. Remove all images that aren't from the default registry. =======> docker rmi registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox
   (base) benadem@eaitinoMacBook-Pro Docker % docker rmi registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox
   Untagged: registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox:latest
   Untagged: registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox@sha256:2376a0c12759aa1214ba83e771ff252c7b1663216b192fbe5e0fb364e952f85c
   Deleted: sha256:5242710cbd55829f6c44b34ff249913bb7cee748889e7e6925285a29f126aa78
   Deleted: sha256:feb4513d4fb7052bcff38021fc9ef82fd409f4e016f3dff5c20ff5645cde4c02

## Work with container

1. Run a busybox container =====> docker run busybox
   1. What happend ? =====> Aucun retour sur la ligne de commande, car aucune commande n'est spécifiée pour maintenir le conteneur en cours d'exécution.
   2. Fix it with a sleep =====> docker run busybox sleep 15  
2. Run a busybox container that said "Hello world" ========> docker run busybox echo "Hello world"
3. Instantiate an interactive shell with busybox   ========> Docker % docker run -it busybox sh
   1. Run a Hello world inside the container   ========>  / # echo "Hello world"
   2. Leave the container =====> exit 
   3. What happened ? =======> Le conteneur se ferme car le processus interactif est terminé avec la commande exit.
4. Run a container in background that say "Hello world" ========>  docker run -d busybox sh -c "echo 'Hello world'" / j'ai eu ce retour caca8ea47011d19fa337c3f41014600051136b426fad07b17b7ad965aadd4665
5. Find the container id 
docker ps -lq
caca8ea47011
6. Print the container logs 
docker logs caca8ea47011  
Hello world
7. Stop the container =========> docker stop caca8ea47011 
8. List all container =====> docker ps
   1. What happend ? =======> la commande retourne tout les conteneurs en cours d'exécution.
   2. List all container even the one that is stopped ======> docker ps -a
9. Delete the stopped container  =======> docker rm caca8ea47011 
10. Delete all stopped containers =======> docker container prune

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop =======> docker run --rm -it -v "$(pwd):/app" busybox sh
   1. Create a txt file with "Hello" ========> echo "Hello" > hello.txt
   2. Exit the container  ========> exit
2. Re-run the container ===========> docker run --rm -it -v "$(pwd):/app" busybox sh
3. Check the file =========> aucun retour.
4. What happened ? ========> le fichier hello.txt n'était plus présent car le conteneur a été recréé à partir de l'image Busybox initiale, sans tenir compte des modifications apportées lors de la première exécution(le fichier a ete supprime)

## Clean up

1. List all images ======> docker images
2. Delete busybox images ==========> Docker % docker rmi $(docker images -q busybox)

You can use the `prune` command
