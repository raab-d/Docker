from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from scipy.sparse import hstack
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Charger les données
def load_data():
    data = pd.read_csv('/app/data/updated_animes_update_base.csv')
    data['year'] = pd.to_numeric(data['year'], errors='coerce').fillna(0).astype(int)
    data['episodes'] = pd.to_numeric(data['episodes'], errors='coerce').fillna(0).astype(int)
    return data

# Nettoyage des données
anime_data = load_data()

def list_animes():
    # Extraire la liste des titres d'anime
    anime_list = anime_data['title'].tolist()
    return anime_list

# Prétraitement et calcul des caractéristiques
def preprocess_and_compute_features(data):
    selected_columns = ['title', 'synopsis', 'genres', 'year', 'producers', 'studios', 'themes']
    anime_features = data[selected_columns].copy()
    anime_features['synopsis'] = anime_features['synopsis'].fillna('')
    
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = tfidf_vectorizer.fit_transform(anime_features['synopsis'])
    
    genre_binarizer = MultiLabelBinarizer()
    theme_binarizer = MultiLabelBinarizer()

    genres_binary = genre_binarizer.fit_transform(anime_features['genres'].apply(ast.literal_eval))
    themes_binary = theme_binarizer.fit_transform(anime_features['themes'].apply(ast.literal_eval))

    feature_matrix = hstack([tfidf_matrix, genres_binary, themes_binary])
    return feature_matrix, tfidf_vectorizer, anime_data

feature_matrix, tfidf_vectorizer, anime_data = preprocess_and_compute_features(anime_data)

class RecommendationRequest(BaseModel):
    title: str
    num_recommendations: int

@app.post("/recommendations/")
def get_recommendations(request: RecommendationRequest):
    try:
        selected_anime = request.title
        num_recs = request.num_recommendations
        idx = anime_data.index[anime_data['title'] == selected_anime].tolist()[0]
        feature_matrix_csr = feature_matrix.tocsr()
        feature_idx = feature_matrix_csr[idx]
        cosine_similarities = cosine_similarity(feature_idx, feature_matrix_csr).flatten()
        similar_indices = np.argsort(-cosine_similarities)[1:num_recs+1]
        recommended_animes = anime_data.iloc[similar_indices]
        # Nettoyer les données avant de les renvoyer
        recommended_animes.replace([np.inf, -np.inf], np.nan, inplace=True)
        recommended_animes.fillna(0, inplace=True)  # Exemple de remplacement par 0
        return recommended_animes.to_dict('records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/animes")
def list_animes():
    # Extraire la liste des titres d'anime
    anime_list = anime_data['title'].tolist()
    return anime_list
