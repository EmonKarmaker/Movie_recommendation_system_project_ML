import streamlit as st
import pickle
import pandas as pd
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


st.title('Movie Recommender System')
Selected_movie_name = st.selectbox(
"What to recommend?",
movies['title'].values)

if st.button("Recommend"):
    st.write("Why hello there")