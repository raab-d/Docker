# Lab 3 - Network

## Expose port

### Tips

- Port must be higher than 1024

### Expose port

1. Pull `couchdb:2.1`

docker pull couchdb:2.1
2.1: Pulling from library/couchdb
Digest: sha256:05a8b4a9bfe8e90fdf8630b404098aab5122c8ead228ad9b8d081309266b1cfb
Status: Image is up to date for couchdb:2.1
docker.io/library/couchdb:2.1

2. Run couchdb, name it `couchedb1` and expose the port `5984` (detached)

docker run -d -p 5984:5984 --name couchdb1 couchdb:2.1
995b5aaa185847d426b7de76166b41c0f764506035536e39a984079efb8b780d

3. Check the couchedb version on `http://localhost:5984`

{
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

docker run -it --rm busybox

5. Call `localhost:5984` with `wget` from busybox container
   1. What happened ?

   / # wget localhost:5984
   Connecting to localhost:5984 (127.0.0.1:5984)
   wget: can't connect to remote host (127.0.0.1): Connection refused

   2. Why ?

   La commande appelle le localhost:5984 de busybox et non la machine hôte, c'est pour ça que ça ne fonctionne pas.

6. Call `couchdb1:5984` with `wget` from busybox container
   1. What happened ?

   / # wget couchdb1:5984
   wget: bad address 'couchdb1:5984'

   2. Why ?

   Les containers Docker ont par défaut un réseau indépendant, couchdb1 n'est pas reconnu par le réseau par défaut de busybox.

7. Create a new network named `busyboxtocouchdb`

docker network create busyboxtocouchdb
ed6f85cd14ee8faf566424e69ac5bf097f2ef872bc8111703bceaed20d368fef

8. Connect `couchdb1` to the network with `docker network connect ...`

docker network connect busyboxtocouchdb couchdb1

9. Re-run busybox connected to the same network

docker run -it --rm --network busyboxtocouchdb busybox

10. Call `couchdb1:5984` with `wget` from busybox container

/ # wget couchdb1:5984
Connecting to couchdb1:5984 (172.18.0.2:5984)
saving to 'index.html'
index.html           100% |**********************************************************************|   116  0:00:00 ETA 
'index.html' saved