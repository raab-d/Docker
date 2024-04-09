# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry

1. What is the default registry ? <br>
docker image inspect 'RegistryName'.<br>
It's the first registry in "RepoTags". Therefore, Docker hub go the default registry.
2. What is the différence between these images ?
The Gitlab got two layers with one Add file and a CMD "sh" whereas the default only have the debian BusyBox
3. Remove all images that aren't from the default registry.<br>
docker image ls

## Work with container

1. Run a busybox container
   1. What happend ? <br>
   Nothing happens. A command bash appears with some further steps.
   2. Fix it with a sleep <br>
   A sleep command stops the bash for the seconds we wrote.
2. Run a busybox container that said "Hello world" <br>
   docker run busybox echo "Hello world"
3. Instantiate an interactive shell with busybox
   1. Run a Hello world inside the container <br>
   docker run -it busybox /bin/sh
   2. Leave the container <br>
   exit
   3. What happened ? <br>
   The container stopped
4. Run a container in background that say "Hello world" <br>
   docker run -d registry.hub.docker.com/library/busybox echo "Hello world"
5. Find the container id <br>
   docker ps -l
6. Print the container logs <br>
   docker logs b5cc2845c16a
   -> Hello world
7. Stop the container <br>
   docker stop b5cc2845c16a
8. List all container
   1. What happend ? <br>
   docker ps -a
   Every container that I have ever created are here.
   2. List all container even the one that is stopped <br>
   C:\Users\erwan\Desktop\ESGI\S10\Docker-Kubernetes\Docker\labs\10-lab-hands-on-docker>docker ps -a
CONTAINER ID   IMAGE                                                 COMMAND                  CREATED          STATUS                      PORTS                              NAMES <br>
b5cc2845c16a   registry.hub.docker.com/library/busybox               "echo 'Hello world'"     3 minutes ago    Exited (0) 3 minutes ago                                       adoring_mirzakhani <br>
02b60520a5cb   registry.hub.docker.com/library/busybox               "/bin/sh"                7 minutes ago    Exited (0) 6 minutes ago                                       boring_ellis <br>
9. Delete the stopped container <br>
   docker rm boring_ellis
10. Delete all stopped containers <br>
   docker rm $(docker ps -a -q -f status=exited) <br>
   But I won't do it since I have a lot of containers stopped and I use them personally. I'll just use the first command.

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop <br>
   docker run -it --rm registry.hub.docker.com/library/busybox
   1. Create a txt file with "Hello" <br>
   echo "Hello" > temp.txt <br>
   ls -> bin          dev          etc          exemple.txt  home         lib          lib64        proc         root         sys          temp.txt     tmp          usr          var
   2. Exit the container <br>
   exit
2. Re-run the container <br>
   Well, "re-run" can't be made since it's destroy when it is stopped. But we will re-run the command
3. Check the file <br>
   ls -> bin    dev    etc    home   lib    lib64  proc   root   sys    tmp    usr    var <br>
4. What happened ? <br>
   The file has been destroyed.

## Clean up

1. List all images <br>
   docker ps -a
2. Delete busybox images <br>
   

You can use the `prune` command