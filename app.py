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
    prompt = f"Generate Taylor Swift full lyrics for the song '{title}"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=2000
    )
    return response.choices[0].text.strip()

# List of Taylor Swift's top 10 songs
top_10_songs = [
    "Love Story",
    "You Belong with Me",
    "Blank Space",
    "Shake It Off",
    "I Knew You Were Trouble",
    "We Are Never Ever Getting Back Together",
    "Bad Blood",
    "Delicate",
    "Style",
    "Wildest Dreams"
]

# Streamlit UI
st.title("AI Taylor Swift Song Generator")
# Display top 10 songs
st.write("Top 10 Taylor Swift Songs:", top_10_songs)

title = st.text_input("Enter the title of the Taylor Swift song to generate lyrics:")

if st.button("Generate"):
    if title.strip() != "":
        st.info("Generating lyrics... 🎵")
        # Call the function to generate lyrics and display result
        generated_lyrics = generate_taylor_swift_lyrics(title)
        st.subheader(f"Generated Lyrics for '{title}':")
        st.write(generated_lyrics)
    else:
        st.warning("Please enter a song title.")
