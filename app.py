import streamlit as st
from google import genai

# Page Config
st.set_page_config(
    page_title="Streamlit AI Chatbot",
    page_icon="🤖"
)

# Gemini Client
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

st.title("🤖 Streamlit AI Chatbot")

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input Box
prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            answer = response.text

            st.markdown(answer)

            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )