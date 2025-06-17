# main.py

import streamlit as st
from agent import handle_prompt
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="SmartAgent", layout="wide")
st.title("🤖 SmartAgent – Multi-Turn AI Assistant")

# Session state to store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 👋 Show welcome message on first load
if not st.session_state.messages:
    st.info("👋 Welcome! Ask me a question or upload a file to get started.")

# File uploader
uploaded_file = st.file_uploader("Upload a file (.txt or .pdf)", type=["txt", "pdf"])
temp_path = None

# Save uploaded file temporarily
if uploaded_file:
    temp_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

# Input from user
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Agent response
    response = handle_prompt(user_input, file=temp_path)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display full chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
