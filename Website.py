import streamlit as st
import pandas as pd


st.title("Welcome to Knowledge Hub")

study_choice = st.selectbox("Enter Your Study Choice: " ,('Instrumentation' , 'CISCO' , 'Python' , 'Share Market' ))

#st.subheader("Instrumentation")
#st.subheader("CISCO")
#st.subheader("Python")
#st.subheader("Share Market")

#dataset = pd.read_csv("Share-Market.csv")
#st.dataframe(dataset)

name = st.text_input("Enter your name: ")
address = st.text_area("Enter your address: ")
gender = st.selectbox("Enter your gender: ",('M','F','Other'))
button = st.button("Done")

if button:
    st.markdown(f"Study Choice: {study_choice}")
    st.markdown(f"Name: {name}")
    st.markdown(f"Address: {address}")
    st.markdown(f"Gender: {gender}")

