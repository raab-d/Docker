# Lab 4 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
$ docker container run --name couchdb -d -p 5984:5984 couchdb:2.1

2. Check existing volumes
   1. Why there is already a volume ?

   Les volumes sont créés automatiquement pour les données persistantes de certains conteneurs 
   (comme CouchDB), pour ne pas perdre ces données lorsque le conteneur est supprimé.


3. Identify the volume that is used by `couchdb`

$ docker container inspect couchdb
-> la section "Mounts" pour identifier le volume.

4. Mount the identified volume to busybox 
$ docker run -it --rm --volumes-from couchdb busybox

5. Check files inside `/opt/couchdb/data`
$ ls /opt/couchdb/data

6. Stop couchdb
$ docker stop couchdb

7. Delete the volume
-> le nom du volume avec docker volume ls, puis on supprime avec :
$ docker volume rm <volume_name>

8. Check that the volume has been deleted
$ docker volume ls


### Create a named volume

1. Create a volume named : `couchdb_vol`
$ docker volume create couchdb_vol

2. Run `couchedb` with the created volume
$ docker run --name couchdb2 -d -p 5985:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1

3. Inspect the container and look at `Mounts` that `couchdb_vol` is used
$ docker container inspect couchdb2
-> la section "Mounts" pour confirmer que couchdb_vol est utilisé.

### Mount directory

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container 
$ docker run -it --rm -v /var/lib/docker:/dck busybox

2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available
$ ls /dck/volumes/couchdb_vol/_data

### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`
$ mkdir sidecar

2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached

$ docker run -d --name gen_date -v $(pwd)/sidecar:/dck busybox sh -c 'while true; do date >> /dck/date.log; sleep 1; done'

3. Check the content of `sidecar/date.log` with `cat`
$ cat sidecar/date.log


4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached

$ docker run -it --rm -v $(pwd)/sidecar:/dck2 busybox tail -f /dck2/date.log

5. Check content of `dck2/date.log` with `tail -f`
-> Utilisez Ctrl+C pour interrompre tail -f et sortir du conteneur.
-> ou bien il faut ouvrir un autre terminal pour stoper directement le container en cours

6. Exit container
$ docker kill gen_date

7. Run `docker kill gen_date`
   1. Why is the container stoped ?
-> Le conteneur s'arrête parce que docker kill envoie un signal pour terminer immédiatement le conteneur.

### In memory 

1. Run busybox with `--tmpfs /test`
$ docker run -it --rm --tmpfs /test busybox

2. Check with `mount | grep test` that tmpfs is used 
$ mount | grep test




#REPONSES

Les commandes utiliser pour lab3 :

 1700  git status
 1701  git diff
 1702  git branch -v
 1703  git pull
 1704  git status
 1705  git merge main
 1706  git branch -v
 1707  cd ..
 1708  tree
 1709  ls
 1710  cd 30-lab-volumes/
 1711  ls
 1712  docker container run --name couchdb -d -p 5984:5984 couchdb:2.1
 1713  docker volume ls
 1714  docker container inspect couchdb
 1715  docker run -it --rm --volumes-from couchdb busybox
 1716  docker stop couchdb
 1717  docker volum rm 23e97bb7ff50d58b7605f515006ad63b3d540b4a7a15cb6646d083285921b8f2
 1718  docker volume rm 23e97bb7ff50d58b7605f515006ad63b3d540b4a7a15cb6646d083285921b8f2
 1719  docker ps -a
 1720  docker stop 1c5b2bbe028e7dd5623f8d1a7766058c6bfe7c61883f1173ed3cec705936abaa
 1721  docker rm 1c5b2bbe028e7dd5623f8d1a7766058c6bfe7c61883f1173ed3cec705936abaa
 1722  docker ps -a
 1723  docker volume rm 23e97bb7ff50d58b7605f515006ad63b3d540b4a7a15cb6646d083285921b8f2
 1724  docker ps -a
 1725  docker volume ls
 1726  docker volume create couchdb_vol
 1727  docker run --name couchdb2 -d -p 5985:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1
 1728  docker container inspect couchdb2
 1729  docker inspect -f '{{.Mounts}}' couchdb2
 1730  docker run -it --rm -v /var/lib/docker:/dck busybox
 1731  mkdir sidecar
 1732  ls
 1733  docker run -d --name gen_date -v $(pwd)/sidecar:/dck busybox sh -c 'while true; do date >> /dck/date.log; sleep 1; done'
 1734  ls sidecar/
 1735  cat sidecar/date.log
 1736  docker run -it --rm -v $(pwd)/sidecar:/dck2 busybox tail -f /dck2/date.log
 1737  docker kill gen_date
 1738  docker run -it --rm --tmpfs /test busybox
