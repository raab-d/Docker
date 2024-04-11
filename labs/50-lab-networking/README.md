# Lab 3 - Network

## Expose port

### Tips

- Port must be higher than 1024

### Expose port

1. Pull `couchdb:2.1`
	"docker pull --platform linux/arm64/v8 couchdb:latest" pour indiquer à Docker de chercher et de télécharger la version de l'image qui est compatible avec l'architecture ARM64 v8

2. Run couchdb, name it `couchedb1` and expose the port `5984` (detached)
	Puis on lance cette commande : "docker run -d --name couchdb1 \
	  -p 5984:5984 \
	  -e COUCHDB_USER=admin \
	  -e COUCHDB_PASSWORD=password \
	  couchdb "

3. Check the couchedb version on `http://localhost:5984`
{"couchdb":"Welcome","version":"3.3.3","git_sha":"40afbcfc7","uuid":"a7b7e8e6a53690f251f50255a3275a77","features":["access-ready","partitioned","pluggable-storage-engines","reshard","scheduler"],"vendor":{"name":"The Apache Software Foundation"}}

Pulled the last version becauser version 2.1 is not compatible with ARM64.

4. Run temporary busybox container
	docker run --rm -it busybox

5. Call `localhost:5984` with `wget` from busybox container
   1. What happened ?
   	Connecting to localhost:5984 (127.0.0.1:5984)
	wget: can't connect to remote host (127.0.0.1): Connection refused
   2. Why ?
   	Cela se produit parce que localhost dans le contexte du conteneur BusyBox pointe vers le conteneur lui-même, et non vers l'hôte où CouchDB est en cours d'exécution. Chaque conteneur a son propre localhost. Ainsi, essayer d'accéder à CouchDB en utilisant localhost depuis le conteneur BusyBox ne fonctionnera pas, car CouchDB n'est pas en cours d'exécution dans ce conteneur mais plutôt dans un autre.

6. Call `couchdb1:5984` with `wget` from busybox container
   1. What happened ?
   	wget: bad address 'couchdb1:5984'
   2. Why ?
   	Cela se produit parce que par défaut, les conteneurs Docker ne sont pas conscients des autres conteneurs par leurs noms, à moins qu'ils ne soient explicitement liés ou qu'ils fassent partie du même réseau Docker personnalisé. Si on exécute simplement un conteneur BusyBox sans le connecter au même réseau que couchdb1 e système de noms de domaine (DNS) interne de Docker ne sera pas capable de résoudre couchdb1 en l'adresse IP appropriée.

7. Create a new network named `busyboxtocouchdb`
	docker network create busyboxtocouchdb

8. Connect `couchdb1` to the network with `docker network connect ...`
	docker network connect busyboxtocouchdb couchdb1

9. Re-run busybox connected to the same network
	docker run --rm -it --network=busyboxtocouchdb busybox

10. Call `couchdb1:5984` with `wget` from busybox container
	wget couchdb1:5984
	Connecting to couchdb1:5984 (172.19.0.2:5984)
	saving to 'index.html'
	index.html           100% |**********************************************************************************************************************************************************************************************|   247  0:00:00 ETA
	'index.html' saved
	/ # 

	Pourquoi ? Tous les deux conteneurs ont maintenant le même network ce qui leur permet de communiquer via le DNS interne de Docker. 
	La réussite indique une communication fluide entre conteneurs sur un réseau Docker, confirmant la configuration réseau correcte et l'accès inter-conteneurs.
