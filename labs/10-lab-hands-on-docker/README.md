# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry

1. What is the default registry ? <br>
   la version par defaut est l'image fournie par docker hub
2. What is the différence between these images ? <br>
   Ces 2 images proviennent de 2 registery différents
   => 2 id différents :
   - docker hub : ba5dc23f65d4
   - gitlab : 5242710cbd55
3. Remove all images that aren't from the default registry.

## Work with container

1. Run a busybox container
   1. What happend ? <br>
   *docker container run busybox* <br>
   Le container s'est lancé et arreté directement 
   2. Fix it with a sleep <br>
   Pour ajouter un sleep de 10s <br>
   *docker container run busybox sleep 10*
2. Run a busybox container that said "Hello world" <br>
   *docker container run busybox echo 'Hello World'*
3. Instantiate an interactive shell with busybox <br>
   *docker container run -i -t busybox* <br>
   -i permet d'interagir avec le container et -t permet de créer un terminal dans le container
   1. Run a Hello world inside the container <br>
   echo 'Hello World'
   2. Leave the container <br>
   'exit'
   3. What happened ? <br>
   Le container est initialisé en lancant un terminal interactif grace a la combinaison d'option -i et -t. On a ensuite écrit dans le terminal la commande shell echo 'Hello World' pour afficher Hello World dans la console puis on a fermé le terminal avec exit
4. Run a container in background that say "Hello world" <br>
   *docker container run -d busybox echo 'Hello World'*
5. Find the container id <br>
   Pour trouver l'id du container, on affiche la liste des containers actif et non actif avec la commande suivante :
   'docker container ls -a', on peut y lire l'id du dernier container exécuté.
6. Print the container logs <br>
   *docker logs a19629649473* remplacer l'id par le container que vous souhaitez
7. Stop the container <br>
   *docker container stop a19629649473*
8. List all container <br>
   *docker container ls*
   1. What happend ? <br>
      On ne voit plus notre container après l'avoir stoppé
   2. List all container even the one that is stopped <br>
      *docker container ls -a*
      On peut afficher les containers stoppés grace à l'option -a et retrouvé le container qu'on a stoppé.
9. Delete the stopped container <br>
   *docker container rm a19629649473*
10. Delete all stopped containers
   *docker container prune*

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop <br>
   *docker container run -i -t --rm busybox*
   1. Create a txt file with "Hello" <br>
      touch demo.txt
      echo 'Hello' > demo.txt
   2. Exit the container
      exit
2. Re-run the container 
3. Check the file 
4. What happened ? <br>
   Le container ayant été supprimé directement après être stoppé. le fichier txt n'existe plus lorsque l'on recrée un nouveau container.

## Clean up

1. List all images <br>
   *docker image ls*
2. Delete busybox images <br>
   *docker image rm busybox*

You can use the `prune` command