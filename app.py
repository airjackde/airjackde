import streamlit as st
import time

st.set_page_config(page_title="AIRJACKDE AI", page_icon="🤖", layout="centered")

st.markdown("""
<style>
    .stChatMessage { border-radius: 15px; }
</style>
""", unsafe_allow_html=True)

st.title("🤖 AIRJACKDE AI")
st.caption("🚀 Your Personal AI Assistant - Built by Airjackde")

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm AIRJACKDE AI 👋\n\nHow can I help you today?"}
    ]

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Response - SMART LOGIC
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1)
            
            prompt_lower = prompt.lower()
            
            if "who are you" in prompt_lower or "your name" in prompt_lower:
                response = "I am **AIRJACKDE AI** 🤖, created by Airjackde in Kericho, Kenya! I'm your personal AI assistant."
            elif "hello" in prompt_lower or "hi" in prompt_lower or "hey" in prompt_lower:
                response = f"Hello there! 👋 Great to see you! How can I help you today?"
            elif "how are you" in prompt_lower:
                response = "I'm doing amazing! Thanks for asking 😊 I'm here and ready to help you with anything!"
            elif "what can you do" in prompt_lower:
                response = "I can help you with:\n\n✅ Answer questions\n✅ Write stories, captions, emails\n✅ Help with school/homework\n✅ Give ideas for business\n✅ Chat like a friend\n\nJust ask me!"
            elif "code" in prompt_lower or "python" in prompt_lower or "streamlit" in prompt_lower:
                response = "Yes! I can help with coding 💻\n\nSend me your code or error, I'll fix it for you. I know Python, Streamlit, HTML, JavaScript and more!"
            else:
                response = f"You asked: **'{prompt}'**\n\nThat's a great question! \n\nAs AIRJACKDE AI, I'm here to help you with that. Could you give me a little more details so I can give you the best answer?\n\n💡 *Tip: I'm getting smarter every day! Soon I'll be connected to real ChatGPT brain.*"

            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("**AIRJACKDE AI v2.0**")
    st.write("Built with ❤️ in Kenya")
    if st.button("Clear Chat 🗑️"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.write("Share your app:")
    st.code("fg3twu22dvv.streamlit.app")
