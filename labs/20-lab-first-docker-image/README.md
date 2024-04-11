# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`
   # docker run -d -p 80:80 --name mynginx1 nginx
2. Check that the nginx page (localhost:80)
   # I opened a web browser and pasted the URL http://localhost:80. I saw the Nginx welcome page
3. Run a shell without stopping the Container
   # docker exec -it mynginx1 sh
4. Update the file `/usr/share/nginx/html/index.html` in the container
   # echo "Hello, this is Sandro's page!">/usr/share/nginx/html/index.html
   # exit
5. Check that the nginx page has been updated (localhost:80)
   # The nginx page now displays "Hello, this is Sandro's page!" 
6. Create a transitive image named `my_awsome_image`
   # docker commit mynginx1 my_awsome_image
7. Run the new image
   # docker run -d -p 80:80 --name newcontainer my_awsome_image
8. Check that the modifications are still present (localhost:80)
   # I had the error "Bind for 0.0.0.0:80 failed: port is already allocated." It is not possible to copy to the same port
9. Check the layer with the `docker history` command
   # docker history my_awsome_image

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`
   # docker tag my_awsome_image sandrolena/my_awsome_image:1.0
2. List your docker images
   # docker images
   1. What do you see ?
   # I see  my_awsome_image which I just created along with other images (nginx and others I created before)
3. Use the CLI to log into your docker account
   # docker login
4. Push your image
   # docker push sandrolena/my_awsome_image:1.0
5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
   # https://hub.docker.com/repository/docker/sandrolena/my_awsome_image
   # my_awsome_image is available here
6. Delete the repository `https://hub.docker.com/repository/docker/sandrolena/my_awsome_image/settings`
   # To delete the repository I had to use the URL "https://hub.docker.com/repository/docker/sandrolena/my_awsome_image" then go to the bottom of the page, click on "Delete repository" and type the name of the repository I wanted to delete to confirm the deletion