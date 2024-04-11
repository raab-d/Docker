# Lab 3 - Network

## Expose port

### Tips

- Port must be higher than 1024

### Expose port

1. Pull `couchdb:2.1`
<br> docker pull couchdb:2.1

2. Run couchdb, name it `couchedb1` and expose the port `5984` (detached)
<br> docker run -d --name couchdb1 -p 5984:5984 couchdb:2.1
3. Check the couchedb version on `http://localhost:5984`
4. Run temporary busybox container
<br> docker run --rm -it busybox
5. Call `localhost:5984` with `wget` from busybox container
   1. What happened ?<br>
   / # wget localhost:5984 <br>
Connecting to localhost:5984 (127.0.0.1:5984) <br>
wget: can't connect to remote host (127.0.0.1): Connection refused

   <br> Une erreur survient et cela indique que la tentative de connexion au port 5984 sur l'adresse localhost (127.0.0.1) depuis le conteneur busybox a échoué car aucune application n'écoutait sur ce port dans le conteneur busybox.
   <br> 
   2. Why ?
   <br> Le conteneur busybox se réfère uniquement à lui-même. Il n'y a donc pas de service écoutant sur le port 5984 dans ce conteneur.
6. Call `couchdb1:5984` with `wget` from busybox container
<br> wget couchdb1:5984
   1. What happened ? <br> wget: bad address 'couchdb1:5984' 
   <br> Le conteneur BusyBox n'a pas pu résoudre l'adresse de couchdb1 parce qu'il ne reconnaît pas le nom du conteneur couchdb1.
   
   2. Why ?
   <br> Cela est dû au fait que les deux conteneurs ne sont pas sur le même réseau Docker et donc ne peuvent pas se résoudre par leurs noms de conteneur respectifs.
7. Create a new network named `busyboxtocouchdb`
<br> docker network create busyboxtocouchdb

8. Connect `couchdb1` to the network with `docker network connect ...`
<br> docker network connect busyboxtocouchdb couchdb1
9. Re-run busybox connected to the same network
<br> docker run --rm -it --network busyboxtocouchdb busybox

10. Call `couchdb1:5984` with `wget` from busybox container
<br> wget couchdb1:5984
Connecting to couchdb1:5984 (172.18.0.2:5984)
saving to 'index.html'
index.html           100% |**************************************************************************************************************************************************************|   116  0:00:00 ETA 
'index.html' saved
