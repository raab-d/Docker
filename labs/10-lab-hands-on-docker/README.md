# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry

1. What is the default registry ?
The default registry is Docker Hub.

2. What is the différence between these images ?
Les deux images ont des répertoires différents et des docker version différentes.

- `busybox` du répertoire de base a deux répertoires : `busybox:latest` et l'adresse complète `registry.hub.docker.com/library/busybox:latest`. Il a également deux RepoDigests.
- Il n'a pas de hostname, Env, Cmd et valeur pour l'image tandis que le conteneur de `busybox` de `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/` en a.
- J'ai utilisé la commande : `docker inspect busybox`

3. Remove all images that aren't from the default registry.

```sh
docker container ls -a
# CONTAINER ID IMAGE NAMES
# 2ea1e6e60136 registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox fervent_ride
# cb180bb84ce9 registry.hub.docker.com/library/busybox elated_ardinghelli

sudo docker container rm fervent_ride
# Password:
# fervent_ride

docker images
# REPOSITORY TAG IMAGE ID CREATED SIZE
# registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox latest 3772266d7498 9 months ago 4.04MB
# registry.hub.docker.com/library/busybox latest 46bd05c4a04f 10 months ago 4.04MB
# busybox latest 46bd05c4a04f 10 months ago 4.04MB

docker rmi 3772266d7498
# Untagged: registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox:latest
# Untagged: registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox@sha256:2376a0c12759aa1214ba83e771ff252c7b1663216b192fbe5e0fb364e952f85c
# Deleted: sha256:3772266d7498c8df7461f1897f6961cdbc71c63c56c213829d56b9c88bea7634
# Deleted: sha256:464371b65142dd2c9c006150984a8dd608bb7cfd4c07705d845ab11d4a8eaf82

## Work with container

1. Run a busybox container
   1. What happend ?

      Le container run et fini de s'executer directement car on ne lui a pas donner d'action à faire. 
   2. Fix it with a sleep

      docker run busybox sleep 300
      On peut définir le temps qu'on veut, là c'est 5min

2. Run a busybox container that said "Hello world"
   docker run busybox echo 'Hello world'
   Hello world

3. Instantiate an interactive shell with busybox
   1. Run a Hello world inside the container
      Nadya@MacBook-Pro-de-Nadya git % docker run -it busybox sh
      / # echo 'Hello world'
      Hello world
   2. Leave the container
      / # exit
   3. What happened ?
      La commande a démarré un conteneur busybox en mode interactif (-it) avec un shell (sh). 
      Le container a exécuté la commande  echo 'Hello world' et a affiché "Hello world".
      En quittant le shell avec exit, cela a arrêté le processus principal du conteneur (sh) et le conteneur.
      
4. Run a container in background that say "Hello world"
docker run -d busybox echo "Hello world"
f7e842842b8c777653287c50ebc3f146ad89f5242d8849b368e71bcdd8ac54ee

5. Find the container id
Nadya@MacBook-Pro-de-Nadya git % docker ps -a
CONTAINER ID   IMAGE                                     COMMAND                CREATED          STATUS                        
f7e842842b8c   busybox                                   "echo 'Hello world'"   23 seconds ago   Exited (0) 22 seconds ago
Le container id est celui du dernier processus exécuté : f7e842842b8c

6. Print the container logs
docker logs f7e842842b8c  
Hello world

7. Stop the container
docker stop f7e842842b8c  
f7e842842b8c

8. List all container
   1. What happend ?
   docker ps
   CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
   Il n'y a rien car ils sont tous inactifs. 

   2. List all container even the one that is stopped
   docker ps -a
   CONTAINER ID   IMAGE          COMMAND                CREATED          STATUS                        PORTS     NAMES
   f7e842842b8c   busybox        "echo 'Hello world'"   6 minutes ago    Exited (0) 6 minutes ago                eloquent_shtern

9. Delete the stopped container
docker rm f7e842842b8c

10. Delete all stopped containers
Nadya@MacBook-Pro-de-Nadya git % docker container prune          
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y


## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
   1. Create a txt file with "Hello"
      docker run --rm -it busybox sh
      / # echo "Hello" > hello.txt
   2. Exit the container
      / # exit
2. Re-run the container 
   docker run --rm -it busybox sh
3. Check the file 
   / # ls -a
   .           ..          .dockerenv  bin         dev         etc         home        lib         lib64       proc        root        sys         tmp         usr         var
4. What happened ?
   Le fichier hello.txt n'existe pas dans ce nouveau conteneur. 
   C'est dû au fait que le conteneur utilisé lors de la première étape a été supprimé avec tous ses fichiers et modifications après le exit. 

## Clean up

1. List all images
   docker images
2. Delete busybox images
   docker rmi busybox
   docker rmi registry.hub.docker.com/library/busybox 
You can use the `prune` command
