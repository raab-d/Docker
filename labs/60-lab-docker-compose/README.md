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
2. curl the `localhost:9092`
   1. Check that the `number` of visit is incremented at each call
### test de l'application 
   abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker_bis/Docker/myapp-compose (rabah_AZI/docker/labs)
$ curl localhost:9092
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    65  100    65    0     0   6057      0 --:--:-- --:--:-- --:--:--  6500This is a sfeir school about Docker !
I have been seen 7 times.




# l'application fonctionne sur le port 6379 et compte le nombre de visite du site
abdou@Rabs MINGW64 ~/Desktop/ESGI/S2/docker/Docker_bis/Docker/myapp-compose (rabah_AZI/docker/labs)
$ docker ps
CONTAINER ID   IMAGE               COMMAND                  CREATED         STATUS         PORTS                                        NAMES
c033e9f81d16   redis:alpine        "docker-entrypoint.s…"   6 minutes ago   Up 6 minutes   6379/tcp                                     myapp-compose-redis-1
69afd42a8c93   myapp-compose-web   "python app.py"          6 minutes ago   Up 6 minutes   0.0.0.0:9092->9090/tcp                       myapp-compose-web-1
6c830f916906   couchdb:2.1         "tini -- /docker-ent…"   2 hours ago     Up 2 hours     4369/tcp, 9100/tcp, 0.0.0.0:5984->5984/tcp   couchdb1
14c7c7a82859   my_awesome_image    "/docker-entrypoint.…"   46 hours ago    Up 46 hours    0.0.0.0:8080->80/tcp                         customnginx
b551c5afff2f   nginx               "/docker-entrypoint.…"   47 hours ago    Up 47 hours    0.0.0.0:80->80/tcp                           mynginx1

# sur le web
http://localhost:9092/
This is a sfeir school about Docker ! I have been seen 8 times.