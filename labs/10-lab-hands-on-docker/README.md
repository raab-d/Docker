# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry


docker pull registry.hub.docker.com/library/busybox
docker pull registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox


1. What is the default registry ?
Le registre par défaut pour Docker est Docker Hub (docker.io ou simplement omis dans la commande)

2. What is the différence between these images ?
Ces images peuvent être différentes en termes de version ou de build, dépendant de la fréquence de mise à jour par les gestionnaires de registres

3. Remove all images that aren't from the default registry.
docker rmi registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox

## Work with container

1. Run a busybox container

docker run busybox

   1. What happend ?
   Rien de visible, car BusyBox a besoin d'une commande à exécuter.

   2. Fix it with a sleep
   docker run busybox sleep 10


2. Run a busybox container that said "Hello world"
docker run busybox echo "Bonjour tout le monde"

3. Instantiate an interactive shell with busybox
docker run -it busybox sh

   1. Run a Hello world inside the container
   echo "Hello World"

   2. Leave the container
   tapper exit

   3. What happened ?
   On voit l'affichage de Hello World sur le terminal

4. Run a container in background that say "Hello world"
docker run -d busybox echo "Bonjour tout le monde"

5. Find the container id
docker ps -a

6. Print the container logs
docker logs fabbd2f72573

7. Stop the container
docker stop fabbd2f72573

8. List all container
docker ps

   1. What happend ?
   On trouve aucun container
   2. List all container even the one that is stopped
   docker ps -a

9. Delete the stopped container
docker rm fabbd2f72573

10. Delete all stopped containers
docker container prune


## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
docker run --rm -it busybox sh

   1. Create a txt file with "Hello"
   echo "Azul" > azul.txt

   2. Exit the container
   exit

2. Re-run the container 
3. Check the file 
4. What happened ?
On voit bien que le fichier n'existe pas, donc il est éphémère (cela grâçe à --rm)

## Clean up

1. List all images
docker images

2. Delete busybox images
docker rmi busybox 

You can use the `prune` command
docker image prune
