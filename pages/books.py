import streamlit as st
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

def recommend(user_input):
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    recommended_books=[]
    recommended_author=[]
    recommended_book_images=[]
    for i in data:
        recommended_books.append(i[0])
        recommended_author.append(i[1])
        recommended_book_images.append(i[2])
    return recommended_books,recommended_author,recommended_book_images


st.title('Book Recommender System')
option=st.selectbox('Name a book you want to see the likeness of?',pt.index.values)
if st.button('Recommend'):
    recommendations,author,posters=recommend(option)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.header(recommendations[0])
        st.header(author[0])
        st.image(posters[0])
    with col2:
        st.header(recommendations[1])
        st.header(author[1])
        st.image(posters[1])
    with col3:
        st.header(recommendations[2])
        st.header(author[2])
        st.image(posters[2])
    with col4:
        st.header(recommendations[3])
        st.header(author[3])
        st.image(posters[3])
    with col5:
        st.header(recommendations[4])
        st.header(author[4])
        st.image(posters[4])