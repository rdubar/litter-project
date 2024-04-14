from openai import OpenAI
import streamlit as st

st.title("Partick Litter Chatbot 🤖")

client = OpenAI(api_key=st.secrets["openai"]["openai_api_key"])

seed_prompt = """
Hello, I'm the **PARTICK LITTER PAL**, your friendly neighborhood chatbot! 🌱✨

I can answer all your questions about keeping Partick clean and litter-free. Whether you need tips on recycling, want to know about local clean-up events, or just curious about how you can help make Partick a dearer, cleaner place, just type away! 🍃🗑️

Let's make Partick sparkle together! 💬🌟
"""

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

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