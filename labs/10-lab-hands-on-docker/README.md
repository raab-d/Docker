# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry

1. What is the default registry ?
# Docker Hub and it is accessible at registry.hub.docker.com
2. What is the différence between these images ?
# There is no diffrence, unless the image from the gitlab is based on diffrent diffrent version or diffrence in the build process
3. Remove all images that aren't from the default registry.
# docker image rm registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox
# Untagged: registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox:latest
# Untagged: registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox@sha256:2376a0c12759aa1214ba83e771ff252c7b1663216b192fbe5e0fb364e952f85c
# Deleted: sha256:5242710cbd55829f6c44b34ff249913bb7cee748889e7e6925285a29f126aa78
# Deleted: sha256:feb4513d4fb7052bcff38021fc9ef82fd409f4e016f3dff5c20ff5645cde4c02


## Work with container

1. Run a busybox container
   1. What happend ?
   # The container named busybox is added to docker desktop, but without adding sh, it will exit directly
   2. Fix it with a sleep
   # docker run busybox sleep 10

2. Run a busybox container that said "Hello world"
# docker run busybox echo "hello world"
# hello world
3. Instantiate an interactive shell with busybox
# docker run -it busybox sh
   1. Run a Hello world inside the container
   # / # echo "hello world"
   # hello world
   2. Leave the container
   # with ctrl + d i quit the container
   3. What happened ?
   # as i quit the container, im back to cmd

4. Run a container in background that say "Hello world"
# docker run -d busybox echo "Hello world"
# c2247cd38e56dd79e33991c354ec54970b23d22bb354e6be339b02d611c8da98

5. Find the container id
# docker ps -l
# CONTAINER ID   IMAGE     COMMAND                CREATED          STATUS                      PORTS     NAMES
# c2247cd38e56   busybox   "echo 'Hello world'"   11 minutes ago   Exited (0) 11 minutes ago             heuristic_noether

6. Print the container logs
# docker logs c2247cd38e56
# Hello world

7. Stop the container
# docker stop c2247cd38e56
# c2247cd38e56

8. List all container
   1. What happend ?
   # docker ps
   # CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
   # i found no containers
   2. List all container even the one that is stopped
   # docker ps -a
   # show the stopped busy boxes containers

9. Delete the stopped container
# docker rm c2247cd38e56

10. Delete all stopped containers
# docker rm $(docker ps -q)

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
# docker run --rm -it busybox sh
   1. Create a txt file with "Hello"
   # echo "Hello" > hello.txt
   2. Exit the container
   # ctrl d
2. Re-run the container 
# docker run --rm -it busybox sh
3. Check the file 
# ls
# there is no file named hello.txt
4. What happened ?
# it is deleted because the container is set to delete at stop

## Clean up

1. List all images
# docker images
2. Delete busybox images
# docker rmi busybox
# Untagged: busybox:latest
# Untagged: busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
# Deleted: sha256:ba5dc23f65d4cc4a4535bce55cf9e63b068eb02946e3422d3587e8ce803b6aab
# Deleted: sha256:95c4a60383f7b6eb6f7b8e153a07cd6e896de0476763bef39d0f6cf3400624bd
You can use the `prune` command
