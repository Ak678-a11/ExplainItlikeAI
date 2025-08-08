import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# -------------------
# Load environment variables
# -------------------
load_dotenv()  # Loads variables from .env file
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("🚫 Gemini API key not found. Please make sure it's set in the .env file as GEMINI_API_KEY.")
    st.stop()

# -------------------
# Configure Gemini
# -------------------
genai.configure(api_key=api_key)

# -------------------
# App Config
# -------------------
st.set_page_config(page_title="ExplainItLikeAI", page_icon="🧠")

# Branding
st.markdown("### 🚀 Built for the Puch AI Hackathon 2025 — Making AI Accessible for Everyone in India")
st.title("🧠 ExplainItLikeAI")
st.info("🔍 Turning complex ideas into simple explanations for all ages and levels.")
st.write("Explain any topic at different difficulty levels — for kids, beginners, or experts.")

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
            prompt = f"Explain the topic '{topic}' in a {difficulty.lower()} way."

            try:
                model = genai.GenerativeModel("gemini-pro")
                response = model.generate_content(prompt)
                explanation = response.text

                st.subheader("📝 Explanation:")
                st.write(explanation)
            except Exception as e:
                st.error(f"❌ Error: {e}")

# -------------------
# Footer
# -------------------
st.markdown("---")
st.caption("Built in 48 hours for Puch AI 🚀 | Making AI accessible for all ages & literacy levels")
