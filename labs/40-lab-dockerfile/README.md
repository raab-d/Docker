# Lab 5 - Dockerfile

## Create your docker image

Create a dockerfile for a Flask application (python).

### Tips
 
### Create your dockerfile

1. There is two file 
   1. `requirement.txt`, contain python dependencies 
   2. `app.py`, contain our flask app that listen on port `9090`
2. Create a new directory named `myapp` 
<br> mkdir myapp
3. Copy `requirement.txt` and `app.py` in `myapp`
<br> cp ./labs/40-lab-dockerfile/requirements.txt ./labs/40-lab-dockerfile/app.py myapp/
4. Run `cd myapp`
5. Create a file name `Dockerfile`

### Modify the dockerfile

1. Use a python image as base
2. Copy `requirement.txt` in `/app/requirements.txt`
3. Define `/app` as working directory
4. Install python dependencies using `pip install -r <file>`
5. Copy `app.py` inside `/app`
6. Specify that the container use the port `9090`
7. Specify the maintainer and the version of the dockerfile
8. Make sure the container will run the command `python app.py`

### Build the image

1. Build the docker image and name it <dockerHubId>/my_flask:1.0
<br> docker build -t dionisauce/my_flask:1.0 .

2. Push it to the docker hub
<br> docker push dionisauce/my_flask:1.0


### Run it 

1. Run your application as `app`
<br> docker run -d -p 9090:9090 --name app dionisauce/my_flask:1.0

2. curl localhost:9090
<br> curl localhost:9090
<br> This is a sfeir school about Docker !