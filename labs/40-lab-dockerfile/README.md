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

docker build -t zhoupinou/my_flask:1.0 .
[+] Building 49.8s (11/11) FINISHED                                                                    docker:default
 => [internal] load build definition from Dockerfile                                                             0.0s
 => => transferring dockerfile: 555B                                                                             0.0s 
 => [internal] load metadata for docker.io/library/python:3.8                                                    1.2s 
 => [auth] library/python:pull token for registry-1.docker.io                                                    0.0s
 => [internal] load .dockerignore                                                                                0.0s
 => => transferring context: 2B                                                                                  0.0s 
 => [1/5] FROM docker.io/library/python:3.8@sha256:678cb8283ebbc43cf64110cb025d8836247db286683e7a9c38c903ce946  38.9s 
 => => resolve docker.io/library/python:3.8@sha256:678cb8283ebbc43cf64110cb025d8836247db286683e7a9c38c903ce9466  0.0s 
 => => sha256:b22191dc7e2839324e89291f6a4b46d62e93af1732ac43b0cd94f9ae9cf56d19 7.36kB / 7.36kB                   0.0s 
 => => sha256:609c73876867487da051ad470002217da69bb052e2538710ade0730d893ff51f 49.56MB / 49.56MB                16.7s 
 => => sha256:7247ea8d81e671d079d67f3a9909315ef4641b45db90d62a1b18e3430c1937d4 24.05MB / 24.05MB                 3.5s
 => => sha256:be374d06f38273b62ddd7aa5bc3ce3f9c781fd49a1f5a5dd94a46d2986920d7a 64.14MB / 64.14MB                 8.3s 
 => => sha256:95f1e554af9c2ce17ccb9437e95e59cb015e1c2b0987f7ee0156cc94476fadcb 2.01kB / 2.01kB                   0.0s 
 => => sha256:678cb8283ebbc43cf64110cb025d8836247db286683e7a9c38c903ce946612a2 1.86kB / 1.86kB                   0.0s 
 => => sha256:b4580645a8e50b87a19330da289a9b1540022379f2c99d3f0112e3c5c4a8d051 211.14MB / 211.14MB              23.5s 
 => => sha256:aa7e0aca67ddfc342e2afe83df590a0e228e34781e7206639ddd9da72a71a0af 6.39MB / 6.39MB                   9.3s 
 => => sha256:32120056a9fe3594e5fbce0a5f08561ba976f9b52e8f14eccca9807fe6660741 15.20MB / 15.20MB                11.6s 
 => => sha256:19107d8e07f6a0b65356139c9458cce3955ee0fef09021002971ba919feb0d3f 245B / 245B                      11.7s 
 => => sha256:2fd0a626ceb4ced86afa0c52f8900554aefee83e12bf312b3b6d0af1e1f85e90 2.85MB / 2.85MB                  12.7s 
 => => extracting sha256:609c73876867487da051ad470002217da69bb052e2538710ade0730d893ff51f                        3.8s 
 => => extracting sha256:7247ea8d81e671d079d67f3a9909315ef4641b45db90d62a1b18e3430c1937d4                        1.0s 
 => => extracting sha256:be374d06f38273b62ddd7aa5bc3ce3f9c781fd49a1f5a5dd94a46d2986920d7a                        3.8s 
 => => extracting sha256:b4580645a8e50b87a19330da289a9b1540022379f2c99d3f0112e3c5c4a8d051                        9.4s 
 => => extracting sha256:aa7e0aca67ddfc342e2afe83df590a0e228e34781e7206639ddd9da72a71a0af                        0.4s 
 => => extracting sha256:32120056a9fe3594e5fbce0a5f08561ba976f9b52e8f14eccca9807fe6660741                        0.6s 
 => => extracting sha256:19107d8e07f6a0b65356139c9458cce3955ee0fef09021002971ba919feb0d3f                        0.0s 
 => => extracting sha256:2fd0a626ceb4ced86afa0c52f8900554aefee83e12bf312b3b6d0af1e1f85e90                        0.4s 
 => [internal] load build context                                                                                0.0s 
 => => transferring context: 265B                                                                                0.0s 
 => [2/5] COPY requirements.txt /app/requirements.txt                                                            3.2s 
 => [3/5] WORKDIR /app                                                                                           0.1s 
 => [4/5] RUN pip install -r requirements.txt                                                                    5.8s 
 => [5/5] COPY app.py /app                                                                                       0.1s 
 => exporting to image                                                                                           0.2s 
 => => exporting layers                                                                                          0.2s 
 => => writing image sha256:6e16db2efcd2c0b21a3c35dc1c564002d8ca1b19e42c139f3838f1a5a4223415                     0.0s 
 => => naming to docker.io/zhoupinou/my_flask:1.0                                                                0.0s 

2. Push it to the docker hub

### Run it 

1. Run your application as `app`

docker run -d -p 9090:9090 --name app zhoupinou/my_flask:1.0    
>> 
4568b2a51504c735088cd93d0f88459c188936c3dd2f43020852feafe8fd6cef

2. curl localhost:9090

curl localhost:9090
This is a sfeir school about Docker !