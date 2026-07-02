import os
from dotenv import load_dotenv
from google import genai
import gradio as gr

# Load API Key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini Client
client = genai.Client(api_key=api_key)


def study_assistant(question):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are an AI Study Assistant.

Explain the following question in very simple language.
Give an example whenever possible.

Question:
{question}
"""
        )

        return response.text

    except Exception as e:
        return f"Error:\n{e}"


demo = gr.Interface(
    fn=study_assistant,

    inputs=gr.Textbox(
        lines=4,
        placeholder="Ask any programming or study-related question..."
    ),

    outputs=gr.Textbox(
        lines=12,
        label="AI Answer"
    ),

    title="📚 AI Study Assistant",

    description="Ask any programming or study question and get AI-generated explanations.",

    theme="soft"
)

demo.launch()