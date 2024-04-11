# Lab 3 - Network

## Expose port

### Tips

- Port must be higher than 1024

### Expose port

1. Pull `couchdb:2.1`
<br> docker pull couchdb:2.1

2. Run couchdb, name it `couchedb1` and expose the port `5984` (detached)
<br>docker run -d --name couchdb1 -p 5984:5984 couchdb:2.1

3. Check the couchedb version on `http://localhost:5984`
<br>{
  "couchdb": "Welcome",
  "version": "2.1.2",
  "features": [
    "scheduler"
  ],
  "vendor": {
    "name": "The Apache Software Foundation"
  }
}
4. Run temporary busybox container
<br>docker run --rm -it busybox

5. Call `localhost:5984` with `wget` from busybox container
<br>wget localhost:5984

   1. What happened ?
   <br> It failed
   2. Why ?
   <br> localhost inside the container refers to the container itself, not the host machine.
6. Call `couchdb1:5984` with `wget` from busybox container
<br>wget couchdb1:5984
   1. What happened ?
   <br>does not resolve to an IP address that the BusyBox container can access.
   2. Why ?
   <br>Docker containers can only communicate by IP addresses unless they are connected to the same user-defined network
7. Create a new network named `busyboxtocouchdb`
<br>docker network create busyboxtocouchdb

8. Connect `couchdb1` to the network with `docker network connect ...`
<br>docker network connect busyboxtocouchdb couchdb1

9. Re-run busybox connected to the same network
<br>docker run --rm -it --network busyboxtocouchdb busybox

10. Call `couchdb1:5984` with `wget` from busybox container
<br>wget couchdb1:5984
<br> / # wget couchdb1:5984
Connecting to couchdb1:5984 (172.18.0.2:5984)
saving to 'index.html'
index.html           100% |****************************************************************|   116  0:00:00 ETA
'index.html' saved

