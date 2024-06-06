import streamlit as st
from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

st.title("Sentiment Analysis App")
st.write("Enter text below to analyze its sentiment.")

# User input
user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    # Perform sentiment analysis
    if user_input:
        result = sentiment_analyzer(user_input)
        st.write("Sentiment:", result[0]['label'])
        st.write("Confidence:", result[0]['score'])
    else:
        st.write("Please enter some text to analyze.")
