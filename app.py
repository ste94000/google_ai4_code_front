import streamlit as st
import os
import time
import io
import requests
import json

# Set the title and subheader of the app
st.title('Welcome to Notebook Organizer :orange_book:')
st.subheader('This app will sort your messy notebook')

# Create a file uploader widget
uploaded_nb = st.file_uploader("Upload a notebook to sort!", type=['ipynb'])
st.markdown('---')

if uploaded_nb is not None:
    st.subheader("I've never seen a notebook that clean :sunglasses:")

    api_url = 'https://googleai4code-ik6xds2r4a-ew.a.run.app/predict/'

    response = requests.get(api_url, files={'file': uploaded_nb})
    if response.status_code == 200:
        st.write('Success')
        prediction = response.json()
        st.write(prediction)


#st.subheader("I've never seen a notebook that clean ! :sunglasses:")

#with open('response_1719674261333.json', 'r', encoding='utf-8') as file:
#    data = json.load(file)
#
#for cell_type, content in zip(data['cell_type'].values(), data['source'].values()):
#    if cell_type == 'code':
#        st.code(content)
#    else:
#        st.markdown(content)
