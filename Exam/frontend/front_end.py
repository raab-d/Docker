import streamlit as st
import requests
import ast
import pandas as pd
import pandas as pd
# Configuration

BACKEND_URL = "http://backend:8000"


st.title('Anime Recommendation System')


# Sidebar pour les entrées utilisateur
with st.sidebar:
    st.header('User Inputs')
    # Faire une requête GET au backend pour récupérer la liste des animes
    response = requests.get(f"{BACKEND_URL}/animes")
    if response.status_code == 200:
        anime_list = response.json()  # Supposons que le backend renvoie directement une liste de titres
        selected_anime = st.selectbox("Select an Anime", anime_list)
    else:
        st.error("Failed to load the anime list.")
        selected_anime = None  # En cas d'échec de chargement, aucun anime n'est sélectionnable

    # Slider pour le nombre de recommandations souhaitées
    num_recommendations = st.slider("Number of Recommendations", min_value=1, max_value=10, value=5)


# Displaying recommendations with additional information
if st.button("Get Recommendations"):
    # Envoyer une requête POST au backend pour obtenir des recommandations
    data = {'title': selected_anime, 'num_recommendations': num_recommendations}
    response = requests.post(f"{BACKEND_URL}/recommendations/", json=data)
    
    if response.status_code == 200:
        recommendations = response.json()  # La réponse attendue est une liste de dictionnaires
        st.header("Anime Recommendations")
        for rec in recommendations:
            col1, col2, col3 = st.columns([3, 2, 2])  # Ajustement de la répartition des colonnes

            with col1:
                st.image(rec['image_url'], use_column_width=True)

            with col2:
                st.markdown("#### Titre")
                st.write(rec['title'])
                st.markdown('#### Genres')
                genres_list = ast.literal_eval(rec['genres'])
                genres_str = ', '.join(genres_list)
                st.write(genres_str)
                st.markdown('#### Thèmes')
                themes_list = ast.literal_eval(rec['themes'])
                themes_str = ', '.join(themes_list)
                st.write(themes_str)
                st.markdown('#### Statut')
                st.write(rec['status'])
                
            with col3:
                st.markdown("#### Score")
                st.write(rec['score'])
                st.markdown("#### Épisodes")
                st.write(rec['episodes'])
                st.markdown("#### Année")        
                st.write(rec['year'])
                st.markdown('#### Type')
                st.write(rec['type'])
                
            st.write("Synopsis:", rec['synopsis'])  # Affichage du synopsis en dessous des informations
            producers_list = ast.literal_eval(rec['producers'])
            producers_str = ', '.join(producers_list)
            st.write("Producers:", producers_str)  # Affichage des producteurs 

            st.markdown("#### Studios")
            studios_list = ast.literal_eval(rec['studios'])
            studios_str = ', '.join(studios_list)
            st.write(studios_str)

            # Traitement et affichage des thèmes
            theme_dict = ast.literal_eval(rec['theme'])
            openings = theme_dict.get('openings', [])
            endings = theme_dict.get('endings', [])
            openings_str = ', '.join(openings) if openings else 'Aucun'
            endings_str = ', '.join(endings) if endings else 'Aucun'
            st.markdown("#### Openings")
            st.write(openings_str)
            st.markdown("#### Endings")
            st.write(endings_str)

            st.write("---")  # Séparateur pour chaque recommandation
    else:
        st.error("Failed to get recommendations.")
