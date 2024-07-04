import streamlit as st
import os
import time
import io
import requests
from fastapi import FastAPI, File, UploadFile

# Set the title and subheader of the app
st.title('Welcome to Notebook Organizer :orange_book:')
st.subheader('This app will sort your messy Jupyter notebook')

# Create a file uploader widget
uploaded_nb = st.file_uploader("Upload a notebook to sort!", type=['ipynb'])

st.markdown('---')
if uploaded_nb is not None:

    api_url = 'https://googleai4code-sk7vxxr4rq-ew.a.run.app/predict'

    content = uploaded_nb.read()

    with st.spinner('Cleaning your confusing notebook...'):
        response = requests.post(api_url, files={'notebook_file': content})
        nb = response.json()
        if response.status_code == 200:
            for cell_type, content in zip(nb['cell_type'].values(), nb['source'].values()):
                if cell_type == 'code':
                    st.code(content)
                else:
                    st.markdown(content)
        else:
            st.markdown("**Oops**, something went wrong 😓 Please try again.")
            st.write(response.status_code, response.content)
