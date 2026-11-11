
import streamlit as st
from src.rag_pipeline import rag_pipeline

# Page configuration
st.set_page_config(
    page_title="SmartSupport AI",
    page_icon="🤖",
    layout="centered"
)

# Application title
st.title("🤖 SmartSupport AI")
st.caption("AI-powered Customer Support Assistant")

st.write(
    "Hello! Welcome to SmartSupport AI. "
    "Ask me any customer support question."
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Sidebar
with st.sidebar:
    st.header("Settings")

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
question = st.chat_input("Ask your question here...")


if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("🤖 Finding your answer..."):

            try:
                answer = rag_pipeline(question)

                if not answer:
                    answer = "No relevant information found."

                st.markdown(answer)

            except Exception as e:

                st.error("Something went wrong!")

                # Display actual error for debugging
                st.exception(e)

                answer = "Unable to generate an answer. Please check the error."

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
