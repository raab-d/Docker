# Lab 4 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
2. Check existing volumes
Commande : docker container inspect couchdb
   1. Why there is already a volume ?
   Réponse : CouchDB utilise un volume par défaut pour stocker ses données. Quand on exécute un conteneur CouchDB sans spécifier de volume externe, Docker crée automatiquement un volume pour stocker les données de CouchDB.
3. Identify the volume that is used by `couchdb`
Réponse : Le volume utilisé par CouchDB peut être identifié en inspectant le conteneur CouchDB et en examinant la section "Mounts"
4. Mount the identified volume to busybox 
Commande : docker run -it --rm -v 575a049e1681acaa716202569a4c3145a8dc9f33761690a05e0e204928d2c0ed:/opt/couchdb/data busybox
5. Check files inside `/opt/couchdb/data`
Commande : ls /opt/couchdb/data
6. Stop couchdb
Commande : docker container stop couchdb
7. Delete the volume
Commande : docker volume rm couchdb 
8. Check that the volume has been deleted
Commande : docker volume ls
### Create a named volume

1. Create a volume named : `couchdb_vol`
Commande : docker volume create couchdb_vol
2. Run `couchedb` with the created volume 
Commande : docker container run --name couchdb -d -p 5984:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1
3. Inspect the container and look at `Mounts` that `couchdb_vol` is used
Commande : docker container inspect couchdb
### Mount directory

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container 
Commande : docker run -it --rm -v /var/lib/docker:/dck busybox
2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available
Commande : ls /dck/volumes/couchdb_vol/_data
### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`
Commande : mkdir sidecar
2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached
Commande : docker run -d --name gen_date -v $(pwd)/sidecar:/dck busybox sh -c 'while true; do date >> /dck/date.log; sleep 1; done'
3. Check the content of `sidecar/date.log` with `cat`
Commande : cat sidecar/date.log
4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached
Commande : docker run -it --rm --name read_date -v $(pwd)/sidecar:/dck2 busybox tail -f /dck2/date.log
5. Check content of `dck2/date.log` with `tail -f`
Commande : tail -f sidecar/date.log
6. Exit container
7. Run `docker kill gen_date`
Commande : docker kill gen_date
   1. Why is the container stoped ?
Réponse : Le conteneur est arrêté car il a été tué avec la commande docker kill.

### In memory 

1. Run busybox with `--tmpfs /test`
Commande : docker run -it --rm --tmpfs /test busybox
2. Check with `mount | grep test` that tmpfs is used 

