# Lab 4 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
2. Check existing volumes
	$docker volume ls
   1. Why there is already a volume ?
	$Docker créer un volume automatiquement
3. Identify the volume that is used by `couchdb`
	$docker inspect -f '{{ .Mounts }}' couchdb
4. Mount the identified volume to busybox
	$docker run -it --rm -v 34047ec88f7e897e70a3a569c644af942948fea4176a62a27124fad70bc05d66:/mnt busybox 
5. Check files inside `/opt/couchdb/data`
	$ls/mnt
6. Stop couchdb
	$docker stop couchdb
7. Delete the volume
	- On supprimme d'abord les dépendances
	$docker volume rm 34047ec88f7e897e70a3a569c644af942948fea4176a62a27124fad70bc05d66
8. Check that the volume has been deleted

### Create a named volume

1. Create a volume named : `couchdb_vol`
	$docker volume create couchdb_vol
2. Run `couchedb` with the created volume
	$docker run -d --name couchdb -p 5984:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1
3. Inspect the container and look at `Mounts` that `couchdb_vol` is used

### Mount directory

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container
	$docker run -it --rm -v /var/lib/docker:/dck busybox
2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available

### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`
2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached
	$docker run -d --name gen_date -v $(pwd)/sidecar:/dck busybox sh -c "while true; do date >> /dck/date.log; sleep1; done"
3. Check the content of `sidecar/date.log` with `cat`
	$cat sidecar/date.log 
4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached
	$docker run -it -v $(pwd)/sidecar:/dck2 busybox tail -f /dck2/date.log
5. Check content of `dck2/date.log` with `tail -f`
6. Exit container
7. Run `docker kill gen_date`
	$docker kill gen_date
   1. Why is the container stoped ?

	$La commande kill force le process "tail" à se stopper ce qui cause la stoppage du container 
### In memory 

1. Run busybox with `--tmpfs /test`
	$docker run -it --tmpfs /test busybox
2. Check with `mount | grep test` that tmpfs is used 
	$mount | grep test

