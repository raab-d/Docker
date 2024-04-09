# Lab 1 - Hands on Docker

## Pull your first images.

### Tips

- Busybox from the docker hub registry: `registry.hub.docker.com/library/busybox`
- Pull busybox from another registry: `registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox`

### Images from different registry

- Pull `busybox` from the default registry
   # docker pull busybox
- Pull `busybox` from the gitlab registry
   # docker pull registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox


1. What is the default registry ?
   # Le registre par défaut est généralement Docker Hub
2. What is the différence between these images ?
   # Les différences entre les images dépendent de leur provenance   
3. Remove all images that aren't from the default registry.
   # docker image prune -a 
   # avec un filtre docker image prune -a --filter "until=1h"
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker image prune -a --filter "until=1h"
   WARNING! This will remove all images without at least one container associated to them.
   Are you sure you want to continue? [y/N] y
   Deleted Images:
   untagged: busybox:latest
   untagged: busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966deleted: sha256:ba5dc23f65d4cc4a4535bce55cf9e63b068eb02946e3422d3587e8ce803b6aab
   deleted: sha256:95c4a60383f7b6eb6f7b8e153a07cd6e896de0476763bef39d0f6cf3400624bd
   untagged: registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox:latest
   untagged: registry.gitlab.com/gitlab-org/cloud-native/mirror/images/busybox@sha256:2376a0c12759aa1214ba83e771ff252c7b1663216b192fbe5e0fb364e952f85c
   deleted: sha256:5242710cbd55829f6c44b34ff249913bb7cee748889e7e6925285a29f126aa78
   deleted: sha256:feb4513d4fb7052bcff38021fc9ef82fd409f4e016f3dff5c20ff5645cde4c02

   Total reclaimed space: 8.523MB
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker image prune -a                    
   WARNING! This will remove all images without at least one container associated to them.
   Are you sure you want to continue? [y/N] y
   Total reclaimed space: 0B
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker image ls
   REPOSITORY   TAG       IMAGE ID   CREATED   SIZE

## Work with container

