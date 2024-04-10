# Lab 4 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`

docker container run --name couchdb -d -p 5984:5984 couchdb:2.1
035c5ae0beb2230decb5c1533c6535038e6d890811dc68c190bd4458f32810bc

2. Check existing volumes

   docker volume ls
   DRIVER    VOLUME NAME
   local     c83148ead17f4c9a3fce5c8e9cea42324b762d0f4ac6886aca78880e179182b0

   1. Why there is already a volume ?

   Docker créé automatiquement des volumes pour stocker des containers de type couchdb (bases de données) afin de sauvegarder les modifications (ajouts ou modification) appliquées dans le container de type couchdb. Le volume existant est donc le volume associé à notre couchdb.

3. Identify the volume that is used by `couchdb`

docker inspect couchdb

"Mounts": [
            {
                "Type": "volume",
                "Name": "c83148ead17f4c9a3fce5c8e9cea42324b762d0f4ac6886aca78880e179182b0",
                "Source": "/var/lib/docker/volumes/c83148ead17f4c9a3fce5c8e9cea42324b762d0f4ac6886aca78880e179182b0/_data",
                "Destination": "/opt/couchdb/data",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],

4. Mount the identified volume to busybox 

docker run --rm -it --name bbx --mount source=c83148ead17f4c9a3fce5c8e9cea42324b762d0f4ac6886aca78880e179182b0,target=/data busybox sh

5. Check files inside `/opt/couchdb/data`

/ # ls /data
_dbs.couch         _nodes.couch       _replicator.couch  _users.couch

6. Stop couchdb

docker stop couchdb                                                                                        
couchdb

7. Delete the volume

docker volume ls
DRIVER    VOLUME NAME
local     c83148ead17f4c9a3fce5c8e9cea42324b762d0f4ac6886aca78880e179182b0

docker volume rm c83148ead17f4c9a3fce5c8e9cea42324b762d0f4ac6886aca78880e179182b0
c83148ead17f4c9a3fce5c8e9cea42324b762d0f4ac6886aca78880e179182b0

8. Check that the volume has been deleted

docker volume ls
DRIVER    VOLUME NAME

### Create a named volume

1. Create a volume named : `couchdb_vol`

docker volume create couchdb_vol
couchdb_vol

2. Run `couchedb` with the created volume

docker run --name couchdb -d -p 5984:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1
658c667d3253287cbbfdbf64f07725e20aea35a25de01846ea9767b3924b02af

3. Inspect the container and look at `Mounts` that `couchdb_vol` is used

docker inspect couchdb_vol
[
    {
        "CreatedAt": "2024-04-10T12:58:16Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/couchdb_vol/_data",
        "Name": "couchdb_vol",
        "Options": null,
        "Scope": "local"
    }
]

### Mount directory

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container 

docker run -it --rm --name busyboxtest -v /var/lib/docker:/dck busybox

2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available

/ # ls /dck/volumes/couchdb_vol/_data
_dbs.couch         _nodes.couch       _replicator.couch  _users.couch

### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`

mkdir sidecar

2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`

   Insère des dates dans les logs

   2. Volume to mount: `$(pwd)/sidecar:/dck`

   Permet d'associer le volume au répertoire sidecar

   3. Name: `gen_date`

   --name gen_date

   4. State: detached

   On ajoute -d à "docker run" pour l'utiliser en arrière-plan

   docker run -d --name gen_date -v $(pwd)/sidecar:/dck busybox `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`

3. Check the content of `sidecar/date.log` with `cat`



4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached
5. Check content of `dck2/date.log` with `tail -f`
6. Exit container
7. Run `docker kill gen_date`
   1. Why is the container stoped ?

### In memory 

1. Run busybox with `--tmpfs /test`
2. Check with `mount | grep test` that tmpfs is used 

