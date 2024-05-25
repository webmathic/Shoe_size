import pandas as pd
import numpy as np
import streamlit as st
import pickle
import streamlit.components.v1 as components

# Load the model
filename = 'best_model.pkl'
try:
    with open(filename, 'rb') as file:
        loaded_model = pickle.load(file)
except FileNotFoundError:
    st.error(f"The file {filename} was not found.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()


# Build a simple Streamlit app
st.set_page_config(layout="wide")
st.header('Shoe Size Predictor App')

# Custom HTML/CSS for the banner
custom_html = """
<div class="banner">
    <img src="https://img.freepik.com/premium-photo/wide-banner-with-many-random-square-hexagons-charcoal-dark-black-color_105589-1820.jpg" alt="Banner Image">
</div>
<style>
    .banner {
        width: 100%;
        height: 200px;
        overflow: hidden;
    }
    .banner img {
        width: 100%;
        object-fit: cover;
    }
</style>
"""
# Display the custom HTML
components.html(custom_html, height=200)

# Sidebar content
st.sidebar.subheader("Subheading")
st.sidebar.text("Sidebar content goes here.")

# Input fields
Height = st.number_input('Height', min_value=0.0, step=0.1)
st.write('The Height given is ', Height)

Weight = st.number_input('Weight', min_value=0.0, step=0.1)
st.write('The Weight given is ', Weight)

Gender = st.selectbox('Gender', ('Male', 'Female'))
st.write('You selected:', Gender)

# Predict button
predict_button = st.button("Predict")

if predict_button:
    # Encode Gender
    Gender = 1 if Gender == 'Male' else 2

    try:
        # Perform prediction
        result = loaded_model.predict([[Height, Weight, Gender]])
        st.write("The Predicted Shoe Size is {}".format(int(result[0])))
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

    # Feedback
    feedback = st.selectbox('Is our prediction Right or Wrong', ('Right', 'Wrong'))
    st.write('Feedback:', feedback)

st.write('Thank you for trying out our app!')
st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
