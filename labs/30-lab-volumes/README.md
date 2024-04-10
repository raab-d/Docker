# Lab 3 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
2. Check existing volumes
   ```bash
   docker volume ls
   ```
   1. Why there is already a volume ?
      There's already a volume because the CouchDB image is designed to store its data in a volume beyond the life of the container
3. Identify the volume that is used by `couchdb`
   ```bash
   docker container inspect couchdb
   ```
   Output: f8473fa8c7f11ecab39ee572942cd46a34def05af3fde9e5c89cd0c68f02a9d5
4. Mount the identified volume to busybox
   ```bash
   docker run -it --rm --volumes-from couchdb busybox
   ```
5. Check files inside `/opt/couchdb/data`
   ```bash
   ls /opt/couchdb/data
   ```
   Output:
   ```bash
   _dbs.couch         _nodes.couch       _replicator.couch  _users.couch
   ```
6. Stop couchdb
   ```bash
   docker stop couchdb
   ```
7. Delete the volume
   ```bash
   docker rm couchdb
   docker volume rm f8473fa8c7f11ecab39ee572942cd46a34def05af3fde9e5c89cd0c68f02a9d5
   ```
8. Check that the volume has been deleted
   ```
   docker volume ls
   ```
   Output:
   ```bash
   DRIVER    VOLUME NAME
   ```
   Already created the named volume of the next part

### Create a named volume

1. Create a volume named : `couchdb_vol`
   ```bash
   docker volume create couchdb_vol
   ```
2. Run `couchedb` with the created volume
   ```bash
   docker run --name couchdb -d -p 5984:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1
   ```
3. Inspect the container and look at `Mounts` that `couchdb_vol` is used
   ```bash
   docker container inspect couchdb
   ```

### Mount directory

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container
   ```bash
   docker run -it --rm -v /var/lib/docker:/dck busybox
   ```
2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available
   ```bash
   docker run -it --rm -v /var/lib/docker:/dck busybox
   ```

### SideCar Pattern

1.  Create a directory named `sidecar` with `mkdir`
   ```bash 
   mkdir sidecar
   ```
2.  Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached
   ```
   docker run -d --name gen_date -v $(pwd)/sidecar:/dck busybox sh -c 'while true; do date >> /dck/date.log; sleep 1; done'
   ```
3.  Check the content of `sidecar/date.log` with `cat`<br>
   ```cat sidecar/date.log```
4.  Run Busybox
    1. Command:  `tail -f /dck2/date.log`
    2.  Volume to mount: `$(pwd)/sidecar:/dck2`
    3.  State: attached<br>
      ```bash 
      docker run -it --rm -v $(pwd)/sidecar:/dck2 busybox tail -f /dck2/date.log
      ```
5.  Check content of `dck2/date.log` with `tail -f`
   ```
   It's being continuously updated.
   ```
6.  Exit container
   ```
   I used ctrl+c to exit
   ```
7.  Run `docker kill gen_date`
   1. Why is the container stoped ?
      ```
      The docker kill command sends a SIGKILL signal to the specified container, forcing it to stop.
      ```

### In memory

1. Run busybox with `--tmpfs /test`
   ```bash
   docker run -it --rm --tmpfs /test busybox
   ```
2. Check with `mount | grep test` that tmpfs is used
   ```bash
   mount | grep test
   tmpfs on /test type tmpfs (rw,nosuid,nodev,noexec,relatime)
   ```
