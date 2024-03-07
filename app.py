import streamlit as st
import openai
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API Key
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Set up OpenAI API
openai.api_key = openai_api_key

# Function to generate Taylor Swift-like song lyrics asynchronously
async def generate_taylor_swift_lyrics(title):
    try:
        prompt = f"Generate Taylor Swift full lyrics for the song '{title}'"
        response = await openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=1000  # Reduced token count for faster response
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.error(f"Failed to generate lyrics due to: {e}")
        return ""

# Streamlit UI
st.title("AI Taylor Swift Song Generator")
st.write("Top 10 Taylor Swift Songs:", top_10_songs)

title = st.text_input("Enter the title of the Taylor Swift song to generate lyrics:")

if st.button("Generate"):
    if title.strip() != "":
        st.info("Generating lyrics... 🎵")
        # Call the function to generate lyrics and display result asynchronously
        with st.spinner('Wait for it...'):
            generated_lyrics = asyncio.run(generate_taylor_swift_lyrics(title))
            st.subheader(f"Generated Lyrics for '{title}':")
            st.write(generated_lyrics)
    else:
        st.warning("Please enter a song title.")
