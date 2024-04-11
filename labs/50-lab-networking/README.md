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
4. Run temporary busybox container
5. Call `localhost:5984` with `wget` from busybox container
docker run --rm busybox wget -O - http://localhost:5984
   1. What happened ?
   wget: can't connect to remote host (127.0.0.1): Connection refused
   2. Why ?
   Parce que dans le contexte d'un conteneur Docker, localhost fait référence au conteneur lui-même et non à l'hôte. Donc, quand nous exécutons wget vers localhost depuis le conteneur busybox, il essaie de se connecter à lui-même et non au service CouchDB s'exécutant sur l'hôte.
6. Call `couchdb1:5984` with `wget` from busybox container
   1. What happened ? 
   cela a échoué 
   2. Why ?
   car les conteneurs Docker ne peuvent pas se résoudre par leurs noms par défaut.
7. Create a new network named `busyboxtocouchdb`
docker network create busyboxtocouchdb

8. Connect `couchdb1` to the network with `docker network connect ...`
docker network connect busyboxtocouchdb couchdb1
docker run --rm --network busyboxtocouchdb busybox wget -O - http://couchdb1:5984
9. Re-run busybox connected to the same network
docker run -it --rm --network busyboxtocouchdb busybox

10. Call `couchdb1:5984` with `wget` from busybox container
wget couchdb1:5984
Connecting to couchdb1:5984 (172.19.0.2:5984)
saving to 'index.html'
index.html           100% |**************************************************************************|   116  0:00:00 ETA 
'index.html' saved