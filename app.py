

import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Smart AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Chatbot title
st.title("🤖 Smart AI Chatbot")
st.caption("Your simple question-answer assistant")

# Predefined question and answer database
knowledge_base = {
    "python": {
        "keywords": ["python", "programming language"],
        "answer": """
        **Python** is a popular programming language.

        - Easy to learn and understand.
        - Used in Artificial Intelligence.
        - Used in Data Science.
        - Used in web development.
        - Supports automation.
        """
    },

    "artificial intelligence": {
        "keywords": ["artificial intelligence", "what is ai", "ai"],
        "answer": """
        **Artificial Intelligence (AI)** is a technology
        that enables computers to perform tasks that
        normally require human intelligence.

        Examples:
        - Chatbots
        - Voice assistants
        - Image recognition
        - Recommendation systems
        """
    },

    "machine learning": {
        "keywords": ["machine learning", "what is ml", "ml"],
        "answer": """
        **Machine Learning (ML)** is a branch of AI.

        It allows computers to learn patterns from data
        and make predictions or decisions.

        Examples:
        - Email spam detection
        - Movie recommendations
        - Weather prediction
        """
    },

    "computer": {
        "keywords": ["computer", "what is computer"],
        "answer": """
        A **computer** is an electronic device that
        accepts data, processes it, stores it and
        produces information.

        Main components:
        - Input unit
        - CPU
        - Memory
        - Output unit
        """
    },

    "data science": {
        "keywords": ["data science"],
        "answer": """
        **Data Science** is a field that uses data,
        statistics and programming to find useful
        information and patterns.

        It is used in business, healthcare,
        education and many other fields.
        """
    },

    "education": {
        "keywords": ["education", "importance of education"],
        "answer": """
        **Education** helps people gain knowledge,
        develop skills and improve their ability
        to solve problems.

        It supports personal and professional growth.
        """
    },

    "science": {
        "keywords": ["science"],
        "answer": """
        **Science** is the systematic study of the
        natural world through observation and experiments.

        Main branches include Physics, Chemistry
        and Biology.
        """
    }
}

# Suggested questions
suggestions = [
    "What is Python?",
    "What is AI?",
    "What is Machine Learning?",
    "What is Data Science?",
    "What is a Computer?"
]

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Find chatbot response
def get_response(question):
    text = question.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! 👋 Welcome to Smart AI Chatbot. Ask me a question."

    if "your name" in text or "who are you" in text:
        return "I am Smart AI Chatbot, a Python-based question-answer assistant."

    if "time" in text:
        return "Current time: " + datetime.now().strftime("%I:%M %p")

    if "date" in text or "today" in text:
        return "Today's date: " + datetime.now().strftime("%d-%m-%Y")

    if any(word in text for word in ["thank you", "thanks"]):
        return "You're welcome! 😊"

    if any(word in text for word in ["bye", "goodbye"]):
        return "Goodbye! Have a great day."

    # Match predefined keywords
    for topic, details in knowledge_base.items():
        for keyword in details["keywords"]:
            if keyword in text:
                return details["answer"]

    return (
        "Sorry! I don't have a predefined answer for this question yet. "
        "Please try asking about Python, AI, Machine Learning, "
        "Data Science, Computers, Education or Science."
    )

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Suggested questions
st.subheader("💡 Suggested Questions")

cols = st.columns(2)

for index, question in enumerate(suggestions):
    with cols[index % 2]:
        if st.button(question, key=f"suggestion_{index}"):
            st.session_state.messages.append(
                {"role": "user", "content": question}
            )

            answer = get_response(question)

            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

            st.rerun()

# User input
user_question = st.chat_input("Ask your question here...")

if user_question:
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    answer = get_response(user_question)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Footer
st.divider()
st.caption("Smart AI Chatbot | Developed using Python and Streamlit")
