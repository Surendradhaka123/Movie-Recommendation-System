
import pickle
import streamlit as st
import requests
import numpy as np
import pandas as pd
from tmdbv3api import TMDb
import json
import requests
from tmdbv3api import Movie
tmdb = TMDb()
tmdb.api_key = st.secrets["key"]
suggestion = 0

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://www.vshsolutions.com/wp-content/uploads/2020/02/recommender-system-for-movie-recommendation.jpg");
background-size: cover;
}

[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
hide_menu_style = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility: hidden;}
</style>
"""
st . markdown (hide_menu_style ,unsafe_allow_html=True)

tmdb_movie = Movie()
def get_movie_id(x):
    result = tmdb_movie.search(x)
    movie_id = result[0].id
    return movie_id
    

split_files = ['chunk_1.pkl', 'chunk_2.pkl', 'chunk_3.pkl', 'chunk_4.pkl', 'chunk_5.pkl', 'chunk_6.pkl', 'chunk_7.pkl', 'chunk_8.pkl', 'chunk_9.pkl', 'chunk_10.pkl', 'chunk_11.pkl']  # Add the names of your split files here
# Combine split files
combined_data = []
for file_name in split_files:
    with open(file_name, 'rb') as file:
        chunk = pickle.load(file)
        combined_data.extend(chunk)
similarity = combined_data
movies = pickle.load(open('movie_list.pkl','rb'))

recommended_movie_names = ['spy kids','godzilla resurgence','the amazing spider-man 2','timeline']

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}".format(movie_id,tmdb.api_key)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['movie_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_name = movies.iloc[i[0]].movie_title
        recommended_movie_posters.append(fetch_poster(get_movie_id(movie_name)))
        recommended_movie_names.append(movies.iloc[i[0]].movie_title.title())

    return recommended_movie_names,recommended_movie_posters

st.title(':red[Movie Recommendation System]')
movie_list = movies['movie_title'].values
selected_movie = st.selectbox(":red[Type or select a movie from the dropdown]",movie_list)
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    suggestion =1
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        html_str = f"""
            <style>
            p.a {{
              font: bold {18}px Courier;
              color: cyan;
            }}
            </style>
            <p class="a">{recommended_movie_names[0]}</p>
            """
        st.markdown(html_str, unsafe_allow_html=True)
        st.image(recommended_movie_posters[0])
        
    with col2:
        html_str = f"""
            <style>
            p.a {{
              font: bold {18}px Courier;
              color: cyan;
            }}
            </style>
            <p class="a">{recommended_movie_names[1]}</p>
            """
        st.markdown(html_str, unsafe_allow_html=True)
        st.image(recommended_movie_posters[1])

    with col3:
        html_str = f"""
            <style>
            p.a {{
              font: bold {18}px Courier;
              color: cyan;
            }}
            </style>
            <p class="a">{recommended_movie_names[2]}</p>
            """
        st.markdown(html_str, unsafe_allow_html=True)
        st.image(recommended_movie_posters[2])
    with col4:
        html_str = f"""
            <style>
            p.a {{
              font: bold {18}px Courier;
              color: cyan;
            }}
            </style>
            <p class="a">{recommended_movie_names[3]}</p>
            """
        st.markdown(html_str, unsafe_allow_html=True)
        st.image(recommended_movie_posters[3])
    with col5:
        html_str = f"""
            <style>
            p.a {{
              font: bold {18}px Courier;
              color: cyan;
            }}
            </style>
            <p class="a">{recommended_movie_names[4]}</p>
            """
        st.markdown(html_str, unsafe_allow_html=True)
        st.image(recommended_movie_posters[4])


st.markdown(""" <style> .font {
font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;} 
</style> """, unsafe_allow_html=True)
st.markdown('<p class="font">You may also like</p>', unsafe_allow_html=True)


suggested_movie_name,suggested_movie_poster = recommend(recommended_movie_names[3].lower())

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    html_str = f"""
        <style>
        p.a {{
            font: bold {18}px Courier;
            color: cyan;
        }}
        </style>
        <p class="a">{suggested_movie_name[0]}</p>
        """
    st.markdown(html_str, unsafe_allow_html=True)
    st.image(suggested_movie_poster[0])
    
with col2:
    html_str = f"""
        <style>
        p.a {{
            font: bold {18}px Courier;
            color: cyan;
        }}
        </style>
        <p class="a">{suggested_movie_name[1]}</p>
        """
    st.markdown(html_str, unsafe_allow_html=True)
    st.image(suggested_movie_poster[1])

with col3:
    html_str = f"""
        <style>
        p.a {{
            font: bold {18}px Courier;
            color: cyan;
        }}
        </style>
        <p class="a">{suggested_movie_name[2]}</p>
        """
    st.markdown(html_str, unsafe_allow_html=True)
    st.image(suggested_movie_poster[2])
with col4:
    html_str = f"""
        <style>
        p.a {{
            font: bold {18}px Courier;
            color: cyan;
        }}
        </style>
        <p class="a">{suggested_movie_name[3]}</p>
        """
    st.markdown(html_str, unsafe_allow_html=True)
    st.image(suggested_movie_poster[3])
with col5:
    html_str = f"""
        <style>
        p.a {{
            font: bold {18}px Courier;
            color: cyan;
        }}
        </style>
        <p class="a">{suggested_movie_name[4]}</p>
        """
    st.markdown(html_str, unsafe_allow_html=True)
    st.image(suggested_movie_poster[4])








