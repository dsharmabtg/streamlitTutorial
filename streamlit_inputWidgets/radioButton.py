import streamlit as st

genre = st.radio(
    "What is your favourite food item?",
    ("Rajma-Chawal","Kadi-Chawal","Aloo Tikki","Ice cream"),
    index=None
)

if genre == "Rajma-Chawal":
    st.write("Wait for a while, Rajma-Chawal is served soon")
elif genre == 'Kadi-Chawal':
    st.write("Wait for a while, Kadi-Chawal is served soon")
elif genre == "Aloo Tikki":
    st.write("Wait for a while, Aloo Tikki is served soon")
elif genre == "Ice cream":
    st.write("Wait for a while, Ice cream is served soon")
else:
    st.write("You have not select any option")