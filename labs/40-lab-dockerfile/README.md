# Lab 5 - Dockerfile

## Create your docker image

Create a dockerfile for a Flask application (python).

### Tips
 
### Create your dockerfile

1. There is two file 
   1. `requirement.txt`, contain python dependencies 
   2. `app.py`, contain our flask app that listen on port `8080`
2. Create a new directory named `myapp` 
3. Copy `requirement.txt` and `app.py` in `myapp`
4. Run `cd myapp`
5. Create a file name `Dockerfile`

### Modify the dockerfile

1. Use a python image as base
2. Copy `requirement.txt` in `/app/requirements.txt`
3. Define `/app` as working directory
4. Install python dependencies using `pip install -r <file>`
5. Copy `app.py` inside `/app`
6. Specify that the container use the port `8080`
7. Specify the maintainer and the version of the dockerfile
8. Make sure the container will run the command `python app.py`

### Build the image

1. Build the docker image and name it <dockerHubId>/my_flask:1.0
 
   docker build labs/40-lab-dockerfile/myapp -t my_flask:1.0 
  
2. Push it to the docker hub
 
   docker tag my_flask:1.0 soso/my_flask:1.0
   docker push soso/my_flask:1.0
  

### Run it 

1. Run your application as `app`
 
docker run my_flask:1.0                                  
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080 (elle ne fait rien resortir)
 * Running on http://172.17.0.2:8080
Press CTRL+C to quit
172.17.0.1 - - [10/Apr/2024 16:11:46] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [10/Apr/2024 16:11:48] "GET /favicon.ico HTTP/1.1" 404 -
  
2. curl localhost:8080
 
curl 172.17.0.2:8080
This is a sfeir school about Docker !% 
  