# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`
<br> docker run --name mynginx1 -d -p 80:80 nginx
2. Check that the nginx page (localhost:80)
<br> http://localhost:80
3. Run a shell without stopping the Container
<br> docker exec -it mynginx1 sh
4. Update the file `/usr/share/nginx/html/index.html` in the container
<br> echo "Your new content here" > /usr/share/nginx/html/index.html
5. Check that the nginx page has been updated (localhost:80)
<br> it updated the page with the new content
6. Create a transitive image named `my_awsome_image`
<br> docker commit mynginx1 my_awsome_image
7. Run the new image
<br> docker run --name mynginx2 -d -p 81:80 my_awsome_image
<br> new port 81:80
8. Check that the modifications are still present (localhost:80)
<br> http://localhost:81
9. Check the layer with the `docker history` command
<br> docker history my_awsome_image

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`
<br>  docker tag my_awsome_image dionisauce/my_awsome_image:1.0
2. List your docker images
<br> docker images
   1. What do you see ?
   <br> REPOSITORY                   TAG       IMAGE ID       CREATED          SIZE
<br> dionisauce/my_awsome_image   1.0       53d090f0b140   23 minutes ago   187MB
<br> my_awsome_image              latest    53d090f0b140   23 minutes ago   187MB
<br> nginx                        latest    92b11f67642b   7 weeks ago      187MB

3. Use the CLI to log into your docker account
<br> docker login
4. Push your image
<br> docker push dionisauce/my_awsome_image:1.0
5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
<br> https://hub.docker.com/repository/docker/dionisauce/my_awsome_image/
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`
<br> 