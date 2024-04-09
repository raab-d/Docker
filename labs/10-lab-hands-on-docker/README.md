# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry

1. What is the default registry ? docker hub.
2. What is the différence between these images ? Celui de gitlab est plus léger -> 4.26mb au lieu de 4.86mb pour celui de docker hub.
3. Remove all images that aren't from the default registry. docker image rm registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox

## Work with container

1. Run a busybox container
   1. What happend ? Un container est up avec l'image busybox, il s'appelle blissful_shannon mais s'exited direct.
   2. Fix it with a sleep : docker run busybox sleep infinity
2. Run a busybox container that said "Hello world" : docker run busybox /bin/sh -c "echo 'Hello world'"
3. Instantiate an interactive shell with busybox : docker run -it busybox /bin/sh
   1. Run a Hello world inside the container : echo 'Hello world'
   2. Leave the container : CTRL + D
   3. What happened ? Le container est exited.
4. Run a container in background that say "Hello world" : docker run busybox /bin/sh -c "echo 'Hello world'"
5. Find the container id : docker ps -aqf "ancestor=busybox"
6. Print the container logs : docker container logs 10b30188a29f
7. Stop the container : docker stop $(docker ps -aq) && docker rm $(docker ps -aq)
8. List all container : docker ps
   1. What happend ? La liste des containers apparait 
   2. List all container even the one that is stopped : docker ps -a
9. Delete the stopped container : docker rm $(docker ps)
10. Delete all stopped containers : docker rm $(docker ps -aq)

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
   1. Create a txt file with "Hello"
   2. Exit the container
2. Re-run the container 
3. Check the file 
4. What happened ?

-> docker run -it busybox /bin/sh -c "touch test_file & echo 'Hello' > test_file & cat test_file" && docker stop $(docker ps -aq) && docker rm $(docker ps -aq)

## Clean up

1. List all images : docker image ls
2. Delete busybox images : docker image rm busybox

You can use the `prune` command
