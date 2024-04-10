# Lab 4 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1` <br>
2. Check existing volumes
   1. Why there is already a volume ? <br>
   docker volume ls <br>
   DRIVER    VOLUME NAME <br>
   local     a240e82cb8dd374125434aa521c93d02d670675f82a057bd41476297dac5b11d <br>
   The persistent data needs a volume in order to be stocked. This is automatically created. <br>
3. Identify the volume that is used by `couchdb`
   docker volume inspect a240e82cb8dd374125434aa521c93d02d670675f82a057bd41476297dac5b11d
4. Mount the identified volume to busybox <br>
   docker run -it --rm --mount source=a240e82cb8dd374125434aa521c93d02d670675f82a057bd41476297dac5b11d,target=/data busybox
5. Check files inside `/opt/couchdb/data` <br>
   / # ls /data <br>
   _dbs.couch         _nodes.couch       _replicator.couch  _users.couch <br>
6. Stop couchdb <br>
   exit <br>
   docker container stop couchdb <br>
7. Delete the volume <br>
   docker rm couchdb <br>
   docker volume rm a240e82cb8dd374125434aa521c93d02d670675f82a057bd41476297dac5b11d
8. Check that the volume has been deleted <br>
   docker volume ls

### Create a named volume

1. Create a volume named : `couchdb_vol` <br>
   docker volume create couchdb_vol
2. Run `couchedb` with the created volume <br>
   docker run -v couchedb_vol:/opt/couchdb/data couchdb
3. Inspect the container and look at `Mounts` that `couchdb_vol` is used <br>
      docker inspect couchdb

### Mount directory

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container <br>
   docker run -it --rm -v /var/lib/docker:/dck busybox
2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available <br>
   ls /dck/volumes/ -> <br>
   42811f52d4f1675440317d78ff224b2d67118e8c01416378bd7b22b5df41177a <br>
   backingFsBlockDev <br>
   couchedb_vol <br>
   e3fa93e4dceb19cacf943f8cf75aa631110a0a3afe84b65a51776ad5ceda396b <br>   

### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir` <br>
   sidecar directory created on premise.
2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached <br>
   docker run -d --name gen_date -v ${pwd}/sidecar:/dck busybox sh -c 'while true; do date >> /dck/date.log; sleep 1; done'
3. Check the content of `sidecar/date.log` with `cat` <br>
   Wed Apr 10 13:36:10 UTC 2024 <br>
   Wed Apr 10 13:36:11 UTC 2024 <br>
   Wed Apr 10 13:36:12 UTC 2024
4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached
   docker run -it -v ${pwd}/sidecar:/dck2 busybox sh -c 'tail -f /dck2/date.log'
5. Check content of `dck2/date.log` with `tail -f`
   Wed Apr 10 13:50:37 UTC 2024 <br>
   Wed Apr 10 13:50:38 UTC 2024 <br>
6. Exit container
7. Run `docker kill gen_date`
   1. Why is the container stoped ? <br>
   It actually killed the process, not the busybox. It has no time to end properly.

### In memory 

1. Run busybox with `--tmpfs /test` <br>
   docker run -it --rm --tmpfs /test busybox
2. Check with `mount | grep test` that tmpfs is used <br>
   tmpfs on /test type tmpfs (rw,nosuid,nodev,noexec,relatime)
