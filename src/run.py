import streamlit as st
import json

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

st.title(':zap: Test Dashboard')

with st.expander('Statistics'):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)
        
        data = json.loads(string_data)
        st.json(data)