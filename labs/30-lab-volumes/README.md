# Lab 3 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
   # docker container inspect couchdb

2. Check existing volumes
   # docker container inspect couchdb
   1. Why there is already a volume ?
   # There's already a volume because the couchdb Docker image defines a volume at /opt/couchdb/data in its Dockerfile. This is where CouchDB stores its data.
3. Identify the volume that is used by `couchdb`
   # In mounts, the name of the volume is "2c614cb1d0a4bb28a2e6c6a3fb4fc6050f650d263b888595ca0865d21dbc4410"
4. Mount the identified volume to busybox 
   # docker run -it --rm --volumes-from couchdb busybox
5. Check files inside `/opt/couchdb/data`
   # ls /opt/couchdb/data
   # I can see those files: dbs.couch         _nodes.couch       _replicator.couch  _users.couch
6. Stop couchdb
   # exit
   # docker stop couchdb
7. Delete the volume
   # I first had an error because the container using the volume was stopped but not removed.
   # docker rm couchdb
   # docker volume rm 2c614cb1d0a4bb28a2e6c6a3fb4fc6050f650d263b888595ca0865d21dbc4410
8. Check that the volume has been deleted
   # docker volume ls
   # the volume has effectively been deleted

### Create a named volume

1. Create a volume named : `couchdb_vol`
   # docker volume create couchdb_vol
2. Run `couchedb` with the created volume
   # docker run -d -p 5984:5984 --name couchdb2 -v couchdb_vol:/opt/couchdb/data couchdb:2.1
3. Inspect the container and look at `Mounts` that `couchdb_vol` is used
   # docker container inspect couchdb2
   # couchdb_vol is used

### Mount directory

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container 
   # docker run -it --rm -v /var/lib/docker:/dck busybox
2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available
   # I write "ls /dck/volumes/couchdb_vol/_data" inside the busyboxexit
   # I can see the following files _dbs.couch         _nodes.couch       _replicator.couch  _users.couch


### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`
   # mkdir sidecar
2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached
   # docker run -d --name gen_date -v $(pwd)/sidecar:/dck busybox sh -c 'while true; do date >> /dck/date.log; sleep 1; done'
3. Check the content of `sidecar/date.log` with `cat`
   # cat sidecar/date.log
4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached
   # docker run -it --rm -v $(pwd)/sidecar:/dck2 busybox tail -f /dck2/date.log
5. Check content of `dck2/date.log` with `tail -f`
   #  It's being continuously updated.
6. Exit container
   # I used ctrl+c to exit
7. Run `docker kill gen_date`
   # docker kill gen_date
   1. Why is the container stoped ?
   # The container stopped because the docker kill command forces it to stop immediately.

### In memory 

1. Run busybox with `--tmpfs /test`
   # docker run -it --rm --tmpfs /test busybox
2. Check with `mount | grep test` that tmpfs is used 
   # mount | grep test
   # tmpfs on /test type tmpfs (rw,nosuid,nodev,noexec,relatime)

