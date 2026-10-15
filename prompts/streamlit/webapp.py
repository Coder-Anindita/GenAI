import streamlit as st

st.title("My First Streamlit App")



option = st.selectbox(
    "Choose a language",
    ["Python", "Java", "C++"]
)

file = st.file_uploader(
    "Upload a file",
    type=["pdf", "txt"]
)

if file:
    st.write(file.name)