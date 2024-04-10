# Lab 4 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
Digest: sha256:05a8b4a9bfe8e90fdf8630b404098aab5122c8ead228ad9b8d081309266b1cfb
Status: Downloaded newer image for couchdb:2.1
1ad5f3353973997826259d0aa78f19f3b6f7fbbd8cefeac1c7ce1c5740e259bf
2. Check existing volumes
"Mounts": [
            {
                "Type": "volume",
                "Name": "ff8a8079a6441b7a8c640796de15d68dbff9052eb68f8110074af280825788cb",
                "Source": "/var/lib/docker/volumes/ff8a8079a6441b7a8c640796de15d68dbff9052eb68f8110074af280825788cb/_data",
                "Destination": "/opt/couchdb/data",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],
   1. Why there is already a volume ?
   L'image couchdb est configurée pour stocker les données de la base de données dans un volume pour garantir leur persistance. Lorsque le conteneur est créé à partir de cette image, Docker crée automatiquement un volume pour ce stockage persistant si aucun volume n'est explicitement spécifié.
3. Identify the volume that is used by `couchdb`
Source": "/var/lib/docker/volumes/ff8a8079a6441b7a8c640796de15d68dbff9052eb68f8110074af280825788cb/_data"
4. Mount the identified volume to busybox 
5. Check files inside `/opt/couchdb/data`
_dbs.couch         _nodes.couch       _replicator.couch  _users.couch
6. Stop couchdb
7. Delete the volume
8. Check that the volume has been deleted

### Create a named volume

1. Create a volume named : `couchdb_vol` docker volume create couchdb_vol

2. Run `couchedb` with the created volume docker run --name couchdb2 -d -p 5985:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1

3. Inspect the container and look at `Mounts` that `couchdb_vol` is used
Mounts": [
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
2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available
_dbs.couch         _nodes.couch       _replicator.couch  _users.couch

### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`
2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached
   $dockerPath = $PWD.Path -replace '^C:', '/c'
$dockerPath = $dockerPath -replace '\\', '/'
docker run -d --name gen_date -v "${dockerPath}/sidecar:/dck" busybox /bin/sh -c 'while true; do date >> /dck/date.log; sleep 1; done'

3. Check the content of `sidecar/date.log` with `cat`
cat sidebar/data.log
4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached
5. Check content of `dck2/date.log` with `tail -f`
6. Exit container
7. Run `docker kill gen_date`
   1. Why is the container stoped ?
   Le conteneur gen_date s'est arrêté parce que nous avons exécuté la commande docker kill, qui envoie un signal SIGKILL au processus principal du conteneur (sh -c 'while true; do date >> /dck/date.log; sleep 1; done'). Ce signal arrête immédiatement le processus sans attendre une fermeture propre, ce qui entraîne l'arrêt du conteneur.

### In memory 

1. Run busybox with `--tmpfs /test` docker run -it --rm --tmpfs /test busybox

2. Check with `mount | grep test` that tmpfs is used 
tmpfs on /test type tmpfs (rw,nosuid,nodev,noexec,relatime)

