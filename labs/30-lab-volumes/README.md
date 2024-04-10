# Lab 4 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
2. Check existing volumes
- docker container inspect couchdb

   1. Why there is already a volume ?
   - Docker crée automatiquement un volume pour l'emplacement /opt/couchdb/data s'il n'est pas fourni. Cela est dû à la configuration de l'image Docker elle-même, qui définit /opt/couchdb/data comme un volume.

3. Identify the volume that is used by `couchdb`
- 511a2d943676f471b010089992adab76f8ef690d23afdc4a3118af73ab8c0038

4. Mount the identified volume to busybox 
- docker run -it --rm --volume 511a2d943676f471b010089992adab76f8ef690d23afdc4a3118af73ab8c0038:/data busybox

5. Check files inside `/opt/couchdb/data`
- ls /data
- _dbs.couch         _nodes.couch       _replicator.couch  _users.couch

6. Stop couchdb
-docker stop couchdb

7. Delete the volume
- docker rm couchdb
- docker volume rm 511a2d943676f471b010089992adab76f8ef690d23afdc4a3118af73ab8c0038

8. Check that the volume has been deleted
- docker volume ls


### Create a named volume

1. Create a volume named : `couchdb_vol`
- docker volume create couchdb_vol

2. Run `couchedb` with the created volume
- docker run --name couchdb -d -p 5984:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1

3. Inspect the container and look at `Mounts` that `couchdb_vol` is used
-  "Mounts": [
            {
                "Type": "volume",
                "Name": "couchdb_vol",
                "Source": "/var/lib/docker/volumes/couchdb_vol/_data",
                "Destination": "/opt/couchdb/data",
                "Driver": "local",
                "Mode": "z",
                "RW": true,
                "Propagation": ""
            }
        ]

### Mount directory

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container 
- docker run -it --rm -v /var/lib/docker:/dck busybox

2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available
- ls /dck/volumes/couchdb_vol/_data
- _dbs.couch         _nodes.couch       _replicator.couch  _users.couch

### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`
- mkdir sidecar

2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached

   - $dockerPath = $PWD.Path.Replace('\','/').Replace('C:','//c')
   - docker run -d --name gen_date -v "${dockerPath}/sidecar:/dck" busybox /bin/sh -c 'while true; do date >> /dck/date.log; sleep 1; done'
 
   - 54ecbdf7e8f589b24363c98c899c727822fd5dbf6047b39339fdb445e8dc635c

3. Check the content of `sidecar/date.log` with `cat`
- cat sidecar/date.log

4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached

   - $dockerPath = (Get-Location).Path.Replace('\','/').Replace('C:', '/c')
   - docker run -it --rm -v "${dockerPath}/sidecar:/dck2" busybox sh -c 'tail -f /dck2/date.log'

5. Check content of `dck2/date.log` with `tail -f`
6. Exit container
- CTRL+C

7. Run `docker kill gen_date`
   1. Why is the container stoped ?
   - Le conteneur gen_date est arrêté parce que la commande docker kill envoie un signal pour terminer immédiatement le processus du conteneur. C'est une manière forcée d'arrêter des conteneurs sans attendre la fin naturelle de leurs processus.

### In memory 

1. Run busybox with `--tmpfs /test`
2. Check with `mount | grep test` that tmpfs is used 
- tmpfs on /test type tmpfs (rw,nosuid,nodev,noexec,relatime)
