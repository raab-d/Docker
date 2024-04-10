# Lab 4 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
2. Check existing volumes
   1. Why there is already a volume ? <br>
      Parce que douchdb est une base de données orienté documents, il a besoin d'initialisé un volume.
3. Identify the volume that is used by `couchdb` <br>
   En utilisant la commande `docker container inspect couchdb` <br>
   "Mounts": [
            {
                "Type": "volume",
                "Name": "51f0b6e852f9ea1c5437dde37aebe32758af041f3afd3550f5bcd464a3de5b20",
                "Source": "/var/lib/docker/volumes/51f0b6e852f9ea1c5437dde37aebe32758af041f3afd3550f5bcd464a3de5b20/_data",
                "Destination": "/opt/couchdb/data",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ]
4. Mount the identified volume to busybox <br>
   `docker container run --name busybox -it -v 51f0b6e852f9ea1c5437dde37aebe32758af041f3afd3550f5bcd464a3de5b20:/data busybox`
5. Check files inside `/opt/couchdb/data` <br>
    *_dbs.couch         _nodes.couch       _replicator.couch  _users.couch*
6. Stop couchdb <br>
   `docker container stop couchdb`
7. Delete the volume <br>
   Il faut supprimer les containers utilisant le volume, les stopper ne suffit pas car le volume est toujours utilisé (si on redémarre le containers il doit pouvoir accéder au volume à nouveau). <br>
   `docker container prune`
   `docker volume rm 51f0b6e852f9ea1c5437dde37aebe32758af041f3afd3550f5bcd464a3de5b20`
8. Check that the volume has been deleted <br>
    `docker volume ls`
    
### Create a named volume

1. Create a volume named : `couchdb_vol` <br>
    `docker volume create couchdb_vol`
2. Run `couchedb` with the created volume <br>
    `docker container run --name couchdb -d -p 5984:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1`
3. Inspect the container and look at `Mounts` that `couchdb_vol` is used
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
        ]
### Mount directory

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container <br>
    `docker container run --name busybox -v /var/lib/docker:/dck -it busybox`
2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available
    *_dbs.couch         _nodes.couch       _replicator.couch  _users.couch* <br>
    On lie le répertoire en local /var/lib/docker au path dans le containers /dck. Le chemin source correspond au répertoire ou se situe tous les volumes que l'on crée.

### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`
2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached <br>
`docker container run --name gen_date -d -v ${PWD}/sidecar:/dck busybox sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
3. Check the content of `sidecar/date.log` with `cat` <br>
    Wed Apr 10 13:31:22 UTC 2024
    Wed Apr 10 13:31:23 UTC 2024
    Wed Apr 10 13:31:24 UTC 2024
    Wed Apr 10 13:31:25 UTC 2024
    Wed Apr 10 13:31:26 UTC 2024
    ...
4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached
`docker container run --name tail_date -v ${pwd}/sidecar:/dck2 busybox tail -f /dck2/date.log`
5. Check content of `dck2/date.log` with `tail -f` <br>
    Wed Apr 10 13:55:59 UTC 2024
    Wed Apr 10 13:56:00 UTC 2024
    Wed Apr 10 13:56:01 UTC 2024
6. Exit container
7. Run `docker kill gen_date`
   1. Why is the container stoped ? <br>
      la commmande kill permet d'envoyer directement le signal SIGKILL
      pour arreter brutalement le container. A l'inverse, stop va envoyer
      un signal SIGTERM pour arreter proprement le container. 
      Si au bout de 10s le containers n'est toujours pas fermé, 
      alors le signal SIGKILL est envoyé.

### In memory 

1. Run busybox with `--tmpfs /test` <br>
    `docker container run --name busybox_tmpfs -it --tmpfs /test busybox`
2. Check with `mount | grep test` that tmpfs is used <br>
    *tmpfs on /test type tmpfs (rw,nosuid,nodev,noexec,relatime)*


