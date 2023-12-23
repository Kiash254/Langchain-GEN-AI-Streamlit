import streamlit as st
from decouple import config
import google.generativeai as genai

API_KEY = config('API_KEY')

with st.sidebar:
    "[View the source code](https://github.com/Kiash254/Langchain-GEN-AI-Streamlit/blob/main/stream.py)"

st.title("Agricultural Recommender System")
st.caption("🚀 Farmers Choice to get the fastest Solution")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello Mkulima 👋 Naeza Kusaidia Ajy(How can i help you) ? "}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    model = genai.GenerativeModel('gemini-pro', API_KEY)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = model.generate(prompt, max_tokens=150)  # Replace this line with the correct method to generate chat completions
    msg = response.choices[0].message.content  # This line might also need to be updated based on the response structure
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)