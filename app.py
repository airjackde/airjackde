import streamlit as st
from groq import Groq

st.set_page_config(page_title="AIRJACKDE AI", page_icon="🤖", layout="centered")

GROQ_API_KEY = "gsk_gDarz9iFpdI3EXIgBIQpWGdyb3FYaoDFJKrJczJSMY9IsNMPSn1s_"

client = Groq(api_key=GROQ_API_KEY)

st.title("🤖 AIRJACKDE AI")
st.caption("🚀 Your Personal AI Assistant - Real AI Connected - Built by Airjackde")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm AIRJACKDE AI 👋 Real AI is now connected!\n\nHow can I help you today?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=st.session_state.messages,
                    temperature=0.7,
                    max_tokens=1024,
                )
                response = completion.choices[0].message.content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Error: {e}")

with st.sidebar:
    st.header("AIRJACKDE AI v3.0 - REAL AI")
    if st.button("Clear Chat 🗑️"):
        st.session_state.messages = st.session_state.messages[:1]
        st.rerun()
