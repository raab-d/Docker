 Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`

   PS C:\Users\ghost\Desktop\5iabd\Docker\labs> docker run -d -p 80:80 --name mynginx1 nginx

   Unable to find image 'nginx:latest' locally
   latest: Pulling from library/nginx
   8a1e25ce7c4f: Pull complete
   e78b137be355: Pull complete
   39fc875bd2b2: Pull complete
   035788421403: Pull complete 
   87c3fb37cbf2: Pull complete
   c5cdd1ce752d: Pull complete
   33952c599532: Pull complete
   Digest: sha256:6db391d1c0cfb30588ba0bf72ea999404f2764febf0f1f196acd5867ac7efa7e
   Status: Downloaded newer image for nginx:latest
   23a691562cf5f252f2b99ad6e7ef9cc4bb41ad9d4bb4d49342edf0e9487c9b62
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs> 

2. Check that the nginx page (localhost:80)

   PS C:\Users\ghost\Desktop\5iabd\Docker\labs> curl http://127.0.0.1:80

   StatusCode        : 200
   StatusDescription : OK
   Content           : <!DOCTYPE html>
                     <html>
                     <head>
                     <title>Welcome to nginx!</title>
                     <style>
                     html { color-scheme: light dark; }
                     body { width: 35em; margin: 0 auto;
                     font-family: Tahoma, Verdana, Arial, sans-serif; }
                     </style...
   RawContent        : HTTP/1.1 200 OK
                     Connection: keep-alive
                     Accept-Ranges: bytes
                     Content-Length: 615
                     Content-Type: text/html
                     Date: Tue, 09 Apr 2024 15:16:27 GMT
                     ETag: "65cce434-267"
                     Last-Modified: Wed, 14 Feb 2024 ...
   Forms             : {}
   Headers           : {[Connection, keep-alive], [Accept-Ranges, bytes], [Content-Length,  
                     615], [Content-Type, text/html]...}
   Images            : {}
   InputFields       : {}
   Links             : {@{innerHTML=nginx.org; innerText=nginx.org; outerHTML=<A
                     href="http://nginx.org/">nginx.org</A>; outerText=nginx.org;
                     tagName=A; href=http://nginx.org/}, @{innerHTML=nginx.com;
                     innerText=nginx.com; outerHTML=<A
                     href="http://nginx.com/">nginx.com</A>; outerText=nginx.com;
                     tagName=A; href=http://nginx.com/}}
   ParsedHtml        : mshtml.HTMLDocumentClass
   RawContentLength  : 615

3. Run a shell without stopping the Container

   PS C:\Users\ghost\Desktop\5iabd\Docker\labs> docker exec -it mynginx1 /bin/bash
   >>
   root@23a691562cf5:/# pwd
   /
   root@23a691562cf5:/# ls
   bin   docker-entrypoint.d   home   media  proc  sbin  tmp
   boot  docker-entrypoint.sh  lib    mnt    root  srv   usr
   dev   etc                   lib64  opt    run   sys   var

4. Update the file `/usr/share/nginx/html/index.html` in the container

   root@23a691562cf5:/# echo "Updated content" > /usr/share/nginx/html/index.html


5. Check that the nginx page has been updated (localhost:80)

   PS C:\Users\ghost\Desktop\5iabd\Docker\labs> curl http://127.0.0.1:80
      

   StatusCode        : 200
   StatusDescription : OK
   Content           : Updated content

   RawContent        : HTTP/1.1 200 OK
                     Connection: keep-alive
                     Accept-Ranges: bytes
                     Content-Length: 16
                     Content-Type: text/html
                     Date: Tue, 09 Apr 2024 15:21:30 GMT
                     ETag: "66155c8e-10"
                     Last-Modified: Tue, 09 Apr 2024 15...
   Forms             : {}
   Headers           : {[Connection, keep-alive], [Accept-Ranges, bytes], [Content-Length,  
                     16], [Content-Type, text/html]...}
   Images            : {}
   InputFields       : {}
   Links             : {}
   ParsedHtml        : mshtml.HTMLDocumentClass
   RawContentLength  : 16



   PS C:\Users\ghost\Desktop\5iabd\Docker\labs>

6. Create a transitive image named `my_awsome_image`

   docker commit mynginx1 my_awesome_image
   sha256:8710ef2792dba85899659eb6d7e5b99daeaed909b7e9bbea7dad570da70898f6
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs> docker image ls
   REPOSITORY         TAG       IMAGE ID       CREATED          SIZE
   my_awesome_image   latest    8710ef2792db   20 seconds ago   187MB
   nginx              latest    92b11f67642b   7 weeks ago      187MB
   PS C:\Users\ghost\Desktop\5iabd\Docker\labs> 


7. Run the new image

   PS C:\Users\ghost\Desktop\5iabd\Docker\labs> docker run -d -p 80:80 --name mynewnginx my_awesome_image
   ccc7bb151f237502804c99fc6b2585b593410e80717d39c2a5c1339d5de8830b

8. Check that the modifications are still present (localhost:80)
9. Check the layer with the `docker history` command
docker history my_awesome_image  
IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT  
0a7d100c2708   2 minutes ago   nginx -g daemon off;                            1.17kB  
92b11f67642b   7 weeks ago     CMD ["nginx" "-g" "daemon off;"]                0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     STOPSIGNAL SIGQUIT                              0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     EXPOSE map[80/tcp:{}]                           0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     ENTRYPOINT ["/docker-entrypoint.sh"]            0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     COPY 30-tune-worker-processes.sh /docker-ent…   4.62kB    buildkit.dockerfile.v0  
<missing>      7 weeks ago     COPY 20-envsubst-on-templates.sh /docker-ent…   3.02kB    buildkit.dockerfile.v0  
<missing>      7 weeks ago     COPY 15-local-resolvers.envsh /docker-entryp…   336B      buildkit.dockerfile.v0  
<missing>      7 weeks ago     COPY 10-listen-on-ipv6-by-default.sh /docker…   2.12kB    buildkit.dockerfile.v0  
<missing>      7 weeks ago     COPY docker-entrypoint.sh / # buildkit          1.62kB    buildkit.dockerfile.v0  
<missing>      7 weeks ago     RUN /bin/sh -c set -x     && groupadd --syst…   112MB     buildkit.dockerfile.v0  
<missing>      7 weeks ago     ENV PKG_RELEASE=1~bookworm                      0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     ENV NJS_VERSION=0.8.3                           0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     ENV NGINX_VERSION=1.25.4                        0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     LABEL maintainer=NGINX Docker Maintainers <d…   0B        buildkit.dockerfile.v0  
<missing>      7 weeks ago     /bin/sh -c #(nop)  CMD ["bash"]                 0B  
<missing>      7 weeks ago     /bin/sh -c #(nop) ADD file:b86ae1c7ca3586d8f…   74.8MB  
### Upload our image

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`  
docker commit mynginx1 my_awesome_image:1.0  
ccc7bb151f237502804c99fc6b2585b593410e80717d39c2a5c1339d5de8830b
2. List your docker images
   1. What do you see ?  
   REPOSITORY         TAG       IMAGE ID       CREATED         SIZE  
   my_awesome_image   1.0       7c81e4aac041   8 seconds ago   187MB  
   my_awesome_image   latest    0a7d100c2708   4 minutes ago   187MB  
   nginx              latest    92b11f67642b   7 weeks ago     187MB  
3. Use the CLI to log into your docker account
4. Push your image
5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
https://hub.docker.com/r/davidzer/my_awesome_image
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`
repository supprimer depuis le hub