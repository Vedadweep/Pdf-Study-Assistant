import streamlit as st
from pypdf import PdfReader
import requests
import os

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="PDF Study Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 PDF Study Assistant")
st.caption("Study Notes & Question Answering using Google Gemini 2.5 Flash")

# ================= API KEY =================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("❌ Please set GEMINI_API_KEY as an environment variable")
    st.stop()

API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"

# ================= PDF TEXT EXTRACTION =================
def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text.strip()

# ================= GEMINI CALL =================
def ask_gemini(context, user_input, mode):
    if mode == "Study Notes":
        instruction = """
Create well-structured study notes for exam preparation.

Rules:
- Use headings and bullet points
- Keep explanations concise but complete
- Only use information from the document
"""

    else:  # Question Answering
        instruction = """
Answer the question strictly using the document.
If the answer is not present, say:
"Answer not found in the document."
"""

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": f"""
You are a helpful academic assistant.

{instruction}

Document Content:
{context}

User Request:
{user_input}
"""
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 1200
        }
    }

    response = requests.post(
        f"{API_URL}?key={GEMINI_API_KEY}",
        json=payload,
        timeout=60
    )

    data = response.json()

    if "candidates" not in data:
        return f"❌ Gemini API Error:\n{data}"

    return data["candidates"][0]["content"]["parts"][0]["text"]

# ================= UI =================
uploaded_file = st.file_uploader("📤 Upload a PDF document", type=["pdf"])

if uploaded_file:
    with st.spinner("Processing PDF..."):
        pdf_text = extract_text(uploaded_file)

    if not pdf_text:
        st.error("❌ Could not extract text from the PDF.")
        st.stop()

    st.success("✅ PDF processed successfully")

    with st.expander("📄 View extracted text"):
        st.text_area("Extracted Text", pdf_text, height=300)

    st.markdown("## 🎯 Choose Mode")
    mode = st.selectbox(
        "Select what you want to do:",
        ["Question Answering", "Study Notes"]
    )

    user_input = st.text_input(
        "❓ Ask a question or request notes",
        placeholder="e.g. Explain this PDF for exam preparation"
    )

    if st.button("🚀 Generate"):
        with st.spinner("Generating response..."):
            output = ask_gemini(pdf_text, user_input, mode)

        st.markdown("## ✅ Output")
        st.markdown(output)
