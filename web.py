import streamlit as st

from app.ai import get_sky_response
from app.utility import get_location_from_ip


st.set_page_config(page_title="SKY - AI Tutor", page_icon=":robot_face:", layout="wide")
    
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
        }
        .title {
            font-size: 36px;
            color: #4b4b4b;
        }
        .header {
            font-size: 24px;
            color: #4b4b4b;
        }
        .subheader {
            font-size: 20px;
            color: #4b4b4b;
        }
        .question-input {
            font-size: 18px;
        }
        .response {
            font-size: 18px;
            background-color: #ffffff;
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #e6e6e6;
            margin-top: 10px;
        }
        .chat-container {
            max-width: 800px;
            margin: auto;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">SKY - AI Tutor</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="header">Learn with the help of Sky</h2>', unsafe_allow_html=True)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

user_question = st.chat_input("Ask your question :")

if user_question:
    location = get_location_from_ip()
    sky_response = get_sky_response(user_question, location)
    st.session_state.chat_history.append({"user": user_question, "sky": sky_response})
    st.rerun()

if st.session_state.chat_history:
    for chat in st.session_state.chat_history:
        st.markdown(f'<div class="response"><strong>You:</strong> {chat["user"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="response"><strong>Sky:</strong> {chat["sky"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

