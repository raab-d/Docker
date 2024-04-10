# Lab 3 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
2. Check existing volumes<br>
Command: docker volume ls
   1. Why there is already a volume ?<br>
   There's already a volume because the CouchDB image is designed to store its data in a volume beyond the life of the container
3. Identify the volume that is used by `couchdb`<br>
Command: docker container inspect couchdb<br>
Then we look at the mounts part: 
![alt text](image.png)
4. Mount the identified volume to busybox<br>
Command: docker run -it --rm --volumes-from couchdb busybox
5. Check files inside `/opt/couchdb/data`<br>
Command : ls /opt/couchdb/data
![alt text](image-1.png)
6. Stop couchdb<br>
Command: docker stop couchdb
7. Delete the volume<br>
Command: docker volume rm 57be773b8e90a92ca35e0c5d0ce468f301eeb36df1f8cb2bae6d6d16b3ea63dc
8. Check that the volume has been deleted<br><br>
![alt text](image-2.png)<br>
Already created the named volume of the next part

### Create a named volume

1. Create a volume named : `couchdb_vol`<br>
Command: docker volume create couchdb_vol
2. Run `couchedb` with the created volume<br>
Command: docker run --name couchdb -d -p 5984:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1
3. Inspect the container and look at `Mounts` that `couchdb_vol` is used<br>
Command: docker container inspect couchdb<br>
![alt text](image-4.png)

### Mount directory

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container <br>
Command: docker run -it --rm -v /var/lib/docker:/dck busybox
2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available<br>
docker run -it --rm -v /var/lib/docker:/dck busybox<br>
![alt text](image-5.png)

### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`<br>
Command: mkdir sidecar
2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached<br>
Command: docker run -d --name gen_date -v C:\Users\Thoma\sidecar:/dck  busybox sh 'while true; do date >> /dck/date.log; sleep 1; done' 
3. Check the content of `sidecar/date.log` with `cat`<br>
No date log to show, i had issues with the dck path in Windows.
4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached<br>
   Command: docker run -it --rm -v C:\Users\Thoma\sidecar:/dck2 busybox tail -f /dck2/date.log
5. Check content of `dck2/date.log` with `tail -f`
   #  It's being continuously updated.
6. Exit container
   # I used ctrl+c to exit
7. Run `docker kill gen_date`
   1. Why is the container stoped ?<br>
   The docker kill command sends a SIGKILL signal to the specified container, forcing it to stop.

### In memory 

1. Run busybox with `--tmpfs /test`<br>
docker run -it --rm --tmpfs /test busybox
2. Check with `mount | grep test` that tmpfs is used 
   # mount | grep test
   # tmpfs on /test type tmpfs (rw,nosuid,nodev,noexec,relatime)

