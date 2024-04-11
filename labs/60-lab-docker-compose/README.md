# Lab 5 - docker-compose

## Create your docker-compose file

Create a docker-compose.yaml for a Flask application (python) that use a redis.

### Tips

### Create your file

1. There is two file 
   1. `requirement.txt`, contain python dependencies 
   2. `app.py`, contain our flask app that listen on port `9090`
2. Create a new directory named `myapp-compose` 
  mkdir myapp-compose
3. Copy `requirement.txt` and `app.py` in `myapp-compose`
  cp requirements.txt myapp-compose 
  cp app.py myapp-compose 
  cp Dockerfile myapp-compose 
4. Run `cd myapp-compose`
  Pour se placer dans le dossiter myapp-compose
5. Create a file name `myapp-compose`
  touch myapp-compose

### Modify the myapp-compose

1. Use the version `3.9`
2. 2 services
   1. `web`
      1. Build on demand the dockerfile
      2. Expose the port 9092:9090
      3. Has a network `my-shared-network`
  2. `redis`
     1. Image: `redis:alpine`
     2. Has a network `my-shared-network`
3. A network `my-shared-network`

  Contenu du docker-compose : 

'''
  version: '3.9'

  services:
    web:
      build: .
      ports:
        - "9092:9090"
      networks:
        - my-shared-network

    redis:
      image: redis:alpine
      networks:
        - my-shared-network

  networks:
  my-shared-network:
'''


### set up the stack

1. Use the `docker-compose up -d` command
  Ne fonctionne pas tant qu'on a pas renommé le fichier myapp-compose en "docker-compose.yaml" et placé le Dockerfile dans le même dossier.
  Lance les services en mode detached. Démarre les conteneurs en background 
2. curl the `localhost:9092`
   1. Check that the `number` of visit is incremented at each call
   "This is a sfeir school about Docker ! I have been seen n times." avec n le nombre de call. 