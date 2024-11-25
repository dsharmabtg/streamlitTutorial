import streamlit as st
from PIL import Image


image = Image.open("C:\\Users\\Dell\\OneDrive\\Pictures\\DL_Applications.png")

st.image(image,caption="List of Deep learning applications")
