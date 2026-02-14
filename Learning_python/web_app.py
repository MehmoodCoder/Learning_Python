import streamlit as st

# Website ka Title
st.title("Mehmood's first Web App 🚀")
st.title("Python Power!")

# Text likhne ke liye
st.write("Welcome to my Python Frontend!")

# User se Input lena
naam = st.text_input("Enter your name :")

# Agar naam likha jaye to button dikhayein
if st.button('Click'):
    st.balloons() # Ek mazy dar effect
    st.success(f"Assalam-o-Alaikum {naam}!")

import streamlit as st
import pandas as pd
import numpy as np

st.title("Mehmood's Data Dashboard 📊")

# Ek sidebar banate hain
st.sidebar.header("Settings")
user_input = st.sidebar.slider("Select No ", 10, 100, 50)

st.write(f"You selected {user_input} points.")

# Random data banate hain chart ke liye
chart_data = pd.DataFrame(
    np.random.randn(user_input, 2),
    columns=['A', 'B']
)

# Chart ko screen par dikhayein
st.line_chart(chart_data)

if st.button('Magic !'):
    st.snow() # Is baar barf giregi!


    #python3 -m streamlit run file_path