# Lab 3 - Network

## Expose port

### Tips

- Port must be higher than 1024

### Expose port

1. Pull `couchdb:2.1`
docker pull couchdb:2.1

2. Run couchdb, name it `couchedb1` and expose the port `5984` (detached)
Lancement d'un conteneur CouchDB nommé couchdb1 en exposant le port 5984 :

abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker (rabah_AZI/docker/labs|MERGING)
$ docker run -d --name couchdb1 -p 5984:5984 couchdb:2.1
6c830f916906ee0a9198793d99a39ea6a725da75b2ae96147b7987e0f258f5dd


3. Check the couchedb version on `http://localhost:5984`
{"couchdb":"Welcome","version":"2.1.2","features":["scheduler"],"vendor":{"name":"The Apache Software Foundation"}}
4. Run temporary busybox container
abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker (rabah_AZI/docker/labs|MERGING)
$ docker run --rm -it busybox wget -qO- http://localhost:5984
the input device is not a TTY.  If you are using mintty, try prefixing the command with 'winpty'

L'erreur rencontrer est due à une incompatibilité entre Docker et le terminal Mintty utilisé par Git Bash sous Windows, surtout lors de l'exécution de commandes interactives.

solution: 
winpty docker run --rm -it busybox wget -qO- http://localhost:5984



5. Call `localhost:5984` with `wget` from busybox container
   1. What happened ?
   2. Why ?
   abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker (rabah_AZI/docker/labs|MERGING)
$ winpty docker run --rm -it busybox wget -qO- http://localhost:5984
Unable to find image 'busybox:latest' locally
latest: Pulling from library/busybox
7b2699543f22: Pull complete
Digest: sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
Status: Downloaded newer image for busybox:latest
wget: can't connect to remote host (127.0.0.1): Connection refused

La commande a bien exécuté wget depuis un conteneur busybox pour essayer d'accéder à http://localhost:5984, mais elle a échoué avec "Connection refused". Cela confirme ce qui était attendu : dans le contexte d'un conteneur Docker, localhost fait référence au conteneur lui-même et non à l'hôte Docker ou à d'autres conteneurs. 
j'essaie d'accéder à CouchDB (qui s'exécute dans un autre conteneur ou sur l'hôte) via localhost depuis un conteneur busybox ne fonctionnera pas.

Pourquoi cela se produit-il ?
Quand on utilise localhost dans le conteneur busybox, il essaie de se connecter au port 5984 sur lui-même (où aucun service n'est en cours d'exécution), et non au service CouchDB qui est hébergé soit dans un autre conteneur soit sur l'hôte Docker. C'est pourquoi la connexion est refusée.
{"couchdb":"Welcome","version":"2.1.2","features":["scheduler"],"vendor":{"name":"The Apache Software Foundation"}}

6. Call `couchdb1:5984` with `wget` from busybox container
docker run --rm -it busybox wget -qO- http://localhost:5984

   1. What happened ?
   Lorsque j'ai tenté d'accéder à CouchDB en utilisant localhost:5984 depuis un conteneur BusyBox, la connexion a été refusée. Cependant, lorsque j'ai utilisé couchdb1:5984 dans le contexte d'un réseau Docker partagé (mynetwork), wget a réussi à obtenir une réponse de CouchDB, comme le montre la réponse JSON affichant la version de CouchDB et un message de bienvenue.
   {"couchdb":"Welcome","version":"2.1.2","features":["scheduler"],"vendor":{"name":"The Apache Software Foundation"}}
   2. Why ?
   L'accès à CouchDB en utilisant localhost:5984 a échoué parce que, dans le contexte du conteneur BusyBox, localhost fait référence au conteneur lui-même, et non à l'hôte Docker ou à un autre conteneur. Ainsi, il n'y avait pas de service CouchDB écoutant sur localhost:5984 dans le conteneur BusyBox.

En revanche, l'accès à couchdb1:5984 a réussi parce que les conteneurs CouchDB et BusyBox étaient connectés au même réseau Docker (mynetwork). Cela a permis au conteneur BusyBox de résoudre couchdb1 comme l'adresse du conteneur CouchDB et d'accéder à CouchDB en utilisant son nom de conteneur, car le réseau Docker gère la résolution de noms entre conteneurs connectés.
7. Create a new network named `busyboxtocouchdb` je l'ai appelé 'mynetwork'
docker network create busyboxtocouchdb ou mynetwork

j'ai créé un nouveau réseau Docker appelé mynetwork. Cette étape était nécessaire pour isoler et faciliter la communication entre les conteneurs spécifiques que je veux connecter.
8. Connect `couchdb1` to the network with `docker network connect ...`
docker network connect busyboxtocouchdb/mynetwork couchdb1

j'ai connecté le conteneur CouchDB (couchdb1) au réseau Docker mynetwork, permettant ainsi une communication isolée au sein de ce réseau.
9. Re-run busybox connected to the same network
10. Call `couchdb1:5984` with `wget` from busybox container
winpty docker run --rm -it --network busyboxtocouchdb/mynetwork busybox wget -qO- http://couchdb1:5984

Finalement, en appelant couchdb1:5984 avec wget depuis le conteneur BusyBox, j'ai réussi à accéder à CouchDB. Cela a été rendu possible grâce à la mise en réseau des conteneurs et à la résolution de noms interne de Docker, qui a permis au conteneur BusyBox de trouver et d'accéder à CouchDB par son nom de conteneur.