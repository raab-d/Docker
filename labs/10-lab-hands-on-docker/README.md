# Lab 1 - Hands on Docker<br>

## Pull your first images.<br>

### Tips<br>

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`<br>
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`<br>

### Images from different registry<br>

- Pull `busybox` from the default registry<br>
Command: docker pull busybox<br>
- Pull `busybox` from the gitlab registry<br>
<br>Command: docker pull registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox<br>


1. What is the default registry ?<br>
<br>registry.hub.docker.com,without specify registery docker uses docker hub<br>
2. What is the différence between these images ?<br>
<br>Images hosted on different registries can have different build triggers, security updates, or patches.<br>
3. Remove all images that aren't from the default registry.<br>

## Work with container<br>

1. Run a busybox container<br>
<br>Command: docker run busybox<br>
   1. What happend ?<br>
   <br>The container started and then exited immediately<br>
   2. Fix it with a sleep<br>
   <br>docker run busybox sleep 5<br>
2. Run a busybox container that said "Hello world"<br>
Command: docker run busybox echo "Hello world"<br>
3. Instantiate an interactive shell with busybox<br>
docker run -it busybox<br>
   1. Run a Hello world inside the container<br>
   # echo "Hello world"<br>
   2. Leave the container<br>
   # exit<br>
   3. What happened ?<br>
   Exiting the shell stops the container<br>
4. Run a container in background that say "Hello world"<br>
Command: docker run -d busybox echo "Hello world"<br>
5. Find the container id<br>
Command: docker ps -l -q<br>
6. Print the container logs<br>
Command: docker logs $(docker ps -l -q)<br>
7. Stop the container<br>
Command: docker stop $(docker ps -l -q)<br>
8. List all container<br>
Command: docker ps<br>
   1. What happend ?<br>
   The list is empty<br>
   2. List all container even the one that is stopped<br>
   Command: docker ps -a<br><br>
   Result : <br>
   CONTAINER ID   IMAGE          COMMAND                CREATED             STATUS                         PORTS     NAMES<br>
dc98c4785df3   ba5dc23f65d4   "echo 'Hello world'"   59 minutes ago      Exited (0) 59 minutes ago            boring_lovelace<br>
0cc13ff409fb   ba5dc23f65d4   "sh"                   About an hour ago   Exited (0) About an hour ago          thirsty_williamson<br>
0a842a7f24d4   ba5dc23f65d4   "echo 'Hello World'"   About an hour ago   Exited (0) About an hour ago            xenodochial_morse<br>
274d1d423c29   ba5dc23f65d4   "sh"                   About an hour ago   Exited (0) About an hour ago            agitated_turing<br>

9. Delete the stopped container<br>
Command: docker rm $(docker ps -a -q)<br>
10. Delete all stopped containers<br>
Command: docker container prune<br>

## Work with ephemeral container<br>

1. Run a interactif container with busybox that will be deleted at stop<br>
Command: docker run --rm -it busybox<br>
   1. Create a txt file with "Hello"<br>
   # echo "Hello" > hello.txt<br>
   2. Exit the container<br>
   # exit<br>
2. Re-run the container <br>
Command: docker run --rm -it busybox<br>
3. Check the file <br>
It doesn't find the file<br>
4. What happened ?<br>
The file doesn't exist because the container was ephemeral and its changes were discarded when it stopped.<br>

## Clean up<br>

1. List all images<br>
<br>Command: docker images
2. Delete busybox images<br>
<br>docker container prune
You can use the `prune` command<br>
