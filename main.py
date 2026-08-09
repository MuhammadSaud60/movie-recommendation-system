from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import pickle
import pandas as pd
from config import get_api
import bz2


app = FastAPI(
    title = "Movie Recommender"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


api_key = get_api()


# LOADING PREPROCESSED
try:
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)

    with bz2.BZ2File('similarity.pkl.bz2', 'rb') as f:
        similarity = pickle.load(f)
        

except FileNotFoundError:
    print('File not found.')


@app.get('/recommend/{movie}')
def recommended_function(movie):

    try:
        movie = movie.strip().title()


        matches_movie = movies[movies['title'] == movie]

                
        movie_index = matches_movie.index[0]

        
        distance = similarity[movie_index]
        movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]


        recomended_movies = []

        for i in movies_list:

            movie_id = movies.iloc[i[0]].id

            movie = movies.iloc[i[0]].title

            poster = fetch_poster(movie_id=movie_id)

            recomended_movies.append({"title": movie, "poster" : poster })

        print(recomended_movies)

        return recomended_movies

    except IndexError:
        raise HTTPException(status_code=404, detail='Movie not found. Please check your spelling.')



def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    try:
        response = requests.get(url)
        data = response.json()
       
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except Exception as e:
        print(f"Error fetching poster: {e}")
    
    # Fallback image if no poster is found
    return "https://via.placeholder.com/500x750?text=No+Poster"