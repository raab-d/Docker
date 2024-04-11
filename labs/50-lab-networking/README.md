# Lab 3 - Network

## Expose port

### Tips

- Port must be higher than 1024

### Expose port

1. Pull `couchdb:2.1`
- docker pull couchdb:2.1

2. Run couchdb, name it `couchedb1` and expose the port `5984` (detached)
- docker run -d --name couchdb1 -p 5984:5984 couchdb:2.1

3. Check the couchedb version on `http://localhost:5984`
- curl http://localhost:5984

4. Run temporary busybox container
- docker run --rm -it busybox

5. Call `localhost:5984` with `wget` from busybox container
- wget http://localhost:5984
   1. What happened ?
   - Connexion echouée
   2. Why ?
   - localhost fait référence au conteneur Busybox lui-même et non à l'hôte ou au conteneur CouchDB.

6. Call `couchdb1:5984` with `wget` from busybox container
   1. What happened ?
   - Echec aussi
   2. Why ?
   - Les conteneurs ne sont pas conscients des noms des autres conteneurs sans un réseau Docker personnalisé

7. Create a new network named `busyboxtocouchdb`
- docker network create busyboxtocouchdb

8. Connect `couchdb1` to the network with `docker network connect ...`
- docker network connect busyboxtocouchdb couchedb1

9. Re-run busybox connected to the same network
- docker run --rm -it --network=busyboxtocouchdb busybox

10. Call `couchdb1:5984` with `wget` from busybox container
- wget http://couchedb1:5984
