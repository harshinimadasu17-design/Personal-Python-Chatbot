import streamlit as st
from chatbot import get_answer


# Page configuration
st.set_page_config(
    page_title="Personal Python Chatbot",

    layout="centered"
)


# Title
st.title("Personal Python Question-Answering Chatbot")

st.write(
    "Ask me questions about Python programming and "
    "I'll provide answers from my Python knowledge base."
)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
user_question = st.chat_input(
    "Ask a Python question..."
)


# Process user question
if user_question:

    # Display user question
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):
        st.markdown(user_question)


    # Generate chatbot answer
    answer = get_answer(user_question)

    # Display chatbot answer
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)


# Sidebar
with st.sidebar:

    st.header("About")

    st.write(
        "This chatbot answers Python programming "
        "questions using a predefined knowledge base."
    )

    st.subheader("Example Questions")

    st.write("• What is Python?")
    st.write("• What is a list?")
    st.write("• What is a tuple?")
    st.write("• What is a function?")
    st.write("• What is a for loop?")
    st.write("• What is a dictionary?")
    st.write("• What is exception handling?")

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()