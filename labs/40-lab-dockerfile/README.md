# Lab 5 - Dockerfile

## Create your docker image

Create a dockerfile for a Flask application (python).

### Tips
 
### Create your dockerfile

1. There is two file 
   1. `requirement.txt`, contain python dependencies 
   2. `app.py`, contain our flask app that listen on port `9090`
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
6. Specify that the container use the port `9090`
7. Specify the maintainer and the version of the dockerfile
8. Make sure the container will run the command `python app.py`

### Build the image

1. Build the docker image and name it <dockerHubId>/my_flask:1.0
2. Push it to the docker hub

### Run it 

1. Run your application as `app`
2. curl localhost:9090




les commandes utilisées : 

 1753  cd ..
 1754  cd 40-lab-dockerfile/
 1755  ls
 1756  mkdir myapp
 1757  cd myapp
 1758  cd ..
 1759  ls
 1760  cp app.py myapp/
 1761  cp requirements.txt myapp/
 1762  tree
 1763  cd myapp/
 1764  touch Dockerfile
 1765  cat Dockerfile
 1766  docker build -t <dockerHubId>/my_flask:1.0 .
 1767  docker build -t cyprin02/my_flask:1.0 .
 1768  docker scout quickview
 1769  docker push cyprin02/my_flask:1.0 .
 1770  docker login
 1771  docker push cyprin02/my_flask:1.0 .
 1772  docker push cyprin02/my_flask:1.0
 1773  docker run -d -p 9090:9090 --name app cyprin02/my_flask:1.0
 1774  tree
 1775  curl http://localhost:9090
 1776  git status
 1777  git add .
 1778  git commit -m "lab4"
 1779  git push origin princy_rasolo/docker/labs
 1780  git status
 1781  git add .
 1782  git status
 1783  cd ..
 1784  git add .
 1785  git status
 1786  git commit -m "add capture photo lab4"
 1787  git push origin princy_rasolo/docker/labs
 1788  git status
 1789  history