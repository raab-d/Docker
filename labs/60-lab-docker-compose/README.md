# Lab 5 - docker-compose

## Create your docker-compose file

Create a docker-compose.yaml for a Flask application (python) that use a redis.

### Tips

### Create your file

1. There is two file 
<br>
   1. `requirement.txt`, contain python dependencies 
   <br>
   2. `app.py`, contain our flask app that listen on port `9090`
   <br>
2. Create a new directory named `myapp-compose` 
<br>mkdir myapp-compose
<br>cd myapp-compose

   3. Copy `requirement.txt` and `app.py` in `myapp-compose`
   <br>cp ./labs/60-lab-docker-compose/app.py ./labs/60-lab-docker-compose/requirements.txt ./myapp-compose
4. Run `cd myapp-compose`
<br>
5. Create a file name `myapp-compose`
<br>touch myapp-compose


### Modify the myapp-compose

1. Use the version `3.9`
<br>
2. 2 services
<br>
   1. `web`
   <br>
      1. Build on demand the dockerfile
      <br>
      2. Expose the port 9092:9090
      <br>
      3. Has a network `my-shared-network`
      <br>
  2. `redis`
     1. Image: `redis:alpine`
     2. Has a network `my-shared-network`
3. A network `my-shared-network`

### set up the stack

1. Use the `docker-compose up -d` command
2. curl the `localhost:9092`
<br> curl localhost:9092
<br> This is a sfeir school about Docker ! 
<br> I have been seen 1 times.

   1. Check that the `number` of visit is incremented at each call
   <br> it works !
   <br> This is a sfeir school about Docker ! 
   <br> I have been seen 4 times.
