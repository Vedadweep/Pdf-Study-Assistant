# 📄 PDF Study Assistant (Notes & Q&A)

A modern **PDF-based study assistant** built using **Streamlit** and **Google Gemini 2.5 Flash**.  
It helps students and learners **generate structured notes** and **ask questions directly from PDFs**, making exam preparation faster and smarter.

---

## 🚀 Features

- 📤 Upload any PDF document
- 📝 Generate **concise, structured study notes**
- ❓ Ask **natural language questions** based strictly on the PDF content
- ⚡ Powered by **Google Gemini 2.5 Flash** (fast & cost-efficient)
- 🎯 Document-grounded answers (no hallucination)
- 🖥️ Clean and intuitive Streamlit UI

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit**
- **Google Gemini 2.5 Flash API**
- **PyPDF2**
- **dotenv**

---

## 📂 Project Structure
pdf-study-assistant/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

--

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here

## 📦 Installation
git clone https://github.com/Vedadweep/pdf-study-assistant.git
cd pdf-study-assistant
pip install -r requirements.txt

▶️ Run the App
streamlit run app.py

📸 App Capabilities

Upload lecture notes, textbooks, or PDFs

Generate exam-oriented notes

Ask questions like:

“Explain this chapter in simple terms”

“Summarize key points for revision”

“What are the important definitions?”

🎓 Use Cases

Exam preparation

Quick revision before tests

Understanding long PDFs faster

Self-study assistant
