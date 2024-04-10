# Lab 4 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
2. Check existing volumes
<br> docker volume ls

   1. Why there is already a volume ?
   <br> CouchDB Docker image is designed to store data persistently. The image's Dockerfile specifies a volume for this purpose. 
   <br> This volume is automatically created when the container starts to ensure that CouchDB data persists.
3. Identify the volume that is used by `couchdb`
<br> docker container inspect couchdb
4. Mount the identified volume to busybox 
<br> docker run -it --rm --volumes-from couchdb busybox
5. Check files inside `/opt/couchdb/data`
<br> ls
<br> _dbs.couch         _nodes.couch       _replicator.couch  _users.couch

6. Stop couchdb
<br> docker stop couchdb
7. Delete the volume
<br> docker stop 8dd86dc7f146
<br> docker rm 8dd86dc7f146
<br> docker volume rm 38fc9ee36d96372d1e4db0bdd41e7413bc690b8cb1db373ef1f36f6be81e14b9

8. Check that the volume has been deleted
<br>  docker volume ls

### Create a named volume

1. Create a volume named : `couchdb_vol`
<br> docker volume create couchdb_vol

2. Run `couchedb` with the created volume
<br> docker run --name couchdb2 -d -p 5985:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1

3. Inspect the container and look at `Mounts` that `couchdb_vol` is used
<br> docker container inspect couchdb2
<br>         "Mounts": [
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
<br> docker run -it --rm -v /var/lib/docker:/dck busybox

2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available
<br> ls /dck/volumes/couchdb_vol/_data 
<br> it just works

### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`
<br> `mkdir sidecar`
2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done``'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached
<br> docker run -d --name gen_date -v $(pwd)/sidecar:/dck busybox sh -c 'while true; do date >> /dck/date.log; sleep 1; done'
   
3. Check the content of `sidecar/date.log` with `cat`
<br> cat sidecar/date.log

4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached
<br> docker run -it --rm -v $(pwd)/sidecar:/dck2 busybox tail -f /dck2/date.log

5. Check content of `dck2/date.log` with `tail -f`
<br> cat sidecar/date.log
6. Exit container
ctrl p + ctrl q

7. Run `docker kill gen_date`
   1. Why is the container stoped ?
   <br> The docker kill command sends a SIGKILL signal to the container, immediately terminating it.

### In memory 

1. Run busybox with `--tmpfs /test`
<br> docker run -it --rm --tmpfs /test busybox

2. Check with `mount | grep test` that tmpfs is used 
<br> mount | grep test
<br> tmpfs on /test type tmpfs (rw,nosuid,nodev,noexec,relatime)
 