1. Run a busybox container
   # docker run busybox
    #""" PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker run busybox
      Unable to find image 'busybox:latest' locally
      latest: Pulling from library/busybox
      7b2699543f22: Pull complete
      Digest: sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
      Status: Downloaded newer image for busybox:latest
      PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker image ls   
      REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
      busybox      latest    ba5dc23f65d4   10 months ago   4.26MB
   1. What happend ?"""
     # Le conteneur busybox démarre, mais il se ferme immédiatement car il n'a pas de processus en cours d'exécution pour maintenir le conteneur ouvert.
   2. Fix it with a sleep
      # docker run busybox sleep 15 

2. Run a busybox container that said "Hello world"
   # PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker run busybox echo "Hello world" >> Hello world
3. Instantiate an interactive shell with busybox
   1. Run a Hello world inside the container
   # PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker run -it busybox sh
      >>
      / # echo "Hello world"
      Hello world
      / #
   
   2. Leave the container
   / exit

   3. What happened ?
   # he came back to the cmd, and the image is not delet or pure 
   # / # exit 
   # PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker>

   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker container ls
   CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker container ls -a
   CONTAINER ID   IMAGE     COMMAND                CREATED         STATUS                   
         PORTS     NAMES
   a4941f05d60b   busybox   "sh"                   3 minutes ago   Exited (0) About a minute ago             zealous_moser
   bb68574ffb70   busybox   "echo 'Hello world'"   4 minutes ago   Exited (0) 4 minutes ago                  modest_wing
   53d90437ab0d   busybox   "sleep 15"             5 minutes ago   Exited (0) 4 minutes ago                  nostalgic_bassi
   7b94cdfd3f7d   busybox   "sh"                   7 minutes ago   Exited (0) 7 minutes ago                  sad_visvesvaraya
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> 

4. Run a container in background that say "Hello world"
   # docker run -d busybox echo "Hello world"
   # 8889cad416b60d12df3501880c9ac73fc9a4262b48c2d9dd42fb83b739e10896

5. Find the container id
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker run -d --name sfc busybox  sleep 60
   afc9e40f0fe92e1c17b243c080c780d90c20b296eb8db43ef8daecc8984f92ad
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker ps 
   CONTAINER ID   IMAGE     COMMAND      CREATED         STATUS         PORTS     NAMES
   afc9e40f0fe9   busybox   "sleep 60"   3 seconds ago   Up 2 seconds             sfc

6. Print the container logs
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker run -d --name soo busybox  echo "hello" sleep 200
   49d8e1093d10025d6a6131ceeb1423dc217b4e08dd0775825d881c20b1095ec6
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker logs soo
   hello sleep 200
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> 
7. Stop the container
   # he will stop after 200 secs 
   # docker kill soo

8. List all container
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker container ls                              
   CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS         PORTS     NAMES
   0cb4d138c705   busybox   "sleep 200"   2 minutes ago   Up 2 minutes             sfc

   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> 
   1. What happend ?
      # sfc toune, he wil stop after few seconds 
      # the other container are stoped after their commande so they are in the -a 
   2. List all container even the one that is stopped
         PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker container ls -a
         CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS                          PORTS     NAMES
         49d8e1093d10   busybox   "echo hello sleep 200"   About a minute ago   Exited (0) About a minute ago             soo
         0cb4d138c705   busybox   "sleep 200"              2 minutes ago        Up 2 minutes                              sfc
         22b6d383b2cd   busybox   "--name c1 echo 'hel…"   12 minutes ago       Created                                   strange_jennings
         27ee67c52bca   busybox   "echo 'Hello world'"     13 minutes ago       Exited (0) 13 minutes ago                 suspicious_cannon
         b500dd270639   busybox   "echo 'Hello world'"     16 minutes ago       Exited (0) 16 minutes ago                 jovial_lehmann
         8889cad416b6   busybox   "echo 'Hello world'"     16 minutes ago       Exited (0) 16 minutes ago                 magical_poitras
         a4941f05d60b   busybox   "sh"                     22 minutes ago       Exited (0) 21 minutes ago                 zealous_moser
         bb68574ffb70   busybox   "echo 'Hello world'"     24 minutes ago       Exited (0) 24 minutes ago                 modest_wing
         53d90437ab0d   busybox   "sleep 15"               24 minutes ago       Exited (0) 24 minutes ago                 nostalgic_bassi
         7b94cdfd3f7d   busybox   "sh"                     27 minutes ago       Exited (0) 27 minutes ago                 sad_visvesvaraya

9. Delete the stopped container
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> 
   docker stop ( or kill ) soo 
   docker rm soo 
   soo
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker container ls -a
   CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS     NAMES
   0cb4d138c705   busybox   "sleep 200"              4 minutes ago    Exited (0) 44 seconds ago             sfc
   22b6d383b2cd   busybox   "--name c1 echo 'hel…"   13 minutes ago   Created                               strange_jennings
   27ee67c52bca   busybox   "echo 'Hello world'"     14 minutes ago   Exited (0) 14 minutes ago             suspicious_cannon
   b500dd270639   busybox   "echo 'Hello world'"     17 minutes ago   Exited (0) 17 minutes ago             jovial_lehmann
   8889cad416b6   busybox   "echo 'Hello world'"     18 minutes ago   Exited (0) 18 minutes ago             magical_poitras
   a4941f05d60b   busybox   "sh"                     24 minutes ago   Exited (0) 23 minutes ago             zealous_moser
   bb68574ffb70   busybox   "echo 'Hello world'"     26 minutes ago   Exited (0) 26 minutes ago             modest_wing
   53d90437ab0d   busybox   "sleep 15"               26 minutes ago   Exited (0) 26 minutes ago             nostalgic_bassi
   7b94cdfd3f7d   busybox   "sh"                     28 minutes ago   Exited (0) 28 minutes ago             sad_visvesvaraya

10. Delete all stopped containers
   # docker container prune
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker container prune
   WARNING! This will remove all stopped containers.
   Are you sure you want to continue? [y/N] y
   Deleted Containers:
   0cb4d138c70515f50cf8ab1c2a587a08ca0f2df57ba6354f01726af45b0b314b
   22b6d383b2cd044b3fcf6fb110eed7206ca73333a324430b14b95be7209a28cd
   27ee67c52bcad4904c5b75bfeb192146d638be918cc31be60d508925abe6c6ab
   b500dd270639fcaa64a1cfdd355357c4538c3cfce8394753f4431facb9b823fd
   8889cad416b60d12df3501880c9ac73fc9a4262b48c2d9dd42fb83b739e10896
   a4941f05d60bee550111233567a4f3aaab5980656f1b24e4ca610d47a10d3499
   bb68574ffb70dea74ffbe2b724768c19897b79ef83ed6ed1bd56b1d8f00a6154
   53d90437ab0d30cbe217bfb14fc0afce8f1202953fcd73351ee898e948a08029
   7b94cdfd3f7d1c815855d7f3419961c96049a879b8153ed2bb90edcc5a8a01e6

   Total reclaimed space: 25B
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker container ls -a
   CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

## Work with ephemeral container

1. Run a interactif container with busybox that will be deleted at stop
   # docker run -it --rm busybox
   1. Create a txt file with "Hello"
      PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker run -it --rm busybox
      >> echo "Hello" > hello.txt

   2. Exit the container
      / # exit

2. Re-run the container 
      PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker run -it --rm busybox
3. Check the file 
      / # cat hello.txt
      cat: can't open 'hello.txt': No such file or directory

4. What happened ?
 # when i just exit the container the rm do remove it 

## Clean up

1. List all images
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker image list
   REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
   busybox      latest    ba5dc23f65d4   10 months ago   4.26MB

2. Delete busybox images

   busybox      latest    ba5dc23f65d4   10 months ago   4.26MB
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> docker rmi $(docker images -q busybox)
   Untagged: busybox:latest
   Untagged: busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
   Deleted: sha256:ba5dc23f65d4cc4a4535bce55cf9e63b068eb02946e3422d3587e8ce803b6aab
   Deleted: sha256:95c4a60383f7b6eb6f7b8e153a07cd6e896de0476763bef39d0f6cf3400624bd
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs\10-lab-hands-on-docker> 
You can use the `prune` command