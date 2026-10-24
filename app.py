import streamlit as st

st.set_page_config(page_title="AIRJACKDE AI", page_icon="🤖")

st.title("🤖 AIRJACKDE AI App")
st.write("Welcome! Your AI app is LIVE!")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello {name}! Your app is working! 🎉")

prompt = st.chat_input("Ask me anything...")
if prompt:
    st.write(f"You asked: {prompt}")
    st.write("This is your AI response!")

st.balloons()
