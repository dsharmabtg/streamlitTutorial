import streamlit as st
import pandas as pd
import numpy as np


sample_text = "Some Text that will be downloaded!!!"

st.download_button('Download text',sample_text)

with open("C:\\Users\\Dell\\OneDrive\\Pictures\\DL_Applications.png","rb") as file:
    btn = st.download_button(
        label="Download Image",
        data= file,
        file_name="DL_Applications.png",
        mime="image/png"
    )

@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv().encode('utf-8')

sample_df = pd.read_csv("C:\\Users\\Dell\\Downloads\\dtm_file_7.csv")
csv = convert_df_to_csv(sample_df)

st.download_button(

    label="Download data as csv",
    data=csv,
    file_name="large_df.csv",
    mime="text/csv"
)