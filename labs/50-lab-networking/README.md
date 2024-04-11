# Lab 3 - Network

## Expose port

### Tips

- Port must be higher than 1024

### Expose port

1. Pull `couchdb:2.1`
   # docker pull couchdb:2.1
2. Run couchdb, name it `couchedb1` and expose the port `5984` (detached)
   # docker run -d -p 5984:5984 --name couchdb1 couchdb:2.1
3. Check the couchedb version on `http://localhost:5984`
   # "version": "2.1.2"
4. Run temporary busybox container
   # docker run -it --rm busybox
5. Call `localhost:5984` with `wget` from busybox container
   # wget localhost:5984
   1. What happened ?
   # I received an error: wget: can't connect to remote host (127.0.0.1): Connection refused.
   2. Why ?
   # This is because localhost in the busybox container refers to the container itself, not the host where couchdb1 is running.
6. Call `couchdb1:5984` with `wget` from busybox container
   # wget couchdb1:5984
   1. What happened ?
   # I received an error: wget: bad address 'couchdb1:5984'
   2. Why ?
   # This is because couchdb1 is not known to the busybox container. They are in isolated networks.
7. Create a new network named `busyboxtocouchdb`
   # docker network create busyboxtocouchdb
8. Connect `couchdb1` to the network with `docker network connect ...`
   # docker network connect busyboxtocouchdb couchdb1
9. Re-run busybox connected to the same network
   # docker run -it --rm --network busyboxtocouchdb busybox
10. Call `couchdb1:5984` with `wget` from busybox container
   # wget couchdb1:5984
   # now it worked