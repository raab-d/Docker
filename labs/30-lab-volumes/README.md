# Lab 4 - Volumes

## Use volumes

### Tips

- Use `docker container inspect ...`

### Existing volumes

1. run `docker container run --name couchdb -d -p 5984:5984 couchdb:2.1`
```bash
   Unable to find image 'couchdb:2.1' locally
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
   3a1b6afbe703f42cce855d7c88cd16dae377a273c0ebcd4ec67b07ce290792b4
```
2. Check existing volumes
   ```bash
      docker volume ls
   ```
   1. Why there is already a volume ?
   ```bash
      La commande précédente en crée un par défaut.
   ```
3. Identify the volume that is used by `couchdb`
   ```bash
      docker container inspect --format "{{json .Mounts}}" couchdb
      -> [{"Type":"volume","Name":"4594a7527c511de3db51b009e1d33077778e70925ae28fce9c1fd55aa94b1263","Source":"/var/lib/docker/volumes/4594a7527c511de3db51b009e1d33077778e70925ae28fce9c1fd55aa94b1263/_data","Destination":"/opt/couchdb/data","Driver":"local","Mode":"","RW":true,"Propagation":""}]
   ```
4. Mount the identified volume to busybox
```bash
   docker container run --rm --name busybox_couchdb_mounted --volumes-from=couchdb busybox
   ou
   docker container run --name busybox_couchdb_mounted --mount source=5d662fafce1071fe045c211c30faf3b42b552db6f55886e4f69971ab31714751,target=/opt/couchdb/data,type=volume busybox
```
5. Check files inside `/opt/couchdb/data`
```bash
   ls /opt/couchdb/data
   -> _dbs.couch         _nodes.couch       _replicator.couch  _users.couch
```
6. Stop couchdb
```bash
   docker stop couchdb
```
7. Delete the volume
```bash
   docker volume rm 5d662fafce1071fe045c211c30faf3b42b552db6f55886e4f69971ab31714751
```
8. Check that the volume has been deleted
```bash
   docker volume ls | grep "5d662fafce1071fe045c211c30faf3b42b552db6f55886e4f69971ab31714751"
   -> None
```

### Create a named volume

1. Create a volume named : `couchdb_vol`
```bash
   docker volume create couchdb_vol
```
2. Run `couchedb` with the created volume
```bash
   docker container run --name couchdb1 -d -p 5984:5984 -v couchdb_vol:/opt/couchdb/data couchdb:2.1
```
3. Inspect the container and look at `Mounts` that `couchdb_vol` is used
```bash
   docker container inspect --format "{{json .Mounts}}" couchdb1                                                        1 ↵
   -> [{"Type":"volume","Name":"couchdb_vol","Source":"/var/lib/docker/volumes/couchdb_vol/_data","Destination":"/opt/couchdb/data","Driver":"local","Mode":"z","RW":true,"Propagation":""}]
```

### Mount directory

1. Mount `/var/lib/docker` from host to `/dck` into a busybox container
```bash
   docker container run --name busybox_couchdb_mounted -v /var/lib/docker:/dck busybox
```
2. Check at `ls /dck/volumes/couchdb_vol/_data` inside the container to verify that `couchdb_vol` is available
```bash
docker exec 72188f5957a4 ls /dck/volumes/couchdb_vol
-> _data                                             
_dbs.couch
_nodes.couch
_replicator.couch
_users.couch
```

### SideCar Pattern

1. Create a directory named `sidecar` with `mkdir`
```bash
   mkdir /var/lib/docker/sidecar
```
2. Run Busybox
   1. Command: `sh -c 'while true; do date >> /dck/date.log; sleep 1; done'`
   2. Volume to mount: `$(pwd)/sidecar:/dck`
   3. Name: `gen_date`
   4. State: detached
```bash
   docker container run -d --name gen_date --mount source=/var/lib/docker/sidecar,target=/dck,type=bind busybox sh -c 'while true; do date >> /dck/date.log; sleep 1; done'
```
3. Check the content of `sidecar/date.log` with `cat`
```bash
   docker exec 8e260264540a cat /dck/date.log        
Wed Apr 10 14:55:13 UTC 2024
Wed Apr 10 14:55:14 UTC 2024
Wed Apr 10 14:55:15 UTC 2024
Wed Apr 10 14:55:16 UTC 2024
Wed Apr 10 14:55:17 UTC 2024
Wed Apr 10 14:55:18 UTC 2024
Wed Apr 10 14:55:19 UTC 2024
Wed Apr 10 14:55:20 UTC 2024
Wed Apr 10 14:55:21 UTC 2024
Wed Apr 10 14:55:22 UTC 2024
Wed Apr 10 14:55:23 UTC 2024
Wed Apr 10 14:55:24 UTC 2024
Wed Apr 10 14:55:25 UTC 2024
Wed Apr 10 14:55:26 UTC 2024
Wed Apr 10 14:55:27 UTC 2024
```
4. Run Busybox
   1. Command: `tail -f /dck2/date.log`
   2. Volume to mount: `$(pwd)/sidecar:/dck2`
   3. State: attached
```bash
   docker container run --name gen_date_2 --mount source=/var/lib/docker/sidecar,target=/dck2,type=bind busybox sh -c 'tail -f /dck2/date.log'
Wed Apr 10 14:59:40 UTC 2024
Wed Apr 10 14:59:41 UTC 2024
Wed Apr 10 14:59:42 UTC 2024
Wed Apr 10 14:59:43 UTC 2024
Wed Apr 10 14:59:44 UTC 2024
Wed Apr 10 14:59:45 UTC 2024
Wed Apr 10 14:59:46 UTC 2024
Wed Apr 10 14:59:47 UTC 2024
Wed Apr 10 14:59:48 UTC 2024
Wed Apr 10 14:59:49 UTC 2024
Wed Apr 10 14:59:50 UTC 2024
Wed Apr 10 14:59:51 UTC 2024
```
5. Check content of `dck2/date.log` with `tail -f` : Voir au dessus.
6. Exit container : CRTL + D
7. Run `docker kill gen_date`
   1. Why is the container stoped ? Car on vient de le kill.

### In memory 

1. Run busybox with `--tmpfs /test`
```bash
docker container run --name gen_date_2 --tmpfs /test busybox
```
2. Check with `mount | grep test` that tmpfs is used 
```bash
   docker container run --name test --tmpfs /test busybox mount | grep test
   -> tmpfs on /test type tmpfs (rw,nosuid,nodev,noexec,relatime,inode64)
```
