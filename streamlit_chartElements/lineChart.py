import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["A","B","C"]
) 
st.line_chart(chart_data)

st.line_chart(chart_data,x="A",y="B")