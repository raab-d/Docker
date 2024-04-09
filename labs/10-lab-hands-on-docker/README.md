# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
<br> docker pull busybox
- Pull `busybox` from the gitlab registry
<br> docker pull registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox


1. What is the default registry ?
<br> The default registry is Docker Hub, located at registry.hub.docker.com.
2. What is the différence between these images ?
<br>The primary difference might be in the version and build of the images. While they are both BusyBox images, the one on Docker Hub may follow a different update schedule and have minor variations compared to the one hosted on GitLab's registry.
3. Remove all images that aren't from the default registry.
<br> docker images --format "{{.Repository}}:{{.Tag}}" | grep -v "docker.io" | xargs -r docker rmi


## Work with container

1. Run a busybox container
   1. What happend ?
   <br> Nothing seems to be happening.
   2. Fix it with a sleep
   <br> $ docker run busybox sleep 10
   <br> Nothing seems to be happening for 10 seconds.
2. Run a busybox container that said "Hello world"
<br> $ docker run busybox echo "Hello world"
3. Instantiate an interactive shell with busybox
<br> $ docker run -it busybox sh
   1. Run a Hello world inside the container
   <br> echo "Hello world"
   
   2. Leave the container
   <br> exit
   3. What happened ?
   <br> The container stopped running.
4. Run a container in background that say "Hello world"
<br> docker run -d busybox echo "Hello world"
5. Find the container id
docker ps -l -q
6. Print the container logs
<br> docker logs 8ef5e4c3ae22 
7. Stop the container
<> docker stop 8ef5e4c3ae22
8. List all container
   1. What happend ?
   <br> $ docker ps
    <br> No container is listed.
   2. List all container even the one that is stopped
   <br> docker ps -a
   <br> The container is listed as stopped.

9. Delete the stopped container
<br> docker rm 8ef5e4c3ae22
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
<br> docker run --rm -it busybox

3. Check the file 
<br> $ ls
4. What happened ?
<br> No file named hello.txt is present.

## Clean up

1. List all images
<br> docker images
2. Delete busybox images
<br> docker rmi busybox

You can use the `prune` command
<br> docker image prune
