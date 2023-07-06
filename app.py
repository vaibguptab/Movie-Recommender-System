import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    # then we enter similarity array by the index of that movie
    distances = similarity[movie_index]
    # then we sort the similarity array for the movie and return 5 movies with highest similarity score
    movies_list = sorted(list(enumerate(similarity[0])), reverse=True, key=lambda x: x[1])[1:6]

    recommended = []
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)
    return recommended

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('simi.pkl' , 'rb'))

st.title('Movie Recommender System')

selected = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected)
    for i in recommendations:
        st.write(i)
