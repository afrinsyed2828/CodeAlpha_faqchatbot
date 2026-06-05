import streamlit as st
import ollama

st.title("🤖 AI Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# New question box always appears at the bottom
prompt = st.chat_input("Ask a question...")

if prompt:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model="gemma3:4b",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            answer = response["message"]["content"]
            st.write(answer)

    # Save AI response
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )