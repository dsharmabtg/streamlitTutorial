import streamlit as st

option = st.selectbox(
    'How would you  like to be contacted?',
    ('Email','Home phone','Mobile phone'),
    index=None
)


st.write('You selected:',option)