import streamlit as st
from groq import Groq

st.set_page_config(page_title="AIRJACKDE AI", page_icon="🤖")
st.title("🤖 AIRJACKDE AI")
st.caption("🚀 Your Personal AI Assistant - Ready!")

GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ SECRET KEY NOT FOUND IN STREAMLIT!")
    st.info("Go to share.streamlit.io → Manage app → Settings → Secrets")
    st.code('GROQ_API_KEY = "gsk_your_key_here"')
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am AIRJACKDE AI. How can I help you today?"}
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
            resp = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.messages
            )
            ans = resp.choices[0].message.content
            st.markdown(ans)
            st.session_state.messages.append({"role": "assistant", "content": ans})
        except Exception as e:
            st.error(f"Error: {e}")
