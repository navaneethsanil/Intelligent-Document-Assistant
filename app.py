import os
import time
import streamlit as st
import tempfile

from backend import upload_document, query_document

# ---------- Page Configuration ----------
st.set_page_config(page_title="📚 Intelligent Document Search", layout="centered")
st.markdown("<h1 style='text-align: center;'>📚 Intelligent Document Assistant</h1><br>", unsafe_allow_html=True)

# ---------- Session State Initialization ----------
# Initializes keys used across sessions
for key in ["page", "chat_history", "openai_api_key"]:
    if key not in st.session_state:
        st.session_state[key] = (
            None if key == "page" 
            else [] if key == "chat_history" 
            else ""
        )

# ---------- Page 1: API Key Entry and File Upload ----------
if st.session_state.page != "chat":
    st.subheader("🔐 Enter API Key")
    api_key_input = st.text_input("OpenAI API Key", type="password", value=st.session_state.openai_api_key)

    st.subheader("📄 Upload a Document")
    uploaded_file = st.file_uploader("Choose a document", type=["pdf", "docx"])

    if st.button("Submit and Go to Chat"):
        # Validate inputs
        if not api_key_input:
            st.error("❌ Please enter the OpenAI API Key.")
        elif not uploaded_file:
            st.error("❌ Please upload a document.")
        else:
            # Store API key
            st.session_state.openai_api_key = api_key_input

            try:
                # Save uploaded file temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                    tmp_file.write(uploaded_file.read())
                    tmp_path = tmp_file.name

                # Process document and add to vector store
                with st.spinner("🔄 Processing and uploading document..."):
                    upload_document(tmp_path, api_key_input)

                st.success("✅ Document uploaded to vector store successfully!")
                os.remove(tmp_path)  # Clean up temp file

                # Switch to chat interface
                st.session_state.page = "chat"
                st.rerun()

            except Exception as e:
                st.error(f"❌ Upload error: {str(e)}")

# ---------- Page 2: Chat Interface ----------
elif st.session_state.page == "chat":
    # Button to restart with a new document
    if st.button("🔄 Upload New Document"):
        st.session_state.page = None
        st.session_state.chat_history = []
        st.rerun()

    st.subheader("💬 Chat with the Document")

    # ---------- Custom Chat Bubble Styles ----------
    st.markdown("""
        <style>
            .chat-bubble {
                max-width: 75%;
                padding: 12px 16px;
                border-radius: 20px;
                margin: 8px 0;
                font-size: 16px;
                line-height: 1.5;
                display: inline-block;
            }
            .user-bubble {
                background-color: #1b1c26;
                text-align: right;
                float: right;
                clear: both;
                border-bottom-right-radius: 0;
            }
            .bot-bubble {
                background-color: #1b1c26;
                text-align: left;
                float: left;
                clear: both;
                border-bottom-left-radius: 0;
            }
        </style>
    """, unsafe_allow_html=True)

    # ---------- Display Chat History ----------
    for user_msg, bot_msg in st.session_state.chat_history:
        st.markdown(f'<div class="chat-bubble user-bubble">{user_msg}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-bubble bot-bubble">{bot_msg}</div>', unsafe_allow_html=True)

    # ---------- Chat Input Field ----------
    prompt = st.chat_input("Ask a question about the document...")
    if prompt:
        st.markdown(f'<div class="chat-bubble user-bubble">{prompt}</div>', unsafe_allow_html=True)
        try:
            with st.spinner("Generating..."):
                # Query document using backend
                response = query_document(api_key=st.session_state.openai_api_key, question=prompt)

                # Typing animation effect for bot's response
                typed_text = ""
                placeholder = st.empty()
                for char in response:
                    typed_text += char
                    placeholder.markdown(f'<div class="chat-bubble bot-bubble">{typed_text}</div>', unsafe_allow_html=True)
                    time.sleep(0.015)

                # Final bot response
                placeholder.markdown(f'<div class="chat-bubble bot-bubble">{response}</div>', unsafe_allow_html=True)

                # Update chat history (limit to last 5 messages)
                st.session_state.chat_history.append((prompt, response))
                if len(st.session_state.chat_history) > 5:
                    st.session_state.chat_history = st.session_state.chat_history[-5:]

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
