# Lab 1 - Hands on Docker

Mon Identifiant GitHub : CYPRIN02 (prasoloarivony@gmail.com)

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry

$ docker pull busybox
$ docker pull registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox

1. What is the default registry ?
-> Le registre par défaut de Docker est Docker Hub (registry.hub.docker.com).


2. What is the différence between these images ?
-> Les images peuvent être les mêmes, mais elles proviennent de registres différents. 
La principale différence pourrait résider dans la version des images ou dans les 
configurations spécifiques liées au registre d'où elles sont tirées.


3. Remove all images that aren't from the default registry.
-> 
$ docker rmi [IMAGE ID or REPOSITORY:TAG]


## Work with container

1. Run a busybox container

   $ docker run busybox

   1. What happend ?
   -> Le conteneur se termine immédiatement car busybox, par défaut, ne fait rien et s'arrête.
   
   2. Fix it with a sleep
   $ docker run busybox sleep 1


2. Run a busybox container that said "Hello world"
$ docker run busybox echo "Hello world"


3. Instantiate an interactive shell with busybox
$ docker run -it busybox sh

   1. Run a Hello world inside the container
   $ echo "Hello world"
   $ exit

   2. Leave the container
   $ exit
   
   3. What happened ?
   -> Le conteneur s'exécute, affiche "Hello world", puis s'arrête lorsque je quitte le shell.

4. Run a container in background that say "Hello world"
$ docker run -d busybox sh -c "echo 'Hello world'; sleep 3600"


5. Find the container id
$ docker ps


6. Print the container logs
$ docker logs [CONTAINER ID]


7. Stop the container
$ docker stop [CONTAINER ID]


8. List all container
$ docker ps

   1. What happend ?
   -> affiche les containers qui sont en RUN
   2. List all container even the one that is stopped
   $ docker ps -a

9. Delete the stopped container
   $ docker rm [CONTAINER ID]

10. Delete all stopped containers
   $ docker container prune

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
$ docker run --rm -it busybox sh

   1. Create a txt file with "Hello"
   $ echo "Hello" > hello.txt

   2. Exit the container
   $ exit


2. Re-run the container 
-> vide
3. Check the file 
-> Je ne peux pas vérifier le fichier car le conteneur est éphémère et a été 
   supprimé à la sortie.


4. What happened ?
-> *****************
## Clean up

1. List all images
-> docker images

2. Delete busybox images
$ docker rmi busybox
$ docker rmi registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox

ou bien 'prune' ou 'rmi'

You can use the `prune` command