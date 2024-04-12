# Lab 3 - Network

## Expose port

### Tips

- Port must be higher than 1024

### Expose port

1. Pull `couchdb:2.1`
```bash
docker pull couchdb:2.1
```
2. Run couchdb, name it `couchedb1` and expose the port `5984` (detached)
```bash
docker run -it --name couchedb1 -p 0.0.0.0:5984:5984 couchdb:2.1
```
3. Check the couchedb version on `http://localhost:5984`
```json
{"couchdb":"Welcome","version":"2.1.2","features":["scheduler"],"vendor":{"name":"The Apache Software Foundation"}}
```
4. Run temporary busybox container
5. Call `localhost:5984` with `wget` from busybox container
   1. What happened ? Connecting to localhost:5984 (127.0.0.1:5984) wget: can't connect to remote host (127.0.0.1): Connection refused
   2. Why ? parce que le conteneur n'est pas autorisé à accéder au réseau de l'hôte
6. Call `couchdb1:5984` with `wget` from busybox container
   1. What happened ? wget: bad address 'couchdb1:5984'
   2. Why ? parce que les 2 conteneurs ne sont pas sur le même network
7. Create a new network named `busyboxtocouchdb`
```bash
docker network create busyboxtocouchdb
```
8. Connect `couchdb1` to the network with `docker network connect ...`
```bash
docker network connect busyboxtocouchdb couchdb1
```
9. Re-run busybox connected to the same network
```bash
docker run -it --rm --network=busyboxtocouchdb busybox
```
10. Call `couchdb1:5984` with `wget` from busybox container
```bash
wget couchdb1:5984
Connecting to couchdb1:5984 (172.18.0.2:5984)
saving to 'index.html'
index.html           100% |**|   116  0:00:00 ETA
'index.html' saved
```
