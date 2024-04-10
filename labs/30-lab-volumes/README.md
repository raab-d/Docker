# Lab 4 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
==> Unable to find image 'couchdb:2.1' locally
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
    9bda8e30f948efa028f9b273740196e1a9c06924ec488cac2649b44306100446

2. Check existing volumes 
==> docker volume ls
DRIVER    VOLUME NAME
local     586926cde806e62b05fe3b493d18ade872e29b4e7d978ac01e12d16c84294977

==> docker volume inspect 586926cde806e62b05fe3b493d18ade872e29b4e7d978ac01e12d16c84294977
   [
    {
        "CreatedAt": "2024-04-10T12:27:18Z",
        "Driver": "local",
        "Labels": {
            "com.docker.volume.anonymous": ""
        },
        "Mountpoint": "/var/lib/docker/volumes/586926cde806e62b05fe3b493d18ade872e29b4e7d978ac01e12d16c84294977/_data",
        "Name": "586926cde806e62b05fe3b493d18ade872e29b4e7d978ac01e12d16c84294977",
        "Options": null,
        "Scope": "local"
    }
]
   1. Why there is already a volume ?
    Certains conteneurs Docker, lorsqu'ils sont lancés sans spécification explicite de gestion de volume, peuvent automatiquement créer des volumes pour stocker des données spécifiques. Docker crée automatiquement des volumes anonymes pour ces emplacements. Ces volumes anonymes assurent que les données stockées dans les répertoires spécifiés restent persistantes même après que le conteneur soit arrêté ou supprimé, à moins que le volume lui-même ne soit explicitement supprimé.

3. Identify the volume that is used by `couchdb`
==> docker container inspect couchdb  
Type : volume
Name : 586926cde806e62b05fe3b493d18ade872e29b4e7d978ac01e12d16c84294977
Source : /var/lib/docker/volumes/586926cde806e62b05fe3b493d18ade872e29b4e7d978ac01e12d16c84294977/_data
Destination : /opt/couchdb/data
Le volume est donc : 586926cde806e62b05fe3b493d18ade872e29b4e7d978ac01e12d16c84294977

4. Mount the identified volume to busybox 
==> docker container run -it -v 586926cde806e62b05fe3b493d18ade872e29b4e7d978ac01e12d16c84294977:/data busybox

5. Check files inside `/opt/couchdb/data`
==> / # ls /data
   _dbs.couch         _nodes.couch       _replicator.couch  _users.couch

6. Stop couchdb
==> docker container stop couchdb
il est bien arrete
7. Delete the volume
==> docker volume rm 586926cde806e62b05fe3b493d18ade872e29b4e7d978ac01e12d16c84294977
Pour supprimer le volume, je doit arreter aussi le container du busybox et supprimer les deux container pour pouvoir supprimer le volume.

8. Check that the volume has been deleted
==> docker volume ls
on aura le resultat suivant 
DRIVER    VOLUME NAME

### Create a named volume

1. Create a volume named : `couchdb_vol`
==> docker volume create couchdb_vol
couchdb_vol

2. Run `couchedb` with the created volume
==> docker container run --name couchdb_with_volume -d -p 5984:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1
bae4e8e4920f7b37bbe0a29d1d5eb5ef59ab88226af518dcee5e94ff569b9e0d

3. Inspect the container and look at `Mounts` that `couchdb_vol` is used
==> docker container inspect couchdb_with_volume
Pour la partie Mounts:
"Mounts": [
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
],

### Mount directory

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container 
==> docker container run -it -v /var/lib/docker:/dck busybox
apres on devrai les etapes suivantes pour bien verifier si le mountage a bien ete fait 
/ # cd /dck
/dck # ls
buildkit    containers  engine-id   image       network     overlay2    plugins     runtimes    swarm       tmp         volumes

2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available
==> ls /dck/volumes/couchdb_vol/_data
j'ai eu le retour suivant :
_dbs.couch         _nodes.couch       _replicator.couch  _users.couch

### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`
==> mkdir sidecar
2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached
==> la commande est : docker run -d --name gen_date -v $(pwd)/sidecar:/dck busybox sh -c 'while true; do date >> /dck/date.log; sleep 1; done'
j'ai le retour suivant : 15c8bd295ed48abb5d6e7ee35af4dd0667d62012a74f5bbff47cc7c05283e0fd

3. Check the content of `sidecar/date.log` with `cat`
==> cat sidecar/date.log
Le contenu du fichier date.log présente une série d'horodatages régulièrement générés toutes les secondes. Cela confirme que le processus en cours dans le conteneur fonctionne comme prévu et écrit les horodatages dans le fichier spécifié. Ce comportement correspond à la commande exécutée lors du démarrage du conteneur.

4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached
==> docker run -it --name watch_log -v $(pwd)/sidecar:/dck2 busybox

5. Check content of `dck2/date.log` with `tail -f`
ca affiche aussi le tismestap un par un

6. Exit container
"CTRL C" pour quitter la commande tail ensuite exit pour quitter le terminal du conteneur.

7. Run `docker kill gen_date`
   1. Why is the container stoped ?
   la commande kill est faite pour forcer et obliger l'arrêt du conteneur.

### In memory 

1. Run busybox with `--tmpfs /test`
==> docker run -it --rm --name tmpfs-test --tmpfs /test busybox
2. Check with `mount | grep test` that tmpfs is used 
/ # mount | grep test
j'ai ce retour :
tmpfs on /test type tmpfs (rw,nosuid,nodev,noexec,relatime)
