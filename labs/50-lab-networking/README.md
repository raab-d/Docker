# Lab 3 - Network

## Expose port

### Tips

- Port must be higher than 1024

### Expose port

1. Pull `couchdb:2.1`
docker pull couchdb:2.1
2. Run couchdb, name it `couchedb1` and expose the port `5984` (detached)
docker run -d --name couchdb1 -p 5984:5984 couchdb:2.1
3. Check the couchedb version on `http://localhost:5984`
![alt text](image.png)
4. Run temporary busybox container
docker run -it --rm busybox
5. Call `localhost:5984` with `wget` from busybox container
   1. What happened ?
   / # wget localhost:5984
Connecting to localhost:5984 (127.0.0.1:5984)
wget: can't connect to remote host (127.0.0.1): Connection refused
   2. Why ?
   because busybox is in private network
6. Call `couchdb1:5984` with `wget` from busybox container
   1. What happened ?
   wget: bad address 'couchdb:5984'
   2. Why ?
   docker try to find couchdb1 name but it not available in the busybox's network
7. Create a new network named `busyboxtocouchdb`
   docker network create busyboxtocouchdb
8. Connect `couchdb1` to the network with `docker network connect ...`
docker network connect busyboxtocouchdb couchdb1
9. Re-run busybox connected to the same network
10. Call `couchdb1:5984` with `wget` from busybox container
it work now