from matplotlib.pyplot import subplots
import streamlit as st
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from db.models import BannedWord, Message, User

login_options = st.sidebar.radio('Login/Sign Up', ['Login', 'Sign Up'])


if login_options == 'Login':
    st.sidebar.write('Please enter your login credentials.')
    st.sidebar.text_input('Username:')
    st.sidebar.text_input('Password:', type='password')
    st.sidebar.button('Login')
else: 
    st.sidebar.write('Please enter your details to sign up.')
    st.sidebar.text_input('Username:')
    st.sidebar.text_input('Email:')
    st.sidebar.text_input('Password:', type='password')
    st.sidebar.button('Sign Up')

# Banner and title
st.image('data/banner.png')
st.title(':zap: Test Dashboard')



# Questions and Answers
with st.expander('Q / A'):
    query = st.text_input('Search:')
    
    # select top 10 from messages
    for msg in Message.objects.all().order_by('-date')[:100]:
        if not msg.text or msg.text[-1] not in '؟?':
            continue
        
        if query and query not in msg.text:
            continue
        col1, col2 = st.columns([1, 4])
        col1.write(f'**{msg.user.username}**')
        col2.write(msg.text)
        # col2.write(msg.text.replace(query, f'**{query}**'))
        # st.write(f"{msg.user.username:100} {msg.text}")
        
    col1, col2 = st.columns(2)
    col1.button('< Previous')
    col2.button('Next >')
