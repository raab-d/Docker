# Lab 1 - Hands on Docker
- idGithub:Roquekinsley 
## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry

1. What is the default registry ?
Le registre par défaut pour Docker est Docker Hub
2. What is the différence between these images ?
- Nom plus complets avec plus d'information dans Repotsdigests et RepotsTags
- pas d'environnement pour celui du docker hub
- date de création différente
- ils ont pas les mêmes version
- un officiel et l'autres non
<br>On peux voir les informations en fesant un docker inspect "lien image"</br>
<br>3. Remove all images that aren't from the default registry.</br>
<br>D'abord je supprime le containeur docker container rm 'ID ou nom'</br>
<br>Je liste les images avec docker image ls</br>
<br>puis un docker image rm 'ID ou nom'</br>

## Work with container

1. Run a busybox container
  <br> 1. What happend ?</br>
   <br>le conteneur démarre et exécute la commande puis s'arréte car pas d'actions</br>
   <br>2. Fix it with a sleep</br>
  <br> gardera le conteneur actif pendant le temps indiquer dans le sleep.</br>
<br>2. Run a busybox container that said "Hello world"</br>
<br>docker container run busybox echo "Hello world"</br>
<br>cela affiche 'Hello world'</br>

3. Instantiate an interactive shell with busybox
   1. Run a Hello world inside the container
   2. Leave the container
   3. What happened ?
  <br> cela execute  Hello world dans le conteneur avec winpty docker run -it busybox sh, puis  echo "Hello world" dans le shell.
   On quitte avec la comande exit sinon le conteneur continura a tourner, ce qui arrêtera le conteneur .</br>
<br>Commande:</br>
   $ winpty docker run -it busybox sh
   / # echo "Hello world"
   Hello world
   / # Exit
   sh: Exit: not found
   / # exit

<br>4. Run a in background that say "Hello world"</br>
 <br>  $     docker container run -d busybox echo "Hello world"</br>
<br> d10e35e29bd87b9a84eaeaa4780b7360bbad0fc69f16f6aa8e907f3e743bb266</br>

<br>5. Find the container id</br>
docker container ls -a
CONTAINER ID   IMAGE     COMMAND                CREATED              STATUS                          PORTS     NAMES
b40e7154b267   busybox   "sh"                   About a minute ago   Exited (0) 26 seconds ago                 friendly_shtern
2dd5dc85fff5   busybox   "echo 'Hello world'"   About a minute ago   Exited (0) About a minute ago             vigilant_varahamihira
c19723450cbd   busybox   "sh"                   2 minutes ago        Exited (0) 2 minutes ago                  strange_mcclintock

6. Print the container logs
docker container logs 'ID du container'
   $ docker container logs b40e7154b267
   / # echo "Hello world"
   Hello world
   / # exit

<br> 7. Stop the container</br>
<br> docker container stop 'ID du container'</br>

<br>8. List all container</br>
  <br> 1. What happend ?</br>
  <br> rien s'affiche car aucun est actif</br>
  <br> 2. List all container even the one that is stopped</br>
<br>si on fais docker container ls cela affiche les containers actif </br>
<br>si on fais docker container ls -a cela affiche tous  les containers</br>

<br>9. Delete the stopped container</br>
<br>docker container rm 'ID du container'</br>

<br>10. Delete all stopped containers</br>
<br>docker container prune</br>



## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
   1. Create a txt file with "Hello"
  <br> winpty docker run --rm -it busybox sh</br>
  <br> echo "Hello" > hello.txt</br>
   
   <br>2. Exit the container</br>
 <br>  exit</br>
<br>2. Re-run the container </br>
<br>docker run -it busybox sh</br>
<br>3. Check the file </br>
<br>ls</br>
<br>4. What happened ?</br>
<br>il n'y aura pas de fichier car le contener est temporaire</br> 

## Clean up

<br>1. List all images</br>
<br>docker image ls</br>
<br>2. Delete busybox images</br>
<br>tous les image qui ne sont pas utilisé:</br>
docker image prune
<br>image spécifique : </br>
docker image rm busybox
<br>toute les images de busybox(a vérifier car j'ai un conflit):
docker rmi $(docker images 'busybox' -q)</br>


You can use the `prune` command
