# Lab 5 - docker-compose

## Create your docker-compose file

Create a docker-compose.yaml for a Flask application (python) that use a redis.

### Tips

### Create your file

1. There is two file 
   1. `requirement.txt`, contain python dependencies 
   2. `app.py`, contain our flask app that listen on port `9090`
2. Create a new directory named `myapp-compose` 
3. Copy `requirement.txt` and `app.py` in `myapp-compose`
4. Run `cd myapp-compose`
5. Create a file name `myapp-compose`

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

### set up the stack

1. Use the `docker-compose up -d` command

docker-compose up --build -d
[+] Building 0.0s (0/0)  docker:default
2024/04/11 15:18:16 http2: server: error reading preface from client //./pipe/docker_engine: file has already been clo[+] Building 11.1s (11/11) FINISHED                                                                    docker:default

docker-compose up -d  
[+] Running 2/2
 ✔ Container myapp-compose-redis-1  Running                                                                      0.0s 
 ✔ Container myapp-compose-web-1    Started                                                                      0.0s

2. curl the `localhost:9092`
   1. Check that the `number` of visit is incremented at each call

   curl localhost:9092
   This is a sfeir school about Docker ! 
   I have been seen 1 times.

   curl localhost:9092
   This is a sfeir school about Docker ! 
   I have been seen 2 times.