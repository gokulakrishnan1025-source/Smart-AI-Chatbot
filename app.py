import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Ask Kira",
    page_icon="🤖",
    layout="centered"
)

# Light animated background
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        180deg,
        #050816,
        #111827,
        #263449,
        #080d1a
    );
    background-size: 400% 400%;
    animation: stormSky 12s ease infinite;
}

@keyframes stormSky {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    background: linear-gradient(
        115deg,
        transparent 45%,
        rgba(255,255,255,0.9) 49%,
        transparent 51%
    );
    opacity: 0;
    animation: lightningFlash 8s infinite;
}

@keyframes lightningFlash {
    0%, 88%, 91%, 100% { opacity: 0; }
    89% { opacity: 0.7; }
    90% { opacity: 0.05; }
}
</style>
""", unsafe_allow_html=True)


# Chatbot title (Branding: Ask Kira / Kira)
st.title("🤖 Ask Kira")
st.caption("Your smart question-answer assistant")
st.caption("Rule-based demo chatbot — predefined Q&A, not a live generative AI.")

# Predefined question and answer database (30 topics, 50+ question variations)
knowledge_base = {
    "python": {
        "keywords": ["python", "programming language", "what is python"],
        "answer": """**Python** is a popular programming language.

- Easy to learn and understand
- Used in Artificial Intelligence
- Used in Data Science
- Used in web development
- Supports automation"""
    },
    "artificial intelligence": {
        "keywords": ["artificial intelligence", "what is ai", "ai"],
        "answer": """**Artificial Intelligence (AI)** is a technology that enables computers to perform tasks that normally require human intelligence.

Examples:
- Chatbots
- Voice assistants
- Image recognition
- Recommendation systems"""
    },
    "machine learning": {
        "keywords": ["machine learning", "what is ml", "ml"],
        "answer": """**Machine Learning (ML)** is a branch of AI.

It allows computers to learn patterns from data and make predictions or decisions.

Examples:
- Email spam detection
- Movie recommendations
- Weather prediction"""
    },
    "deep learning": {
        "keywords": ["deep learning", "neural network", "what is deep learning"],
        "answer": """**Deep Learning** is a branch of Machine Learning that uses neural networks with many layers.

It is used for:
- Image recognition
- Speech recognition
- Language translation"""
    },
    "computer": {
        "keywords": ["computer", "what is computer"],
        "answer": """A **computer** is an electronic device that accepts data, processes it, stores it and produces information.

Main components:
- Input unit
- CPU
- Memory
- Output unit"""
    },
    "data science": {
        "keywords": ["data science", "data scientist"],
        "answer": """**Data Science** is a field that uses data, statistics and programming to find useful information and patterns.

It is used in business, healthcare, education and many other fields."""
    },
    "education": {
        "keywords": ["education", "importance of education"],
        "answer": """**Education** helps people gain knowledge, develop skills and improve their ability to solve problems.

It supports personal and professional growth."""
    },
    "science": {
        "keywords": ["science", "what is science"],
        "answer": """**Science** is the systematic study of the natural world through observation and experiments.

Main branches include Physics, Chemistry and Biology."""
    },
    "natural language processing": {
        "keywords": ["natural language processing", "nlp"],
        "answer": """**Natural Language Processing (NLP)** is a branch of AI that helps computers understand and respond to human language.

Examples: voice assistants, chatbots, language translation."""
    },
    "robotics": {
        "keywords": ["robotics", "robot"],
        "answer": """**Robotics** is a field that designs and builds robots that can perform tasks automatically.

Robots are used in factories, hospitals, space research and homes."""
    },
    "internet": {
        "keywords": ["internet", "what is internet"],
        "answer": """The **Internet** is a global network that connects millions of computers and devices.

It allows us to share information, communicate and use online services."""
    },
    "programming": {
        "keywords": ["programming", "coding", "what is programming"],
        "answer": """**Programming** is the process of writing instructions for a computer to perform tasks.

Programmers use languages like Python, Java and JavaScript."""
    },
    "software": {
        "keywords": ["software", "what is software"],
        "answer": """**Software** is a set of programs that tell a computer what to do.

Types:
- System software (example: operating system)
- Application software (example: browser, games)"""
    },
    "web development": {
        "keywords": ["web development", "website", "what is web development"],
        "answer": """**Web Development** is the process of building websites and web applications.

