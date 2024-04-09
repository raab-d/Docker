# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry

1. What is the default registry ? <br>
Le registry par défaut est celle de Docker Hub.
2. What is the différence between these images ?<br>
La différence pourrait être la version de BusyBox ou les configurations de build, mais pour cela, on doit vérifier directement des images avec la commande "docker inspect " 
3. Remove all images that aren't from the default registry.<br>
j'ai gardé l'image de cette address (registry.hub.docker.com/library/busybox) même si elle est la même que quand on fait avec un simple busybox

## Work with container

1. Run a busybox container
   1. What happend ?
   <br> Cela créer un container avec l'image busybox puis ce quite directement.
   2. Fix it with a sleep
   <br> Cela fait attendre quelques secondes avant de s'éteindre.
2. Run a busybox container that said "Hello world"
   <br> docker run busybox echo "Hello world"
3. Instantiate an interactive shell with busybox
   1. Run a Hello world inside the container
   <br> echo "Hello world"
   2. Leave the container
   <br> exit
   3. What happened ?
   <br>  Cela nous permet de rester à l'intérieur du container et donc de travailler dans son environement.
4. Run a container in background that say "Hello world"
<br> docker run -d busybox echo "Hello world"
5. Find the container id
<br> docker ps -l <br> cela donne comme résultat 7940ffc6abc0
6. Print the container logs
<br> docker logs 7940ffc6abc0 <br> cela affiche Hello world
7. Stop the container
 <br> docker stop 7940ffc6abc0
8. List all container
<br> docker ps
   1. What happend ?
   <br> N'affiche que les conteneurs en cours d'exécution.
   2. List all container even the one that is stopped
   <br> docker ps -a
9. Delete the stopped container
<br> docker rm 7940ffc6abc0
10. Delete all stopped containers
<br> docker container prune

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
<br> docker run --rm -it busybox
   1. Create a txt file with "Hello"
   <br> echo "Hello" > hello.txt
   2. Exit the container
   <br> exit
2. Re-run the container 
3. Check the file 
<br> Le fichier n'existe pas car le conteneur est supprimé.
4. What happened ?
<br> Les modifications sont perdues à cause de --rm.

## Clean up

1. List all images
<br> docker images
2. Delete busybox images
<br> docker rmi -f $(docker images 'busybox' -q) <br> j'ai du mettre un -f car j'avais une erreur due au fait que j'avais plusieurs repositories avec cette image.

You can use the `prune` command