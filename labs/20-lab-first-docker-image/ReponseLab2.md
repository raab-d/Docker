# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

<br>1. Run `nginx` image detached with param `-p 80:80` named `mynginx1`</br>
 <br>docker run --name mynginx1 -d -p 80:80 nginx</br>

<br>2. Check that the nginx page (localhost:80)</br>
<br>http://localhost:80</br>

<br>3. Run a shell without stopping the Container</br>
<br>winpty docker exec -it mynginx1 /bin/bash</br>

<br>4. Update the file `/usr/share/nginx/html/index.html` in the container</br>
<br>echo 'Salut tous le monde' > /usr/share/nginx/html/index.html</br>

<br>5. Check that the nginx page has been updated (localhost:80)</br>
<br>repartir sur le lien http://localhost:80</br>
<br>6. Create a transitive image named `my_awsome_image`</br>
  <br> $ docker commit mynginx1 my_awesome_image</br>
    <br>  sha256:6e9444f8a9858d2f16521a007486af35a058a0ac900893594833440c3dccf390</br>
<br>7. Run the new image</br>
<br>docker run --name myawesomecontainer -d -p 8o:80 my_awesome_image</br>

<br>8. Check that the modifications are still present (localhost:80)</br>
<br>on ne peux pas créer sur le même port que Nginx car cela créer un conflit</br>

<br>9. Check the layer with the `docker history` command</br>
<br>docker history my_awesome_image</br>

### Upload our image

<br>1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0`</br>
<br>docker tag my_awesome_image kinsley94/my_awesome_image:1.0</br>

<br>2. List your docker images</br>
<br>docker images</br>
 <br>  1. What do you see ?</br>
 <br>  je voie l'image que j'ai créer </br>
<br>3. Use the CLI to log into your docker account</br>
  <br> $ docker login</br>
  <br> Authenticating with existing credentials...</br>
  <br> Login Succeeded</br>

<br>4. Push your image</br>
<br>docker push kinsley94/my_awesome_image:1.0</br>


<br>5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`</br>
<br>https://hub.docker.com/repository/docker/kinsley94/my_awesome_image/</br>
<br>6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`</br>
<br>https://hub.docker.com/repository/docker/kinsley94/my_awesome_image/settings</br>