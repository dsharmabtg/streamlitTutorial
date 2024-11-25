import streamlit as st

video_file = open("D:\Lecture Videos\\Movies\\Srila Prabhupada - Your ever well wisher (Hindi).webm","rb")

video_bytes = video_file.read()

st.video(video_bytes)