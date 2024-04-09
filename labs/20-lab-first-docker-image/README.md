# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`<br>
Terminal: docker run -d -p 80:80 --name mynginx1 nginx
2. Check that the nginx page (localhost:80)
![Alt text](image1.png)
3. Run a shell without stopping the Container<br>
Terminal: docker exec -it mynginx1 /bin/bash
4. Update the file `/usr/share/nginx/html/index.html` in the container<br>
Terminal: # echo "My Page" > /usr/share/nginx/html/index.html
5. Check that the nginx page has been updated (localhost:80)
![Alt text](image2.png)
6. Create a transitive image named `my_awsome_image`<br>
Terminal: docker commit mynginx1 my_awesome_image
7. Run the new image<br>
Terminal: docker run -d -p 8080:80 --name my_awesome_container my_awesome_image
8. Check that the modifications are still present (localhost:80)
![Alt text](image3.png)
9. Check the layer with the `docker history` command<br>
Terminal: docker history my_awesome_image<br>
Terminal Result:<br>
![Alt text](image4.png)

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`<br>
Terminal: docker tag my_awesome_image kuramathi/my_awesome_image:1.0
2. List your docker images<br>
Terminal: docker images<br>
   1. What do you see ?
   ![Alt text](image5.png)
3. Use the CLI to log into your docker account<br>
Terminal: docker login<br>
4. Push your image
Command: docker push kuramathi/my_awesome_image:1.0<br>
5. Check that your image is available on `https://hub.docker.com/r/leonardeaux/my_awesome_image`
![Alt text](image6.png)
6. Delete the repository `https://hub.docker.com/repository/docker/leonardeaux/my_awesome_image/settings`
![Alt text](image7.png)