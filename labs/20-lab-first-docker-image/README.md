# Lab 2 - Your first docker images
## Create a transitive image
### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`
Command: docker run -d -p 80:80 --name mynginx1 nginx
2. Check that the nginx page (localhost:80)
![alt text](./image.png)
3. Run a shell without stopping the Container<br>
Command: docker exec -it mynginx1 /bin/bash<br>
4. Update the file `/usr/share/nginx/html/index.html` in the container
# echo "My Custom Page" > /usr/share/nginx/html/index.html
5. Check that the nginx page has been updated (localhost:80)<br>
![alt text](image-1.png)<br>
6. Create a transitive image named `my_awsome_image`<br>
Command: docker commit mynginx1 my_awesome_image<br>
7. Run the new image<br>
Command: docker run -d -p 8080:80 --name my_awesome_container my_awesome_image<br>
8. Check that the modifications are still present (localhost:80)<br>
![alt text](image-2.png)<br>
9. Check the layer with the `docker history` command<br>
Command: docker history my_awesome_image<br>
Result : <br>
![alt text](image-3.png)<br>

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`<br>
Command: docker tag my_awesome_image kuramathi/my_awesome_image:1.0<br>
2. List your docker images<br>
Command: docker images<br>
   1. What do you see ?<br>
   ![alt text](image-4.png)<br>
3. Use the CLI to log into your docker account<br>
Command: docker login<br>
4. Push your image<br>
Command: docker push kuramathi/my_awesome_image:1.0<br>
5. Check that your image is available on `https://hub.docker.com/repository/docker/kuramathi/my_awsome_image/`<br>
![alt text](image-5.png)<br>
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`<br>
![alt text](image-6.png)<br>