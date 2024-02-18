# AI Taylor Swift Song Generator

This is a simple web application built with Streamlit that generates Taylor Swift song lyrics using OpenAI's GPT-3 language model.

## Usage

1. Clone the repository:

```
git clone https://github.com/your-username/ai-taylor-swift-song-generator.git
```

2. Navigate to the project directory:

```
cd ai-taylor-swift-song-generator
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Obtain your OpenAI API key from the [OpenAI website](https://openai.com).

5. Create a file named `.env` in the project directory and add your API key:

```
OPENAI_API_KEY=your-api-key-here
```

Replace `your-api-key-here` with your actual API key obtained from OpenAI.

6. Run the Streamlit app:

```
streamlit run app.py
```

7. Enter the title of a Taylor Swift song and click "Generate" to generate lyrics.

## Dependencies

- Streamlit
- OpenAI

## Website

Visit the deployed application at [https://ghea-techin510-lab6.azurewebsites.net/](https://ghea-techin510-lab6.azurewebsites.net/)

## Reflection
1. Always create your .gitignore before your .env file, otherwise your API KEY will be pushed to github
2. Check your prompt, try to make it as relevant as possible
3. If I have more time, I will consider refining the user interface to make it more intuitive and visually appealing. 

