import streamlit as st
import openai
import os

# Get OpenAI API Key
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Set up OpenAI API
openai.api_key = openai_api_key

st.title('Your AI Companion')
st.write('Tell me how you feel and I will give you companionship!')

# Function to interact with OpenAI API
def chat_with_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002", 
        prompt=prompt, 
        max_tokens=150
    )
    return response.choices[0].text.strip()

user_input = st.text_input("How do you feel today?:", "")

if st.button("Send"):
    if user_input.strip() != "":
        st.text_area("Companion:", chat_with_openai(user_input))