# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry

1. What is the default registry ?
Le registre par défaut pour Docker est Docker Hub, accessible via registry.hub.docker.com ou simplement par docker.io.
2. What is the différence between these images ?
Les images busybox provenant de Docker Hub et de GitLab peuvent être identiques en termes de fonctionnalité et de contenu. Cependant, les différences peuvent résider dans leur cycle de mise à jour ou dans des modifications spécifiques apportées par la communauté ou l'organisation qui gère l'image dans le registre alternatif. Par exemple, GitLab pourrait avoir une politique de mise à jour différente ou inclure des configurations spécifiques pour mieux intégrer busybox dans ses pipelines CI/CD.
3. Remove all images that aren't from the default registry.

## Work with container

1. Run a busybox container
   1. What happend ?
   lorsque j'exécute docker run busybox sans spécifier une commande, le conteneur s'exécute puis s'arrête immédiatement parce que busybox n'a pas de processus de longue durée pour le garder actif.
   2. Fix it with a sleep
   Pour le garder en exécution : docker run busybox sleep 3600.
2. Run a busybox container that said "Hello world"
docker run busybox echo "Hello world"
Affiche "Hello world" puis le conteneur s'arrête.
3. Instantiate an interactive shell with busybox
   1. Run a Hello world inside the container
   Après avoir démarré le shell avec docker run -it busybox sh, j'ai tapé echo "Hello world" dans le shell.
   2. Leave the container
   exit ou Ctrl+D
   3. What happened ?
   Le conteneur s'arrête car le processus principal (le shell interactif) a été fermé.
4. Run a container in background that say "Hello world"
avec la commande 
docker run -d busybox echo "Hello world"

5. Find the container id
voila l'id
97a328cdd2c3 
6. Print the container logs
docker logs 97a328cdd2c3

abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker (rabah_AZI/docker/labs)
$ docker logs 47df20122070
Hello world

7. Stop the container
abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker (rabah_AZI/docker/labs)
$ docker stop 47df20122070
47df20122070

8. List all container
   1. What happend ?
   docker ps affiche seulement les conteneurs en cours d'exécution.
   2. List all container even the one that is stopped
   abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker (rabah_AZI/docker/labs)
$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES


abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker (rabah_AZI/docker/labs)
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND                CREATED          STATUS                      PORTS     NAMES
97a328cdd2c3   busybox   "echo 'Hello world'"   6 minutes ago    Exited (0) 6 minutes ago              loving_meitner
654def50fc42   busybox   "sh"                   36 minutes ago   Exited (0) 31 minutes ago             fervent_sutherland
47df20122070   busybox   "echo 'Hello world'"   39 minutes ago   Exited (0) 39 minutes ago             unruffled_vaughan
58e59236ba31   busybox   "sh"                   40 minutes ago   Exited (0) 40 minutes ago             priceless_darwin

abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker (rabah_AZI/docker/labs)

Affiche tous les conteneurs, y compris ceux arrêtés.

9. Delete the stopped container

10. Delete all stopped containers

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
docker run --rm -it busybox sh

   1. Create a txt file with "Hello"
   echo "Hello" > hello.txt

   2. Exit the container
2. Re-run the container 
3. Check the file 
4. What happened ?
Le fichier hello.txt n'existe pas dans le nouveau conteneur car chaque conteneur est isolé et éphémère, ce qui signifie que les changements sont perdus lorsque le conteneur est arrêté et supprimé (--rm).
## Clean up

1. List all images
2. Delete busybox images

You can use the `prune` command