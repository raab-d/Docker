# Lab 4 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
2. Check existing volumes
<br> docker container inspect couchdb
   1. Why there is already a volume ?
   <br> CouchDB utilise un volume pour stocker les données de manière persistante, cela permet que les données restent disponibles même après l'arrêt ou la suppression du conteneur.
3. Identify the volume that is used by `couchdb`
<br>  Grace à la commande docker container inspect couchdb <br>
"Mounts": [
		{
			"Type": "volume",
			"Name": "6a4dd5f5c9d9a6efeead0766b25680b4a9067028b3cb7adec6372cdb0bc9bad6",
			"Source": "/var/lib/docker/volumes/6a4dd5f5c9d9a6efeead0766b25680b4a9067028b3cb7adec6372cdb0bc9bad6/_data",
			"Destination": "/opt/couchdb/data",
			"Driver": "local",
			"Mode": "",
			"RW": true,
			"Propagation": ""
		}
	],
<br>
4. Mount the identified volume to busybox 
<br> docker run --rm -it --volume 6a4dd5f5c9d9a6efeead0766b25680b4a9067028b3cb7adec6372cdb0bc9bad6:/data busybox
5. Check files inside `/opt/couchdb/data`
<br> j'utilise la commande ls /data et j'ai cess 4 fichiers <br>
_dbs.couch <br>        _nodes.couch   <br>    _replicator.couch <br> _users.couch <br>
6. Stop couchdb
<br> docker stop couchdb
7. Delete the volume
<br> Avec cette commande docker volume rm 6a4dd5f5c9d9a6efeead0766b25680b4a9067028b3cb7adec6372cdb0bc9bad6 cela devrait nous permettre de supprimer le volume, mais nous ne pouvons pas, car nous avons juste stop le container et non supprimé donc on doit le supprimer avant de pouvoir supprimer le volume.
<br>  Donc pour le supprimé je fais un "docker container prune" puis on refait la même commande pour supprimer le volume
9. Check that the volume has been deleted
<br> docker volume ls cette commande nous permet de voir que le volume à bien était supprimer.

### Create a named volume

1. Create a volume named : `couchdb_vol`
<br> docker volume create couchdb_vol
2. Run `couchedb` with the created volume
<br> docker run --name couchdb -d -p 5984:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1  
3. Inspect the container and look at `Mounts` that `couchdb_vol` is used
<br> "Mounts": [
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
<br> docker run --rm -it -v /var/lib/docker:/dck busybox
2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available
<br> J'ai bien accé aux 4 fichiers qui sont dans mon volume avec le nouveau container

### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`
2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached
	<br> docker run -d --name gen_date -v ${PWD}/sidecar:/dck busybox /bin/sh -c 'while true; do date >> /dck/date.log; sleep 1; done'
	<br> j'ai du changer le (pwd) en {PWD} car je suis en windows powershell
3. Check the content of `sidecar/date.log` with `cat`
<br> on voit bien les logs
4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached
<br> docker run --rm -it --name log_viewer -v ${PWD}/sidecar:/dck2 busybox tail -f /dck2/date.log
<br> Lance un second conteneur BusyBox en mode attaché qui lit en continu le fichier log date.log à travers un montage de volume.
5. Check content of `dck2/date.log` with `tail -f`
<br> le contenu du fichier log est affiché en continu dans le terminal.
6. Exit container
7. Run `docker kill gen_date`
   1. Why is the container stoped ?
   <br> La commande docker kill force l'arrêt immédiat du conteneur spécifié en envoyant un signal. Cela est utile pour arrêter des conteneurs en exécution sans attendre la fin naturelle de leurs processus.

### In memory 

1. Run busybox with `--tmpfs /test`
<br> docker run --rm -it --tmpfs /test busybox
<br> Conteneur BusyBox avec un système de fichiers temporaire (tmpfs) monté à /test. tmpfs est un stockage volatile
2. Check with `mount | grep test` that tmpfs is used 
<br> tmpfs on /test type tmpfs (rw,nosuid,nodev,noexec,relatime)

