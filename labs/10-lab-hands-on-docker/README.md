# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry

1. What is the default registry ?

registry.hub.docker.com est le registre par défaut quand on n'en spécifie aucun lors d'une commande pull

2. What is the différence between these images ?

Ils n'ont pas la même version de Docker. On inspecte les images en utilisant "docker inspect [IMAGE ID]".
busybox : pas de version
busybox gitlab : 20.10.23

3. Remove all images that aren't from the default registry.


docker rmi registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox

Untagged: registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox:latest
Untagged: registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox@sha256:2376a0c12759aa1214ba83e771ff252c7b1663216b192fbe5e0fb364e952f85c
Deleted: sha256:5242710cbd55829f6c44b34ff249913bb7cee748889e7e6925285a29f126aa78
Deleted: sha256:feb4513d4fb7052bcff38021fc9ef82fd409f4e016f3dff5c20ff5645cde4c02

## Work with container

1. Run a busybox container

docker run busybox

   1. What happend ?

   L'exécution s'est arrêtée immédiatement car on n'a pas spécifié d'action lors de l'exécution

   2. Fix it with a sleep

   docker run busybox sleep 60

2. Run a busybox container that said "Hello world"

docker run busybox echo "Hello World"
Hello World

3. Instantiate an interactive shell with busybox
   1. Run a Hello world inside the container

   docker run -it busybox sh
   / # echo Hello world
   Hello world

   2. Leave the container

   / # exit

   3. What happened ?

   En quittant l'interface interactive, on a mis fin au processus principal. 

4. Run a container in background that say "Hello world"

docker run -d busybox /bin/sh -c "while true; do echo Hello World; sleep 60; done"
b7757fafee2850a479afad287eceaa90171b103343337264b42a95d1ef87c6d5

5. Find the container id

docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
b7757fafee28   busybox   "/bin/sh -c 'while t…"   48 seconds ago   Up 47 seconds             infallible_stonebraker

6. Print the container logs

docker logs b7757fafee28
Hello World
Hello World

7. Stop the container

docker stop b7757fafee28
b7757fafee28

8. List all container

docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

   1. What happend ?

   La commande docker ps recense les processus actifs, étant donné que nous avons arrêté le container avec docker stop, il n'apparaît plus.

   2. List all container even the one that is stopped

   docker ps -a
   CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                            PORTS     NAMES
   b7757fafee28   busybox   "/bin/sh -c 'while t…"   2 minutes ago   Exited (137) About a minute ago             infallible_stonebraker
   ccc18501ecc4   busybox   "sh"                     7 minutes ago   Exited (0) 7 minutes ago                    strange_hamilton
   7dbde04fd01a   busybox   "echo 'Hello World'"     7 minutes ago   Exited (0) 7 minutes ago                    wonderful_mccarthy

9. Delete the stopped container

On peut utiliser la commande docker rm [CONTAINER_ID]
 docker rm b7757fafee28
b7757fafee28
 docker ps -a
CONTAINER ID   IMAGE     COMMAND                CREATED         STATUS                     PORTS     NAMES
ccc18501ecc4   busybox   "sh"                   8 minutes ago   Exited (0) 8 minutes ago             strange_hamilton
7dbde04fd01a   busybox   "echo 'Hello World'"   8 minutes ago   Exited (0) 8 minutes ago             wonderful_mccarthy

10. Delete all stopped containers

docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
ccc18501ecc46f94ec4efdd936be256274aabc12063f26eeaa231974c451dc1a
7dbde04fd01aad30b66fe95af3ad1578b9a67e81cbbacdb6c7b90f72d1946270

Total reclaimed space: 22B


## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
   1. Create a txt file with "Hello"

   docker run --rm -it busybox
   / # echo "Hello" > hello.txt
   / # cat hello.txt
   Hello

   2. Exit the container

   / # exit

2. Re-run the container 

docker run --rm -it busybox

3. Check the file 

/ # ls -l hello.txt
ls: hello.txt: No such file or directory
/ # exit

4. What happened ?

Avec l'option "--rm" on spécifie la suppression du container une fois arrêté. Puisque nous l'avons quitté avec "exit", les fichiers créés n'existent plus ce qui explique que hello.txt n'apparaisse plus.

## Clean up

1. List all images

docker images

REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
busybox      latest    ba5dc23f65d4   10 months ago   4.26MB

2. Delete busybox images

 docker rmi -f busybox
Untagged: busybox:latest
Untagged: busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
Deleted: sha256:ba5dc23f65d4cc4a4535bce55cf9e63b068eb02946e3422d3587e8ce803b6aab
Deleted: sha256:95c4a60383f7b6eb6f7b8e153a07cd6e896de0476763bef39d0f6cf3400624bd

You can use the `prune` command