import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


arrr_data = np.random.normal(1,1,size=100)

fig,ax = plt.subplots()

ax.hist(arrr_data,bins=20)

st.pyplot(fig)