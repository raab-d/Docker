# Lab 3 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`  

   Unable to find image 'couchdb:2.1' locally  
   2.1: Pulling from library/couchdb  
   d660b1f15b9b: Pull complete  
   0d7aab2be023: Pull complete  
   f58c3777efba: Pull complete  
   1acbc80638bb: Pull complete  
   d6a82611f685: Pull complete  
   27abbe831be1: Pull complete  
   2e41520ee187: Pull complete  
   f8d127415410: Pull complete  
   18cc54fd89c6: Pull complete  
   896902be7e0e: Pull complete  
   Digest: sha256:05a8b4a9bfe8e90fdf8630b404098aab5122c8ead228ad9b8d081309266b1cfb  
   Status: Downloaded newer image for couchdb:2.1  
   06ddfd6c9913ea30aaa058d1ddea3355a101dd8e9968631ce5dc2547210097b2 

2. Check existing volumes 

#docker volume ls  

   1. Why there is already a volume ?

   #l'image couchdb créer un volume pour stocker un os linux pour fonctionner

3. Identify the volume that is used by `couchdb`  

a22b1509c259afb005eade8a10568d4a1046454561817ecd28e8eb88c0181834

4. Mount the identified volume to busybox  

docker container run -it --rm --volumes-from=couchdb busybox

5. Check files inside `/opt/couchdb/data`  

   /opt/couchdb/data # ls  
   _dbs.couch         _nodes.couch       _replicator.couch  _users.couch  

6. Stop couchdb
 
   # docker stop couchdb  

7. Delete the volume  

   # docker container rm couchdb   
   # docker volume rm a22b1509c259afb005eade8a10568d4a1046454561817ecd28e8eb88c0181834  

8. Check that the volume has been deleted 

   # docker volume ls  
   # DRIVER VOLUME NAME  

### Create a named volume

1. Create a volume named : `couchdb_vol` 

   # docker volume create couchdb_vol

2. Run `couchedb` with the created volume  

   # docker container run --name couchdb -d -p 5984:5984 -v couchdb_vol:/opt/couchdb/data couchdb 

   #3H5b2cf46255ff719a27a86a2636f1092d71906685b5f174bce665afdf41fb87

3. Inspect the container and look at `Mounts` that `couchdb_vol` is used  
[{"Type":"volume","Name":"couchdb_vol","Source":"/var/lib/docker/volumes/couchdb_vol/_data","Destination":"/opt/couchdb/data","Driver":"local","Mode":"z","RW":true,"Propagation":""}]



### Mount directory

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container  

   # docker container run -it --rm -v /var/lib/docker:/dck busybox  

2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available  

      / # cd dck/volumes/  
      /dck/volumes # ls  

      backingFsBlockDev  couchdb_vol        metadata.db  
      /dck/volumes #  

### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`

   # mkdir sidecar

2. Run Busybox  

   # docker container run --name gen_date -it -v /var/lib/docker/sidecar:/dck busybox  

   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`

   2. Volume to mount: `$(pwd)/sidecar:/dck`

   3. Name: `gen_date`

   4. State: detached

3. Check the content of `sidecar/date.log` with `cat`  

      cat dck/date.log  
      Wed Apr 10 14:14:37 UTC 2024  
      Wed Apr 10 14:14:39 UTC 2024  
      Wed Apr 10 14:14:39 UTC 2024  
      Wed Apr 10 14:27:18 UTC 2024  
      Wed Apr 10 14:27:18 UTC 2024  
      Wed Apr 10 14:28:46 UTC 2024  
      Wed Apr 10 14:28:47 UTC 2024  
      Wed Apr 10 14:28:48 UTC 2024  
      Wed Apr 10 14:28:50 UTC 2024  

4. Run Busybox  

   # docker container run -it --rm -v /var/lib/docker/sidecar:/dck2 busybox  

   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached

5. Check content of `dck2/date.log` with `tail -f`

      tail -f /dck2/date.log  
      Wed Apr 10 14:14:37 UTC 2024  
      Wed Apr 10 14:14:38 UTC 2024  
      Wed Apr 10 14:14:39 UTC 2024  

6. Exit container

7. Run `docker kill gen_date` `` 
# docker kill gen_date
# Error response from daemon: Cannot kill container: gen_date: Container 3076b4bfdabff7160d4419bd770d065c1d8df421fe00836f157aff37552f5884 is not running

   1. Why is the container stoped ?
   # quitter le conteneur et comme il n'est plus utiliser il s'arrête pour économiser les ressources

### In memory 

1. Run busybox with `--tmpfs /test`  
2. Check with `mount | grep test` that tmpfs is used  
   # mount | grep test  
   # tmpfs on /test type tmpfs (rw,nosuid,nodev,noexec,relatime)  