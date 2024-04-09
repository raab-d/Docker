# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry

1. What is the default registry ?
The default registry is : registry.hub.docker.com
2. What is the différence between these images ?
Different updates, patches or build triggers
3. Remove all images that aren't from the default registry.

## Work with container

1. Run a busybox container
   1. What happend ?
   The container start and terminate
   2. Fix it with a sleep
   docker run busybox sleep 5
2. Run a busybox container that said "Hello world"
docker run buxybox echo "Hello world"
3. Instantiate an interactive shell with busybox
   1. Run a Hello world inside the container
   echo "Hello world"
   2. Leave the container
   exit
   3. What happened ?
   It stops the container
4. Run a container in background that say "Hello world"
docker run -d busybox echo "Hello world"
5. Find the container id
docker ps -l -q
6. Print the container logs

7. Stop the container
docker logs $(docker ps -l -q)
8. List all container
   1. What happend ?
   The list is empty
   2. List all container even the one that is stopped
   docker ps
9. Delete the stopped container
docker rm $(docker ps -a -q)
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
docker run --rm -it busybox 
3. Check the file 
It doesn't find the file
4. What happened ?
The file does not exist because we have a ephemeral container
## Clean up

1. List all images
docker images
2. Delete busybox images
docker container prune

You can use the `prune` command