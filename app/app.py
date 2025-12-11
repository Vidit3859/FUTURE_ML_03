import sys
import os

# Dynamically add project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

import streamlit as st
from utils.chatbot_engine import ChatbotEngine

# Load chatbot engine
chatbot = ChatbotEngine(
    vectorizer_path="./models/vectorizer.pkl",
    faq_data_path="./models/faq_data.pkl"
)

st.set_page_config(page_title="Customer Support Chatbot", page_icon="🤖")

st.title("Customer Support Chatbot 🤖")
st.write("Ask me anything related to *customer service*!")

user_input = st.text_area("Your Question")

if st.button("Get Answer"):
    if user_input.strip():
        response = chatbot.get_response(user_input)
        st.success(response)
    else:
        st.warning("Please type a question!")