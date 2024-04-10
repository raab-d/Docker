# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
- Pull `busybox` from the gitlab registry

1. What is the default registry ? 
Le registre par défaut de Docker est Docker Hub (registry.hub.docker.com). C'est le service de cloud public pour trouver et partager des conteneurs Docker. Quand vous utilisez docker pull sans spécifier un registre, Docker cherche l'image dans Docker Hub par défaut.
2. What is the différence between these images ?
Les images busybox tirées de Docker Hub et du registre GitLab devraient être fonctionnellement identiques car elles sont censées être des miroirs l'une de l'autre. Cependant, il peut y avoir des différences en termes de :

Version: Selon la fréquence de la synchronisation du miroir, il pourrait y avoir de légères différences de versions ou de patches entre les registres.
Taille: Bien que les images soient similaires, des différences de compression ou de construction peuvent entraîner des variations de taille.
Sécurité et conformité: Certains environnements peuvent préférer utiliser des images d'un registre spécifique pour des raisons de politique de sécurité ou de conformité.
3. Remove all images that aren't from the default registry.

## Work with container

1. Run a busybox container
docker run busybox

   1. What happend ?
   il ne se passe rien car se termine immédiatement. C'est parce que busybox est une image minimaliste conçue pour exécuter une commande spécifique et se terminer après l'exécution de cette commande. Si aucune commande n'est spécifiée, il n'y a rien à exécuter, donc le conteneur s'arrête.
   2. Fix it with a sleep
   docker run busybox sleep 1000

2. Run a busybox container that said "Hello world"
docker run busybox echo "Hello world"

3. Instantiate an interactive shell with busybox
docker run -it busybox sh

   1. Run a Hello world inside the container
   echo 'hello world'
   2. Leave the container
   exit
   3. What happened ?
   Cela arrêtera le conteneur car le processus principal (le shell interactif dans ce cas) s'est terminé.
4. Run a container in background that say "Hello world"
5. Find the container id
   docker ps -lq
   4c4ee9f77e07
6. Print the container logs
   Hello world
7. Stop the container
   docker stop 4c4ee9f77e07
   4c4ee9f77e07
8. List all container
docker ps

   1. What happend ?
   Les conteneurs qui s'exécutent en arrière-plan ou avec des commandes rapides (comme echo) s'arrêtent une fois la commande terminée. La commande docker ps ne montrera pas ces conteneurs car ils ne sont plus actifs.
   2. List all container even the one that is stopped
   docker ps -a


9. Delete the stopped container
   4c4ee9f77e07
10. Delete all stopped containers
docker container prune

Deleted Containers:
12586ddb409e0356596a176b0c0de26638516fcb82cdd3050ce3e4549f35d830
31bc765acdc490aae8f6ba2d8cb50691175b58722d70887df8024f5dc8a802d5
4f67635e2b4dab1da9f3638fa58139bcd961cb5ea3b4110d5dfefacd3ea86612

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
docker run --rm -it busybox

   1. Create a txt file with "Hello"
   echo '3aslamanwen' > 3aslamanwen.txt
   2. Exit the container
   exit
2. Re-run the container 
docker run --rm -it busybox

3. Check the file 
4. What happened ?
on ne trouve pas le fichier 3aslamanwen.txt que nous avons créé dans le premier conteneur. Ceci est dû à la nature éphémère du conteneur que nous avons utilisé. Lorsque nous avons quitté le premier conteneur, il a été supprimé en raison de l'option --rm, y compris tous les fichiers et modifications que nous avons effectués. Le second conteneur que nous avons lancé est une nouvelle instance fraîche basée sur l'image busybox, sans aucune des modifications effectuées dans le conteneur précédent.

## Clean up

1. List all images
   docker images
2. Delete busybox images
docker rmi busybox

You can use the `prune` command