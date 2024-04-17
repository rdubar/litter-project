import streamlit as st
from openai import OpenAI
import os

st.title("Partick Litter Chatbot 🤖")

# Attempt to get the API key from Streamlit secrets or environment variable
api_key = st.secrets.get("openai", {}).get("openai_api_key", None) or os.getenv("OPENAI_API_KEY")

try:
    client = OpenAI(api_key=api_key)
except Exception as e:
    st.error(f"Sorry! The Chatbot is out of order.")
    st.stop()

seed_prompt = """
Hello, I'm the **PARTICK LITTER PAL**, your friendly neighborhood chatbot! 🌱✨

I can answer all your questions about keeping Partick clean and litter-free. Whether you need tips on recycling, want to know about local clean-up events, or just curious about how you can help make Partick a dearer, cleaner place, just type away! 🍃🗑️

You can also ask me about local wildlife, nature, history, or anything else you're curious about. I'm here to help! 🐦🌳

Let's make Partick sparkle together! 💬🌟
"""

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4-turbo"

if "messages" not in st.session_state:
    if seed_prompt:
        st.session_state["messages"] = [{"role": "system", "content": seed_prompt}]
    else:
        st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What's your question?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
    