# Examen 

Notre application est un moteur de recommendation d'Animés japonais, nos données proviennent de requêtes effectuées sur l'API Animelist.

## Test

Nous avons un volume **exam_database** auquel nous avons ajouté à la main les données "updated_animes_update_base.csv" à l'aide de la commande suivante : 

**Pour Windows** : 
docker run --rm -v exam_database:/app/data -v ${PWD}:/host busybox cp /host/dataset/updated_animes_update_base.csv /app/data/

**Pour MAC** :
docker run --rm -v exam_database:/app/data -v $(pwd):/host busybox cp /host/dataset/updated_animes_update_base.csv /app/data/

Pour lancer notre docker-compose et l'application : 
docker-compose up --build

