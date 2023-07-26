# Movie Recommendation System

[Movie Recommendation](https://movie-recommendation-system-alidamt41f6.streamlit.app/)

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Cosine Similarity](#cosine-similarity)
- [Web App](#web-app)

  
## Introduction

The Movie Recommendation System using Cosine Similarity is a collaborative filtering-based application that suggests movies to users based on the director name, actor's name and genres. It utilizes two dataset containing user-movie director name, actor's name and genres to calculate the similarity between movies using cosine similarity. The system then recommends movies that are most similar to the ones the user has already watched.

This README provides an overview of the project, instructions for setting up the environment, guidelines for using the recommendation system.

## Dataset

The datasets used for building the movie recommendation system have contain movie title, director name, actor's name and genres.. Each row in the dataset represents movie title, director name, actor's name and genres for a specific movie. The datasets used for this recommendation system are in csv format, It can also be in JSON, or other tabular formats.

 The dataset have the following columns:

- `Movie title`
- `Director name`
- `Actors name`
-  `Genres`
- Dataset used for this model can be found on the following links:
  1. IMDB 5000 Movie Dataset[https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset]
  2. The Movie Dataset[https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset]

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Surendradhaka123/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

2. Set up a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use the Movie Recommendation System, follow these steps:

1. Ensure you have installed the required dependencies as mentioned in the [Installation](#installation) section.

2. If you are using our pretrained model then simply load the `MovieRecommendation_app.py` file, `movie_list.pkl` file and all `chunk` files and run the Streamlit app by using following command:
   ```python
   Streamlit run MovieRecommendation_app.py
   ```

4. If you want to train the model for your dataset then prepare your dataset in the required format.

5. Load the dataset and build the recommendation model:

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Assuming 'data' is a pandas DataFrame containing your dataset
cv = CountVectorizer(max_features=5364,stop_words='english')
vector = cv.fit_transform(new['comb']).toarray()

similarity = cosine_similarity(vector)

# Now we use the `TMDB` website api for getting the movies poster according to the movie i'd but first we get the movie i'd for the movie name.
from tmdbv3api import TMDb
import requests
from tmdbv3api import Movie
tmdb = TMDb()
tmdb.api_key = Your API KEY

#For getting movie i'd
tmdb_movie = Movie()
def get_movie_id(x):
    result = tmdb_movie.search(x)
    movie_id = result[0].id
    return movie_id

#For getting movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}".format(movie_id,tmdb.api_key)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

```

4. Get movie recommendations:

```python
def recommend(movie):
    index = movies[movies['movie_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[0:5]:
        # fetch the movie poster
        movie_name = movies.iloc[i[0]].movie_title
        recommended_movie_posters.append(fetch_poster(get_movie_id(movie_name)))
        recommended_movie_names.append(movies.iloc[i[0]].movie_title.title())

    return recommended_movie_names,recommended_movie_posters

recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
```

## Cosine Similarity

The movie recommendation system utilizes cosine similarity to calculate the similarity between movies. Cosine similarity measures the cosine of the angle between two non-zero vectors in an n-dimensional space. In the context of movie recommendation, each movie is represented as a vector based on director name, actor's name and genres, and cosine similarity is used to find movies with similar director name, actor's name and genres patterns.

## Web App

I have developed the web app for the `Recommendation System` using Streamlit and deployed it on the Streamlit Cloud.

Check- out  web app by following link: [WebApp](https://movie-recommendation-system-alidamt41f6.streamlit.app/)

---

We hope this README helps you understand the Movie Recommendation System using Cosine Similarity project. If you have any questions or need further assistance, please don't hesitate to reach out.

Enjoy great recommended movies!
