import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API Key
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Set up OpenAI API
openai.api_key = openai_api_key

# Function to generate Taylor Swift-like song lyrics
def generate_taylor_swift_lyrics(title):
    prompt = f"Generate lyrics for the song '{title}' in the style of Taylor Swift."
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Streamlit UI
st.title("AI Taylor Swift Song Generator")

title = st.text_input("Enter the title of the Taylor Swift song to generate lyrics:")

if st.button("Generate"):
    if title.strip() != "":
        generated_lyrics = generate_taylor_swift_lyrics(title)
        st.subheader(f"Generated Lyrics for '{title}':")
        st.write(generated_lyrics)
