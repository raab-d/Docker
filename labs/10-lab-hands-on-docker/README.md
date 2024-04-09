# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
$pull busybox
- Pull `busybox` from the gitlab registry
$pull registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox
1. What is the default registry ?
- Docker hub
2. What is the différence between these images ?
-L'image qui provient du docker hub est l'original tandis que celle qui provient du registre gitlab qui peut être une version modifié. 

3. Remove all images that aren't from the default registry.


## Work with container

1. Run a busybox container
   1. What happend ?
	-L'image se lance mais s'arrette immédiatement
   2. Fix it with a sleep
	$docker run busybox sleep 5
2. Run a busybox container that said "Hello world"
	$docker run busybox echo hello world
3. Instantiate an interactive shell with busybox
	$docker run -it busybox sh
   1. Run a Hello world inside the container
	$echo "Hello world"
   2. Leave the container
	$exit
   3. What happened ?
Le shell interactif se ferme et le conteneur s'arrête de fonctionner
4. Run a container in background that say "Hello world"
	$docker run -d --name hello-container busybox echo "Hello world"
5. Find the container id
	$docker ps -a
	-68360f00009e
6. Print the container logs
	$docker logs hello-container
7. Stop the container
	$docker stop hello-container
8. List all container
	$docker ps -a
   1. What happend ?
	-La commande m'affiche tout les containeurs en cours d'éxecution ou non. 
   2. List all container even the one that is stopped
	$docker ps -a
9. Delete the stopped container
	$docker rm hello-container
10. Delete all stopped containers
	$docker container prune

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
	$docker run -it --rm busybox sh
   1. Create a txt file with "Hello"
	$echo "Hello" > hello.txt
   2. Exit the container
	$exit
2. Re-run the container 
	$docker run -it --rm busybox sh
3. Check the file 
4. What happened ?
	- Les changements n'ont pas été sauvergardé à cause de la commande --rm

## Clean up

1. List all images
	$docker images
2. Delete busybox images
	$docker rmi busybox

You can use the `prune` command