It uses HTML for structure, CSS for design and JavaScript for interaction."""
    },
    "database": {
        "keywords": ["database", "dbms", "sql"],
        "answer": """A **Database** is an organized collection of data that can be stored and searched easily.

Examples: MySQL, PostgreSQL, MongoDB."""
    },
    "cloud computing": {
        "keywords": ["cloud computing", "cloud", "what is cloud"],
        "answer": """**Cloud Computing** means using computing services like storage and servers over the internet.

Examples: Google Drive, AWS, Azure."""
    },
    "cybersecurity": {
        "keywords": ["cybersecurity", "cyber security", "hacking"],
        "answer": """**Cybersecurity** is the practice of protecting computers, networks and data from attacks and unauthorized access.

It includes firewalls, encryption and safe passwords."""
    },
    "big data": {
        "keywords": ["big data", "what is big data"],
        "answer": """**Big Data** refers to extremely large datasets that cannot be handled easily by traditional tools.

It is analyzed to find trends and patterns."""
    },
    "statistics": {
        "keywords": ["statistics", "what is statistics"],
        "answer": """**Statistics** is the science of collecting, analyzing and interpreting data.

It is widely used in Data Science and research."""
    },
    "mathematics": {
        "keywords": ["mathematics", "maths", "math"],
        "answer": """**Mathematics** is the study of numbers, shapes, patterns and logical reasoning.

It is the foundation of AI, Data Science and Engineering."""
    },
    "operating system": {
        "keywords": ["operating system", "os", "windows", "linux"],
        "answer": """An **Operating System (OS)** is system software that manages the computer's hardware and software.

Examples: Windows, Linux, Android."""
    },
    "javascript": {
        "keywords": ["javascript", "js"],
        "answer": """**JavaScript** is a programming language mainly used to make websites interactive.

It runs in every modern web browser."""
    },
    "html": {
        "keywords": ["html", "hypertext"],
        "answer": """**HTML** (HyperText Markup Language) is used to structure content on web pages.

It uses tags like <h1>, <p> and <img>."""
    },
    "css": {
        "keywords": ["css", "styling"],
        "answer": """**CSS** (Cascading Style Sheets) is used to design and style web pages.

It controls colours, fonts, layouts and animations."""
    },
    "iot": {
        "keywords": ["iot", "internet of things", "smart devices"],
        "answer": """**IoT (Internet of Things)** connects everyday devices to the internet so they can share data.

Examples: smart watches, smart home devices."""
    },
    "engineering": {
        "keywords": ["engineering", "engineer"],
        "answer": """**Engineering** is the application of science and mathematics to design and build useful products and systems.

Examples: software, bridges, machines, electrical systems."""
    },
    "technology": {
        "keywords": ["technology", "what is technology"],
        "answer": """**Technology** means tools and systems created using scientific knowledge to solve problems.

Examples: smartphones, computers, the internet."""
    },
    "smartphone": {
        "keywords": ["smartphone", "mobile phone"],
        "answer": """A **smartphone** is a mobile phone that can run apps, browse the internet, take photos and much more.

Examples: Android phones, iPhones."""
    },
    "career": {
        "keywords": ["career", "job", "future scope"],
        "answer": """AI and Data Science careers include:
- Data Scientist
- Machine Learning Engineer
- AI Researcher
- Data Analyst

These are in high demand today."""
    },
    "streamlit": {
        "keywords": ["streamlit", "what is streamlit"],
        "answer": """**Streamlit** is a Python library used to build interactive web applications quickly.

