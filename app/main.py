
import streamlit as st
import tempfile
import os

from src.ingest import ingest_pdf
from src.rag_pipeline import generate_answer

st.set_page_config(
    page_title="SmartSupport AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 SmartSupport AI")
st.caption("Intelligent RAG-Based Customer Support Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.sidebar.header("Upload Knowledge Base")

uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.sidebar.button("Process PDF"):

        temp_path = None

        try:
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as temp_file:

                temp_file.write(uploaded_file.getvalue())
                temp_path = temp_file.name

            with st.spinner("Processing document..."):
                count = ingest_pdf(temp_path)

            st.sidebar.success(
                f"Successfully indexed {count} chunks!"
            )

        except Exception as e:
            st.sidebar.error(str(e))

        finally:
            if temp_path and os.path.exists(temp_path):
                os.remove(temp_path)


st.subheader("Ask your question")

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("sources"):
            st.caption(
                "Sources: " + ", ".join(message["sources"])
            )


question = st.chat_input(
    "Ask something about your uploaded documents..."
)

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    try:
        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                result = generate_answer(question)

            st.markdown(result["answer"])

            st.caption(
                "Sources: " +
                ", ".join(result["sources"])
            )

        st.session_state.messages.append({
            "role": "assistant",
            "content": result["answer"],
            "sources": result["sources"]
        })

    except Exception as e:
        st.error(f"Error: {e}")
