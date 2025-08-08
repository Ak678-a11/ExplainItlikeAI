import streamlit as st
import requests
from dotenv import load_dotenv
import os

# -------------------
# Load environment variables
# -------------------
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

# Check API key
if not HF_API_KEY:
    st.error("🚫 Hugging Face API key not found. Please set HF_API_KEY in your .env file.")
    st.stop()

# -------------------
# App Config
# -------------------
st.set_page_config(page_title="ExplainItLikeAI", page_icon="🧠")

# Branding
st.markdown("### 🚀 Built for the Puch AI Hackathon 2025 — Making AI Accessible for Everyone in India")
st.title("🧠 ExplainItLikeAI")
st.write("Explain any topic at different difficulty levels — for kids, beginners, or experts.")

# -------------------
# Hugging Face API Call Function
# -------------------
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}


def query_huggingface(prompt_text: str):
    payload = {"inputs": prompt_text}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        return f"❌ API Error: {response.status_code} - {response.text}"
    try:
        data = response.json()
        return data[0]['generated_text']
    except Exception as e:
        return f"⚠ Unexpected response format: {e}"


# -------------------
# User input
# -------------------
topic = st.text_input("Enter a topic:")
difficulty = st.selectbox("Select difficulty level:", ["Kid-friendly", "Beginner", "Expert"])

# -------------------
# Handle Explain Button
# -------------------
if st.button("Explain"):
    if topic.strip() == "":
        st.warning("⚠ Please enter a topic.")
    else:
        with st.spinner("🤖 Thinking..."):
            final_prompt = f"Explain the topic '{topic}' in a {difficulty.lower()} way."
            explanation = query_huggingface(final_prompt)
            st.subheader("📝 Explanation:")
            st.write(explanation)

# -------------------
# Footer
# -------------------
st.markdown("---")
st.caption(
    "Built in 48 hours for Puch AI 🚀 | Powered by Hugging Face | Making AI accessible for all ages & literacy levels")
