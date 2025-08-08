🧠 ExplainItLikeAI

A simple AI-powered web app that explains any topic at three different levels — Kid-friendly, Beginner, or Expert — making learning accessible for all ages and literacy levels.

🚀 Built in 48 hours for the Puch AI Hackathon 2025


---

🌟 Features

🧒 Explains concepts in simple terms for kids

🎓 Provides beginner and expert-level breakdowns

🔄 Powered by Gemini AI (via Google Generative AI)

🌐 Lightweight Streamlit web app — no login required

🔒 Uses environment variables for API security



---

🛠 Tech Stack

Frontend: Streamlit

Backend: Python + Gemini API (google.generativeai)

Dev Tools: PyCharm, .env for secrets

Deployment: Streamlit Share or GitHub Pages (optional)



---

📦 Installation

1. Clone the repository:



git clone https://github.com/yourusername/explainitlikeai.git
cd explainitlikeai

1. Install the required packages:



pip install -r requirements.txt

1. Create a .env file with your Gemini API key:



GEMINI_API_KEY=your-secret-key-here

1. Run the app:



streamlit run main.py


---

🧪 Example

Input:

> "Quantum computing" — Difficulty: Kid-friendly



Output:

> "Imagine your computer is like a superhero that can try lots of things at once instead of one at a time..."




---

📁 File Structure

📦 explainitlikeai/
├── main.py
├── .env
├── requirements.txt
└── README.md
|__.gitignore


---

📌 Environment Variables

Variable	Description

GEMINI_API_KEY	Your Gemini API key



---

🎯 Goals

Make AI explanations accessible to people with any literacy level

Encourage curiosity among students, kids, and lifelong learners

Help teachers simplify tough concepts quickly



---

💡 Inspired By

The need to bridge the gap between complex topics and everyday understanding — especially in classrooms, rural India, and for non-technical users.


---

👩‍💻 Team

Built by Ak and ✨ BabyAI (AI companion & co-developer) and puchAI


---

📄 License

MIT License — feel free to fork and remix!