import json

import streamlit as st
import ollama

MODEL = "llama3.1:8b"
SYSTEM_PROMPT = (
    "You are Movie Panthulu, a movie question-and-answer assistant. "
    "Answer questions about films, actors, directors, genres, and plots. "
    "Keep replies short and clear. "
    "If a question is not about movies, say you only answer movie questions."
)

st.set_page_config(page_title="Movie Panthulu")
st.title("Movie Panthulu")
st.caption("Ask a movie question. Answers come from a local Ollama model (llama3.1:8b).")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about a movie"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                response = ollama.chat(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        *st.session_state.messages,
                    ],
                )
            answer = response["message"]["content"]
        except Exception:
            st.error(
                "Could not reach Ollama. Start Ollama, then run: ollama pull llama3.1:8b"
            )
        else:
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})

history_json = json.dumps(st.session_state.messages, indent=2)
st.download_button(
    "Download history",
    data=history_json,
    file_name="chat_history.json",
    mime="application/json",
    disabled=not st.session_state.messages,
)
