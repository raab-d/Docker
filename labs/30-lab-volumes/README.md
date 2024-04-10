# Lab 4 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
	Version indisponible sur l'architecture ARM64 v8
	"docker pull --platform linux/arm64/v8 couchdb:latest" pour indiquer à Docker de chercher et de télécharger la version de l'image qui est compatible avec l'architecture ARM64 v8
	Puis on lance cette commande plutôt : "docker run -d --name couchdb \
  -p 5984:5984 \
  -e COUCHDB_USER=admin \
  -e COUCHDB_PASSWORD=password \
  couchdb " pour éviter l'erreur "*************************************************************
ERROR: CouchDB 3.0+ will no longer run in "Admin Party"
       mode. You *MUST* specify an admin user and
       password, either via your own .ini file mapped
       into the container at /opt/couchdb/etc/local.ini
       or inside /opt/couchdb/etc/local.d, or with
       "-e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password"
       to set it via "docker run".
*************************************************************"
2. Check existing volumes
	docker volume ls
   1. Why there is already a volume ?
   		Il y'a déjà un volume qui est d'ailleurs anonyme car le conteneur qui lui est rattaché (couchdb) a été créé avec une image spécifiant un volume et aucun nom de volume ne lui a été fourni donc il crée un volume anonyme.

3. Identify the volume that is used by `couchdb`
	On lance la commande "docker container inspect couchdb" et la partie ""Mounts": [
            {
                "Type": "volume",
                "Name": "4e49b00439a8a2cba6aba3f34f2bb914f9ec478abe99688c86386fe904396495",
                "Source": "/var/lib/docker/volumes/4e49b00439a8a2cba6aba3f34f2bb914f9ec478abe99688c86386fe904396495/_data",
                "Destination": "/opt/couchdb/data",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ]" de la réponse affiché sur le shell montre que le volume 4e49b00439a8a2cba6aba3f34f2bb914f9ec478abe99688c86386fe904396495 est celui utilisé par couchdb.
4. Mount the identified volume to busybox 
	docker run -it --name busybox-test --mount src=4e49b00439a8a2cba6aba3f34f2bb914f9ec478abe99688c86386fe904396495,target=/opt/couchdb/data busybox
5. Check files inside `/opt/couchdb/data`
	cd /opt/couchdb/data
	Ce répertoire contient 2 fichiers .couch que sont : _dbs.couch    _nodes.couch
6. Stop couchdb
	docker stop couchdb
7. Delete the volume
	"docker stop busybox-test" pour s'assurer que plus aucun conteneur n'utilise ce volume.
	Cela ne suffit pas on va donc supprimer les conteneurs qui utilisent ce volume au lieu de les stopper : 
	"docker rm fbd834ce1c2cfffb11d05b4c5d27bb2824757ae60a738cdf7e93a30e01bc1b7b"
	"docker rm 7649389f3edbbb60a70a3a007f0f6e30417bc548067dda3e0a43af1a49d6ecfa"
	"docker volume rm 4e49b00439a8a2cba6aba3f34f2bb914f9ec478abe99688c86386fe904396495" pour supprimer le volume
8. Check that the volume has been deleted
	docker volume ls

### Create a named volume

1. Create a volume named : `couchdb_vol`
	"docker volume create couchdb_vol" pour créer le volume
	"docker volume ls" pour vérifier qu'il est bien créé
2. Run `couchedb` with the created volume
	docker run -d --name couchdb \
  -p 5984:5984 \
  -v couchdb_vol:/opt/couchdb/data \
  -e COUCHDB_USER=admin \
  -e COUCHDB_PASSWORD=password \
  couchdb

3. Inspect the container and look at `Mounts` that `couchdb_vol` is used
	"docker container inspect couchdb" et on a bien 
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

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container 
	docker run -it --name busybox-test -v /var/lib/docker:/dck busybox
2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available 
	Oui, les deux fichiers _dbs.couch    _nodes.couch qui étaient dans couchdb_vol y sont.


### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`
2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached
   docker run -d --name gen_date -v $(pwd)/sidecar:/dck busybox sh -c 'while true; do date >> /dck/date.log; sleep 1; done'
3. Check the content of `sidecar/date.log` with `cat`
		Ca m'affiche les timestamps qui sont dans le log file.
4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached
   docker run -it --name watch_log -v $(pwd)/sidecar:/dck2 busybox 
5. Check content of `dck2/date.log` with `tail -f`
	Ca affiche les timestamp en temps réel (un à un).
6. Exit container
	"CTRL C" pour quitter la commande tail ensuite exit pour quitter le terminal du conteneur.
7. Run `docker kill gen_date`
   1. Why is the container stoped ?
   		La commande kill est faite pour forcer l'arrêt du conteneur.


### In memory 

1. Run busybox with `--tmpfs /test`
	docker run -it --rm --name tmpfs-test --tmpfs /test busybox
2. Check with `mount | grep test` that tmpfs is used  
	tmpfs on /test type tmpfs (rw,nosuid,nodev,noexec,relatime) ====> le répertoire /test est mounté comme un fichier tmpfs 


