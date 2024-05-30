import streamlit as st
import time

# Title of the app
st.title("Student Information")

# input widget
text_username = st.text_input(label = "Name: ", value ="")

# slider widget
slider_age = st.slider(label = "Age: ")

# button
if st.button(label="Display information"):
    if text_username == "":
        st.error('No name enter', icon="🚨")
    else:
        with st.spinner(text='In progress'):
            time.sleep(3)
            st.success('Done')
        text = st.caption(f"{text_username} est agé de {slider_age} ans")
        
