import streamlit as st
import openai
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API Key
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    st.error("OPENAI_API_KEY is not set in the environment variables.")
    st.stop()

# Set up OpenAI API
openai.api_key = openai_api_key

# List of top 10 Taylor Swift songs
top_10_songs = [
    "Cardigan",
    "Love Story",
    "Shake It Off",
    "Blank Space",
    "Wildest Dreams",
    "You Belong With Me",
    "All Too Well",
    "I Knew You Were Trouble",
    "Delicate",
    "Bad Blood"
]

# Function to generate Taylor Swift-like song lyrics
async def generate_taylor_swift_lyrics(title):
    prompt = f"Generate Taylor Swift song lyrics for the title '{title}'"
    prompt_length = len(prompt.split())  # Rough estimate of prompt token count
    max_completion_length = 4097 - prompt_length  # Adjusting for the model's token limit

    try:
        loop = asyncio.get_running_loop()
        response = await loop.run_in_executor(
            None,
            lambda: openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",  # Use the appropriate model
                prompt=prompt,
                max_tokens=min(1000, max_completion_length)  # Request fewer tokens if needed
            )
        )
        if response and response.choices:
            lyrics = response.choices[0].text.strip()
            st.text_area("Generated Lyrics:", lyrics, height=300)  # Display in a text area
            return lyrics
        else:
            st.error("No lyrics were generated.")
            return ""
    except Exception as e:
        st.error(f"Failed to generate lyrics due to: {e}")
        return ""

# Streamlit UI
st.title("AI Taylor Swift Song Generator")

# Print out the top 10 Taylor Swift songs
st.write("Top 10 Taylor Swift Songs:")
for song in top_10_songs:
    st.text(song)

title = st.text_input("Enter the title of the Taylor Swift song to generate lyrics:")

if st.button("Generate"):
    if title.strip():
        st.info(f"Generating lyrics for '{title}'... 🎵")
        asyncio.run(generate_taylor_swift_lyrics(title))
    else:
        st.warning("Please enter a song title.")
