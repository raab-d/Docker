# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry

1. What is the default registry ?
le dépot par défaut est le docker hub en passant par docker.io, c'est de la que sont téléchargé les images par défaut.
2. What is the différence between these images ?
l'image qui provient de gitlab est plus légère que celle de docker hub
3. Remove all images that aren't from the default registry.
docker image rm 5242710cbd55 (gitlab image)

## Work with container

1. Run a busybox container
   1. What happend ?
   Le conteneur se lance et se coupe instantanément
   2. Fix it with a sleep
   docker run busybox sleep 5
2. Run a busybox container that said "Hello world"
docker run busybox echo "Hello world"
3. Instantiate an interactive shell with busybox
   1. Run a Hello world inside the container
   docker run -it busybox sh
   / #
   / # echo "Hello World"
   Hello World
   2. Leave the container
   / # exit
   3. What happened ?
   on est retourné sur l'invite de commande windows et le conteneur s'est fermé.
4. Run a container in background that say "Hello world"
docker run -d -ti busybox echo Hello world
5. Find the container id
1d74212d2b4f6baf308d374f0c23501b38ed3d8692d0c1f00724a86e82fa2e67
6. Print the container logs
docker logs 1d74212d2b4f6baf308d374f0c23501b38ed3d8692d0c1f00724a86e82fa2e67
Hello world
7. Stop the container
docker stop 1d74212d2b4f6baf308d374f0c23501b38ed3d8692d0c1f00724a86e82fa2e67
8. List all container
docker ps
CONTAINER ID   IMAGE     COMMAND              CREATED         STATUS                     PORTS     NAMES
   1. What happend ?
   aucun container s'afficher car aucun n'est lancé
   2. List all container even the one that is stopped
   docker ps -a
   CONTAINER ID   IMAGE     COMMAND              CREATED         STATUS                     PORTS     NAMES
   1d74212d2b4f   busybox   "echo Hello world"   3 minutes ago   Exited (0) 3 minutes ago             interesting_dewdney
9. Delete the stopped container
1d74212d2b4f6baf308d374f0c23501b38ed3d8692d0c1f00724a86e82fa2e67
10. Delete all stopped containers
docker container prune

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
docker run -it --rm busybox
   1. Create a txt file with "Hello"
   docker run -it --rm busybox
   /# echo "Hello" > hello.txt
   2. Exit the container
   /# exit
2. Re-run the container
docker run -it busybox
3. Check the file 
le fichier n'est plus la 
4. What happened ?
le fichier disparait car le container a été supprimé

## Clean up

1. List all images
docker image list
2. Delete busybox images
docker image rm busybox

You can use the `prune` command