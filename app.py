
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Smart AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Smart AI Chatbot")
st.caption("Your personal chatbot assistant")

# Connect to OpenAI using the key saved in Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Model name (if this gives an error, we can change it)
MODEL = "gpt-4o-mini"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Type your message here...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                result = client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful and friendly AI assistant."
                        }
                    ] + st.session_state.messages
                )
            response = result.choices[0].message.content
        except Exception as e:
            response = "Sorry, error vandhuduchu: " + str(e)

        st.write(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )