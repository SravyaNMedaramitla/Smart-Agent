# agent.py

from tools.calculator import calculate
from tools.file_reader import read_file
from tools.search_stub import search_web
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env for API key
load_dotenv()
client = OpenAI()  # Automatically uses OPENAI_API_KEY from .env

def classify_prompt(prompt):
    prompt = prompt.lower()
    if any(word in prompt for word in ["calculate", "add", "subtract", "multiply", "divide"]):
        return "calculator"
    elif "read file" in prompt or "open file" in prompt:
        return "file_reader"
    elif "search" in prompt or "look up" in prompt:
        return "search"
    else:
        return "llm"

def handle_prompt(prompt, file=None):
    tool = classify_prompt(prompt)

    if tool == "calculator":
        return calculate(prompt)
    
    elif tool == "file_reader" and file:
        file_text = read_file(file)
        return query_llm(f"The user uploaded the following document:\n\n{file_text}\n\nNow answer this question: {prompt}")
    
    elif tool == "search":
        return search_web(prompt)
    
    elif file:
        file_text = read_file(file)
        return query_llm(f"Here is the uploaded file content:\n\n{file_text}\n\nNow answer this: {prompt}")

    else:
        return query_llm(prompt)


def query_llm(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are SmartAgent, a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"LLM Error: {str(e)}"
