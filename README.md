# SmartAgent – Multi-Turn AI Assistant with Tool Use

SmartAgent is an intelligent conversational assistant that can:
- Perform natural language math
- Summarize `.txt` and `.pdf` files (even scanned/image-based ones)
- Simulate web search results
- Use GPT-3.5 for fallback reasoning
- Maintain memory across a multi-turn chat session

Built with **Python, OpenAI API, Streamlit, and OCR**, SmartAgent is fully modular and production-ready for file-based LLM workflows.

---

## Features

- **Intent-based routing**: calculator, file reader, search, LLM
- **PDF support**: Text or scanned PDFs via OCR (Tesseract)
- **Multi-turn memory** with Streamlit session state
- **LLM fallback** using OpenAI GPT-3.5
- **Streamlit UI**: Chat-based with file upload support

---

## 📸 Demo

| Task                    | Example |
|-------------------------|---------|
| Math prompt             | `What is 12 * 4` |
| File summary (text)     | `Summarize this document` |
| OCR fallback (scanned)  | `What is this image-based PDF about?` |

> Screenshots and notebook available in `jupyter/screenshots/` and `SmartAgent_Report.ipynb`.

---

## Folder Structure
smartagent/
├── main.py # Streamlit app
├── agent.py # Core agent logic
├── memory.py # (optional) placeholder
├── tools/ # Calculator, File Reader, Search Stub
├── jupyter/ # Report + screenshots
│ └── SmartAgent_Report.ipynb
├── .env.example # Sample OpenAI key config
├── requirements.txt
└── README.md


---

## 🚀 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/SravyaNMedaramitla/Smart-Agent.git
cd Smart-Agent

# Create and activate virtual environment
python -m venv .venv
source .venv/Scripts/activate   # (Windows)
# or
source .venv/bin/activate       # (Mac/Linux)

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI key
cp .env.example .env
# then edit .env to include your OPENAI_API_KEY

# Run the app
streamlit run main.py

---
Built By
Sravya Medaramitla
Full-Stack & AI Developer
LinkedIn → www.linkedin.com/in/sravya-neha
--- 