# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
<br>
Terminal: docker pull busybox
- Pull `busybox` from the gitlab registry
<br>
Terminal: docker pull registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox
<br>

1. What is the default registry ?
<br>
registry.hub.docker.com, without specify registery docker uses docker hub
<br>
2. What is the différence between these images ?
<br>
Images hosted on different registries can have different build triggers, security updates, or patches.
<br>
3. Remove all images that aren't from the default registry.
<br>
Deleted on Docker Desktop

## Work with container

1. Run a busybox container
<br>
Terminal: docker run busybox
<br>
   1. What happend ?
   <br>
   The container started and then exited immediately
   <br>
   2. Fix it with a sleep
   <br>
   Terminal: docker run busybox sleep 5
   <br>
2. Run a busybox container that said "Hello world"
<br>
Terminal: docker run busybox echo "Hello world"
<br>
3. Instantiate an interactive shell with busybox
<br>
Terminal: docker run -it busybox
<br>
   1. Run a Hello world inside the container
   <br>
   Container's terminal #: echo "Hello world"
   <br>
   2. Leave the container
   <br>
   Container's terminal #: exit
   <br>
   3. What happened ?
   <br>
   Exiting the shell stop the container
   <br>
4. Run a container in background that say "Hello world"
<br>
Terminal: docker run -d busybox echo "Hello world"
<br>
5. Find the container id
<br>
Terminal: docker ps -l -q
<br>
6. Print the container logs
<br>
Terminal: docker logs $(docker ps -l -q)
<br>
7. Stop the container
<br>
docker stop $(docker ps -l -q)
<br>
8. List all container
<br>
Terminal: docker ps
<br>
   1. What happend ?
   <br>
   List is empty
   <br>
   2. List all container even the one that is stopped
   <br>
   Terminal: docker ps -a
   <br>
9. Delete the stopped container
<br>
Terminal: docker rm $(docker ps -a -q)
<br>
10. Delete all stopped containers
<br>
Terminal: docker container prune
<br>

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
<br>
Terminal: docker run --rm -it busybox
<br>
   1. Create a txt file with "Hello"
   <br>
   Container's terminal #: echo "Hello" > hello.txt
   <br>
   2. Exit the container
   <br>
   Container's terminal #: exit
   <br>
2. Re-run the container
<br>
Terminal: docker run --rm -it busybox
<br>
3. Check the file 
<br>
No file
<br>
4. What happened ?
<br>
Dile doesn't exist because the container was ephemeral and its changes were discarded when it stopped.
<br>

## Clean up

1. List all images
<br>
Terminal: docker images
<br>
2. Delete busybox images
<br>
Terminal: docker image prune -a
<br>

You can use the `prune` command