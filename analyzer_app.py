import streamlit as st
from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment(user_text):
    if not user_text:
        return "Please enter some text."
    
    blob = TextBlob(user_text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        result = "Positive"
    elif polarity < 0:
        result = "Negative"
    else:
        result = "Neutral"
    
    return f"Sentiment: {result}\nPolarity: {polarity:.2f} | Subjectivity: {subjectivity:.2f}"

# --- Streamlit App UI ---
st.title("Text Sentiment Analyzer")

# Initialize session state variables if they don't exist
if 'result' not in st.session_state:
    st.session_state.result = ""
if 'user_text' not in st.session_state:
    st.session_state.user_text = ""

# Text area for input (using session state for persistent data)
user_text = st.text_area("Enter Text for Sentiment Analysis:", value=st.session_state.user_text, height=150)

# Save the user input to session state so it's available across reruns
st.session_state.user_text = user_text

# Analyze Button
if st.button("Analyze"):
    st.session_state.result = analyze_sentiment(st.session_state.user_text)

# Display the result
st.write(st.session_state.result)

# Clear Button (without rerun)
if st.button("Clear"):
    st.session_state.result = ""  # Clear the result
    st.session_state.user_text = ""  # Clear the text area
    # Simply resetting session state values is enough to clear the app state

