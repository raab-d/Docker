# Lab 2 - Your first docker images

## Create a transitive image

### Tips

- Use the `docker commit`

### Make our image

1. Run `nginx` image detached with param `-p 80:80` named `mynginx1` : docker run --name mynginx1 -d -p 80:80 nginx sleep infinity
2. Check that the nginx page (localhost:80)
3. Run a shell without stopping the Container : docker run -it --name mynginx1 -p 80:80 nginx /bin/sh
4. Update the file `/usr/share/nginx/html/index.html` in the container :
   - docker exec -it bd388db562c0 /bin/sh
   - nano /usr/share/nginx/html/index.html
5. Check that the nginx page has been updated (localhost:80)
6. Create a transitive image named `my_awsome_image` : docker commit mynginx1 my_awsome_image:1.0
7. Run the new image : docker run -it my_awsome_image sleep infinity
8. Check that the modifications are still present (localhost:80)
9. Check the layer with the `docker history` command : docker history my_awsome_image

### Upload our image

1. Tag your image with the tag `<dockerHubId>/my_awsome_image:1.0` : docker tag my_awsome_image:1.0 hugomonteiro21/my_awsome_image:1.0
2. List your docker images
   1. What do you see ? Ma nouvelle image avec le tag 1.0 qui a été créé
3. Use the CLI to log into your docker account : docker login
4. Push your image : docker push hugomonteiro21/my_awsome_image:1.0
5. Check that your image is available on `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/`
6. Delete the repository `https://hub.docker.com/repository/docker/<dockerHubId>/my_awsome_image/settings`