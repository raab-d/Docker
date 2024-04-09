# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
```bash 
docker pull busybox
```
- Pull `busybox` from the gitlab registry
```bash
docker pull registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox
```

1. What is the default registry ?
   ```
   The default registry is the docker hub registry.
   ```
2. What is the différence between these images ?
   ```
   The difference is the registry where the images are stored.
   ```
3. Remove all images that aren't from the default registry.
   ```
   docker rmi registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox
   ```

## Work with container

1. Run a busybox container
   ```bash
   docker run busybox
   ```
   1. What happend ?
      ```
      The container is created and stopped immediately.
      ```
   2. Fix it with a sleep
      ```bash
      docker run busybox sleep 1
      ```
2. Run a busybox container that said "Hello world"
   ```bash
   docker run busybox echo "Hello world"
   ```
3. Instantiate an interactive shell with busybox
   ```bash
   docker run -it busybox sh
   ```
   1. Run a Hello world inside the container
      ```bash
      echo "Hello world"
      ```
   2. Leave the container
      ```bash
      exit
      ```
   3. What happened ?
      ```
      Exiting the shell stops the container.
      ```
4. Run a container in background that say "Hello world"
   ```bash
   docker run -d busybox echo "Hello world"
   ```
5. Find the container id
   ```
   51ed68c1d5375d5124f04de95a0eec988f007dca417858b91365f14b2c86ec74
   ```
6. Print the container logs
   ```bash
   docker logs $(docker ps -l -q)
   ```
   Output: Hello world
7. Stop the container
   ```bash
   docker stop $(docker ps -l -q)
   ```
8. List all container
   ```bash
   docker ps
   ```
   1. What happend ?
      ```
      The list is empty
      ```
   2. List all container even the one that is stopped
      ```bash
      docker ps -a
      ```
      Output :
      ```
      CONTAINER ID   IMAGE     COMMAND                CREATED          STATUS                          PORTS     NAMES
      51ed68c1d537   busybox   "echo 'Hello world'"   18 minutes ago   Exited (0) 18 minutes ago                 mystifying_allen
      025fabc4c1cb   busybox   "sh"                   18 minutes ago   Exited (0) 18 minutes ago                 agitated_blackwell
      1a4798761e4b   busybox   "echo 'Hello world'"   18 minutes ago   Exited (0) 18 minutes ago                 nostalgic_joliot
      199df7f98965   busybox   "sleep 1"              18 minutes ago   Exited (0) 18 minutes ago                 interesting_sammet
      0ea5d4cd95ad   busybox   "sh"                   18 minutes ago   Exited (0) 18 minutes ago                 loving_goodall
      866e6e53c538   busybox   "sleep 1000"           25 minutes ago   Exited (0) About a minute ago             dreamy_margulis
      ac36760331f3   busybox   "sh"                   25 minutes ago   Exited (0) 25 minutes ago                 ecstatic_lalande
      ```
9. Delete the stopped container
   ```bash
   docker rm $(docker ps -a -q)
   ```
10. Delete all stopped containers
      ```bash
      docker container prune
      ```

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
   ```bash
   docker run --rm -it busybox sh
   ```
   1. Create a txt file with "Hello"
      ```bash
      echo "Hello" > /tmp/hello.txt
      ```
   2. Exit the container
      ```bash
      exit
      ```
2. Re-run the container 
   ```bash
   docker run --rm -it busybox sh
   ```
3. Check the file 
   ```bash
   cat /tmp/hello.txt
   ```
4. What happened ?
   ```
   The file is not present because the container is deleted.
   ```

## Clean up

1. List all images
   ```bash
   docker images
   ```
   Output:
   ```
   REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
   busybox      latest    ba5dc23f65d4   10 months ago   4.26MB
   ```
2. Delete busybox images
   ```bash
   docker rmi busybox
   ```

You can use the `prune` command