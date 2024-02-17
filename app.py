import streamlit as st
import openai
import os
from dotenv import load_dotenv
import docx2txt

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API Key
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Set up OpenAI API
openai.api_key = openai_api_key

# Function to generate resume feedback
def generate_resume_feedback(resume_text):
    # Provide the resume text as input to the AI model
    prompt = f"This is a resume feedback bot. Please provide feedback on the following resume:\n\n{resume_text}\n\nFeedback:"
    response = openai.Completion.create(
        engine="davinci-codex", 
        prompt=prompt, 
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit UI
st.title("AI Resume Feedback Bot")

uploaded_file = st.file_uploader("Upload your resume (docx format)", type="docx")

if uploaded_file is not None:
    # Read the uploaded resume file
    resume_text = docx2txt.process(uploaded_file)
    
    # Generate feedback
    feedback = generate_resume_feedback(resume_text)
    
    # Display feedback
    st.subheader("Resume Feedback:")
    st.write(feedback)
