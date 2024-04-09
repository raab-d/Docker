# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`
	docker run --name mynginx1 -d -p 80:80 nginx
2. Check that the nginx page (localhost:80)
	It works  : "Welcome to nginx!If you see this page, the nginx web server is successfully installed and working. Further configuration is required....."
3. Run a shell without stopping the Container
	docker exec -it mynginx1 /bin/bash
4. Update the file `/usr/share/nginx/html/index.html` in the container
	echo "<H1> Hello, World! <H1>" > /usr/share/nginx/html/index.html
5. Check that the nginx page has been updated (localhost:80)
	Had "Hello, World" in title H1 characteristics in my screen
6. Create a transitive image named `my_awsome_image`
	docker commit mynginx1 my_awesome_image
7. Run the new image
	docker run -d -p 8080:80 --name myawesomecontainer my_awesome_image
8. Check that the modifications are still present (localhost:80)
	They are still present
9. Check the layer with the `docker history` command
	docker history nginx 
	docker history my_awsome_image 

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`
	docker tag my_awesome_image anna2000/my_awesome_image:1.0
2. List your docker images
	docker image ls -a
   1. What do you see ?
   		A new image has been created with the repo anna2000/my_awesome_image
3. Use the CLI to log into your docker account
	docker login
4. Push your image
	docker push anna2000/my_awesome_image:1.0
5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
	It's available !!!!
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`
	Deleted the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings` after confirming the name. 