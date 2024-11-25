import streamlit as st
import datetime
sample_date = st.date_input(
    'When is your birthday?',
    datetime.date(2019,7,6)
)

st.write("Your birthday date is :", sample_date)