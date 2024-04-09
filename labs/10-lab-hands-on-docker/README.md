# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
	docker pull registry.hub.docker.com/library/busybox 
- Pull `busybox` from the gitlab registry
	docker pull registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox

1. What is the default registry ?
	It's Docker Hub
2. What is the différence between these images ?
3. Remove all images that aren't from the default registry.
	"docker container ls -a" to show all containers
	"docker container rm 4141abed1c0a" to delete the container related to that image
	"docker image ls -a" to show all images
	"docker image rm 3772266d7498" to delete the image related to registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox


## Work with container

1. Run a busybox container
	docker run busybox
   1. What happend ?
   		Nothing happened it has runned a busybox container and exited from it directly.
   2. Fix it with a sleep
   		"docker run busybox sleep 300" to maintain the container alive for the specificied timeline.
2. Run a busybox container that said "Hello world"
	docker run busybox echo "Hello world"  
3. Instantiate an interactive shell with busybox
	docker run -it busybox 
   1. Run a Hello world inside the container
   		echo "Hello world"
   2. Leave the container
   		exit
   3. What happened ?
   		Don't have 'Hello world' printed on my local shell. That means it was just executed in the container.
4. Run a container in background that say "Hello world"
	docker run -d busybox echo "Hello World"
5. Find the container id
	45a2a39656ce by executing the commandline "docker container ls -a"
6. Print the container logs
	"docker container logs 45a2a39656ce" prints "Hello world" on the shell     
7. Stop the container
	docker stop 45a2a39656ce
8. List all container
	docker ps
   1. What happend ?
   		That container is no longer there
   2. List all container even the one that is stopped
   		docker ps -a
9. Delete the stopped container
	docker rm 45a2a39656ce
10. Delete all stopped containers
	docker container prune

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
	docker run --rm -it busybox
   1. Create a txt file with "Hello"
   		echo "Hello" > hello.txt
   2. Exit the container
   		exit
2. Re-run the container 
	docker ps -a to check the container id but nothing appeare. That's normal so we cannot rerun the container because the container has been deleted at stop
3. Check the file 
	Cannot check anything in a deleted container
4. What happened ?
	The container has been deleted at stop (--rm in the commandline).

## Clean up

1. List all images
	"docker image ls -a"
2. Delete busybox images
	"docker rmi busybox" or "docker image prune"

You can use the `prune` command