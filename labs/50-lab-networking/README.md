# Lab 3 - Network

## Expose port

### Tips

- Port must be higher than 1024

### Expose port

1. Pull `couchdb:2.1`
===> docker pull couchdb:2.1

2. Run couchdb, name it `couchedb1` and expose the port `5984` (detached)
==> docker run -d --name couchdb1 -p 5984:5984 couchdb:2.1
j'ai eu ce retour : 5cbcc6e29eedc74f0a5a8a4c9d5a4071714793807d440f2d15ae474f32f8a82c

3. Check the couchedb version on `http://localhost:5984`
==> curl http://localhost:5984
j'ai eu ce retour :  {"couchdb":"Welcome","version":"2.1.2","features":["scheduler"],"vendor":{"name":"The Apache Software Foundation"}}

4. Run temporary busybox container
==>  docker run --rm -it busybox

5. Call `localhost:5984` with `wget` from busybox container 
==> / # wget http://localhost:5984
   
   1. What happened ?
   Je ne pouvais pas me connecter 
   j'ai eu ce retour :
   Connecting to localhost:5984 (127.0.0.1:5984)
   wget: can't connect to remote host (127.0.0.1): Connection refused
   
   2. Why ?
   Cela se produit parce que localhost dans le contexte du conteneur BusyBox pointe vers le conteneur lui-même, et non vers l'hôte où CouchDB est en cours d'exécution. Chaque conteneur a son propre localhost. Ainsi, essayer d'accéder à CouchDB en utilisant localhost depuis le conteneur BusyBox ne fonctionnera pas, car CouchDB n'est pas en cours d'exécution dans ce conteneur mais plutôt dans un autre.

6. Call `couchdb1:5984` with `wget` from busybox container
==> / # wget http://localhost:5984

   1. What happened ?
   j'ai eu ce retour 
   wget: bad address 'couchdb1:5984'

   2. Why ?
   Cela se produit parce que par défaut, les conteneurs Docker ne sont pas conscients des autres conteneurs par leurs noms, à moins qu'ils ne soient explicitement liés ou qu'ils fassent partie du même réseau Docker personnalisé. Si on exécute simplement un conteneur BusyBox sans le connecter au même réseau que couchdb1 e système de noms de domaine (DNS) interne de Docker ne sera pas capable de résoudre couchdb1 en l'adresse IP appropriée.

7. Create a new network named `busyboxtocouchdb`
==> docker network create busyboxtocouchdb
j'ai eu ce retour : d0ea8aeef67f4ce4d92deee1be2844613a4b5a1f98898a425fe0b3d47baab3bc

8. Connect `couchdb1` to the network with `docker network connect ...`
==> docker network connect busyboxtocouchdb couchdb1

9. Re-run busybox connected to the same network
==> docker run --rm -it --network=busyboxtocouchdb busybox

10. Call `couchdb1:5984` with `wget` from busybox container
==> / # wget http://couchdb1:5984
j'ai eu le retour suivant :
Connecting to couchdb1:5984 (172.19.0.2:5984)
saving to 'index.html'
index.html  100% |**********************************************************************************************************************************|   116  0:00:00 ETA
'index.html' saved

commentaire : La réussite indique une communication fluide entre conteneurs sur un réseau Docker, 
confirmant la configuration réseau correcte et l'accès inter-conteneurs.
