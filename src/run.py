from matplotlib.pyplot import subplots
import streamlit as st
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


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

# Metrics
st.metric('Total Users', '1,234', '5% increase')

# Statistics
with st.expander('Statistics'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.normal(size=100), ax=ax)
    st.pyplot(fig)
    
# User info
with st.expander('User Profile'):
    col1, col2 = st.columns(2)
    col1.text_input('Name:')
    col2.text_input('Email:')
    st.camera_input('Take a picture:')