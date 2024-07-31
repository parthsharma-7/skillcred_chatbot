from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv() 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

st.set_page_config(
    page_icon=":robot:",
    page_title="SkillCred Q&A Project",
    layout="wide",
)

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Sidebar for chat history
with st.sidebar:
    st.header("**Chat History**")
    for i in range(0, len(st.session_state['chat_history']), 2):
        st.markdown(f"**Question:** {st.session_state['chat_history'][i][1]}")
        if i+1 < len(st.session_state['chat_history']):
            st.markdown(f"**Answer:** {st.session_state['chat_history'][i+1][1]}")
        st.markdown("---")

# Main content
st.header("Gemini-Pro Q&A Project")

input = st.text_input("Input:")
submit = st.button("Ask the question")

if submit and input:
    st.subheader("The Response is")
    
    st.markdown(f"**Question:** {input}")
    
    response_placeholder = st.empty()
    full_response = ""
    
    # Get and display the response
    for chunk in get_gemini_response(input):
        full_response += chunk.text
        response_placeholder.markdown(f"**Answer:** {full_response}")
    
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("Question:", input))
    st.session_state['chat_history'].append(("Answer:", full_response))

    # rerun to update the sidebar
    st.rerun()