Ask Kira itself is built using Streamlit!"""
    },
}

# Suggested questions
suggestions = [
    "What is Python?",
    "What is AI?",
    "What is Machine Learning?",
    "What is Data Science?",
    "What is a Computer?",
]

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "page" not in st.session_state:
    st.session_state.page = "chat"
if "show_upgrade" not in st.session_state:
    st.session_state.show_upgrade = False
if "premium" not in st.session_state:
    st.session_state.premium = False

# Find chatbot response
def get_response(question):
    text = question.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! 👋 Welcome to **Ask Kira**. Ask me a question."

    if "your name" in text or "who are you" in text:
        return "I am **Kira**, a Python-based question-answer assistant. 🤖"

    if "who made you" in text or "who created you" in text or "developer" in text:
        return "I was developed as a college mini project using Python and Streamlit. 🎓"

    if "help" in text:
        return "Sure! Ask me about Python, AI, Machine Learning, Data Science, Computers, Science and more."

    if "time" in text:
        return "Current time: " + datetime.now().strftime("%I:%M %p")

    if "date" in text or "today" in text:
        return "Today's date: " + datetime.now().strftime("%d-%m-%Y")

    if any(word in text for word in ["thank you", "thanks"]):
        return "You're welcome! 😊"

    if any(word in text for word in ["bye", "goodbye"]):
        return "Goodbye! Have a great day. 👋"

    # Match predefined keywords
    for topic, details in knowledge_base.items():
        for keyword in details["keywords"]:
            if keyword in text.split():
                return details["answer"]

    return None  # Unknown question

# Initialize session state
if "messages" not in 
st.session_state:
    st.session_state.messages = []

if "premium" not in st.session_state:
    st.session_state.premium = False

if "show_upgrade" not in 
st.session_state:
    st.session_state.show_upgrade = False



# Send a message and handle the reply
def send_message(text):
    st.session_state.messages.append({"role": "user", "content": text})
    answer = get_response(text)

    if answer is None:
        # Unknown question -> credit finished message
        if st.session_state.premium:
            st.session_state.messages.append({
                "role": "assistant",
                "content": ("⭐ **Kira Premium is active!**\n\n"
                            "But I am still a rule-based chatbot, so I only "
                            "answer predefined topics. Try asking about Python, "
                            "AI, Machine Learning or Data Science.")
            })
        else:
            st.session_state.messages.append({
                "role": "assistant",
                "content": "Sorry, your credit finished. Upgrade Premium."
            })
            st.session_state.show_upgrade = True
    else:
        st.session_state.messages.append({"role": "assistant", "content": answer})

    st.rerun()

# ==================== PREMIUM PAGE ====================
if st.session_state.page == "premium":
    st.title("💎 Kira Premium")
    st.subheader("₹1,00,000")
    st.caption("Demonstration price only — no real payment is processed.")

    st.markdown(
        """
        **Premium Plan (Demo) includes:**
        - Unlimited questions
        - Priority responses
        - Future AI model integration when eligible API access is available
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        confirm = st.button("✅ Confirm", use_container_width=True)
    with col2:
        back = st.button("⬅️ Back", use_container_width=True)

    if confirm:
        st.session_state.premium = True
        st.session_state.messages = []        # return to initial chat screen
        st.session_state.show_upgrade = False
        st.success("Demo confirmed! Premium activated. (No payment was made — demonstration only.)")
        if st.button("⬅️ Back to Chat"):
            st.session_state.page = "chat"
            st.rerun()

    if back:
        st.session_state.page = "chat"        # return to previous conversation
        st.rerun()

# ==================== CHAT PAGE ====================
else:
    # Display previous messages (Reply shows as "Kira")
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown("**Kira**")
                st.markdown(message["content"])
        else:
            with st.chat_message("user"):
                st.markdown(message["content"])

    # Upgrade Premium button (shown only after an unknown question)
    if st.session_state.show_upgrade and not st.session_state.premium:
        if st.button("⬆️ Upgrade Premium"):
            st.session_state.page = "premium"
            st.rerun()

    # Suggested questions
    st.subheader("💡 Suggested Questions")
    cols = st.columns(2)
    for index, question in enumerate(suggestions):
        with cols[index % 2]:
            if st.button(question, key=f"suggestion_{index}"):
                send_message(question)

    # Voice-to-text input (works on mobile browsers)
    voice_text = None
    try:
        from streamlit_mic_recorder import speech_to_text
        voice_text = speech_to_text(
            key="kira_voice",
            language="en",
            start_prompt="🎤 Speak",
            stop_prompt="⏹ Stop"
        )
    except Exception:
        st.caption("🎤 Voice input needs the streamlit-mic-recorder package (see requirements.txt).")

    if voice_text:
        st.success(f"Voice detected: {voice_text}")
        send_message(voice_text)
    else:
        st.caption("Waiting for voice input...")

    # Text input
    user_question = st.chat_input("Ask Kira anything...")
    if user_question:
        send_message(user_question)

    # Clear chat button (Chat refresh)
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.show_upgrade = False
        st.rerun()

    # Footer
    st.divider()
    st.caption("Ask Kira | Developed using Python and Streamlit")



          

    