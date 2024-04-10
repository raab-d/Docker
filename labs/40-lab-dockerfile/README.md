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

Answer : I used this command to build : docker build -t nadim1/my_flask:1.0 . and theseare the last
few lines of the logs : 
 => => writing image sha256:456b6f43c38a395cb5d35fca66ec28bda91c30704c16278917b174e8e2cff2e7                           0.0s 
 => => naming to docker.io/nadim1/my_flask:1.0                                                                         0.0s 

What's Next?
  View a summary of image vulnerabilities and recommendations → docker scout quickview


2. Push it to the docker hub
Answer : i used this command to push : docker push nadim1/my_flask:1.0
Logs : 
2adfe632ae1c: Mounted from library/python
a03ae7e93f37: Mounted from library/python
e35535ad594c: Mounted from library/python
bfc9081d1eb2: Mounted from library/python
1f00ff201478: Mounted from library/python
1.0: digest: sha256:f32aef2ccbfe18721af7a44ea83ea6bfabd2a5143edf00fb365318d67cb85c69 size: 2201

### Run it 

1. Run your application as `app`
Answer : I used this command to run the app i created : docker run -d -p 9090:9090 --name app nadim1/my_flask:1.0
when i look at the app in docker hub, i can see the green active tag 1.0

2. curl localhost:9090
Answer : so since i am using windows and i cant excute curl, i used an alternative cmd that must be executed on PowerShell : iwr http://localhost:9090
and this is the results : 
PS C:\*\Docker\labs\40-lab-dockerfile\myapp> iwr http://localhost:9090


StatusCode        : 200
StatusDescription : OK
Content           : This is a sfeir school about Docker !
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 37
                    Content-Type: text/html; charset=utf-8
                    Date: Wed, 10 Apr 2024 15:34:11 GMT
                    Server: Werkzeug/3.0.2 Python/3.8.19

                    This is a sfeir school abou...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 37], [Content-Type, text/html; charset=utf-8], [Date, Wed,
                    10 Apr 2024 15:34:11 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 37