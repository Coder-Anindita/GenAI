from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

st.title("Research Chatbot")

# Topic selection
topic = st.selectbox(
    "Choose a topic",
    [
        "Artificial Intelligence",
        "Machine Learning",
        "Web Development",
        "Data Science",
        "Cyber Security",
        "Cloud Computing"
    ]
)

# Style selection
style = st.selectbox(
    "Choose the style",
    [
        "Professional",
        "Simple",
        "Technical",
        "Creative",
        "Educational"
    ]
)

# Output length selection
length = st.selectbox(
    "Choose output length",
    [
        "Short",
        "Medium",
        "Long",
        "Detailed"
    ]
)

# User's specific request
user_query = st.text_input("What do you want to know about this topic?")

template = PromptTemplate( template=""" You are a research assistant. Topic: {topic} Style: {style} Desired Output Length: {length} User's Question: {user_query} Generate a response according to the selected topic, style, and output length. """, input_variables=["topic", "style", "length", "user_query"] )
if st.button("Submit Query"): 
    prompt = template.invoke({ "topic": topic, "style": style, "length": length, "user_query": user_query }) 
    result = model.invoke(prompt) 
    st.subheader("Response") 
    st.write(result.content)
