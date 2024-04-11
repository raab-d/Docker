# Lab 3 - Network

## Expose port

### Tips

- Port must be higher than 1024

### Expose port

1. Pull `couchdb:2.1` (`docker pull couchdb:2.1`)
2. Run couchdb, name it `couchedb1` and expose the port `5984` (detached) (`docker run -d -p 5984:5984 --name couchdb1 couchdb:2.1`)
3. Check the couchedb version on `http://localhost:5984`
Accessing http://localhost:5984 should show the CouchDB version as "2.1.2". This confirms that the container is running and accessible.
4. Run temporary busybox container
Command: `docker run -it --rm busybox`
A BusyBox container is started for testing network connectivity.
5. Call `localhost:5984` with `wget` from busybox container
   1. What happened ?
   Outcome: Error stating wget: can't connect to remote host (127.0.0.1): Connection refused.
   2. Why ? 
   This error occurs because within the context of the BusyBox container, localhost refers to the container itself, not the Docker host where couchdb1 is accessible.
6. Call `couchdb1:5984` with `wget` from busybox container
   1. What happened ?
   Outcome: Error stating wget: bad address 'couchdb1:5984'.
   2. Why ? 
   This failure happens because couchdb1 is not recognized as a hostname by the BusyBox container. By default, containers do not share a network namespace and cannot resolve each other by name unless explicitly connected to the same network.
7. Create a new network named `busyboxtocouchdb`
Command: `docker network create busyboxtocouchdb`
A custom network named busyboxtocouchdb is created to facilitate communication between containers.
8. Connect `couchdb1` to the network with `docker network connect ...`
Command: `docker network connect busyboxtocouchdb couchdb1`
This connects the couchdb1 container to the newly created network, allowing other containers on the same network to communicate with it.
9. Re-run busybox connected to the same network (Command: `docker run -it --rm --network busyboxtocouchdb busybox`)
The BusyBox container is now also connected to busyboxtocouchdb, sharing a network namespace with couchdb1.
10. Call `couchdb1:5984` with `wget` from busybox container (Command: `wget couchdb1:5984`)
Why? With both containers on the same network, couchdb1 is recognized as a hostname within the BusyBox container. This showcases Docker's network isolation features and how custom networks can be used to facilitate container-to-container communication.