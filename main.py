import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

from app.ai import get_sky_response
from app.utility import get_location_from_ip

# Load environment variables
load_dotenv()

# Initialize Groq API client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)



def run_terminal_mode():
    location = get_location_from_ip()
    print("Welcome to SKY - AI Tutor")
    while True:
        user_question = input("Ask your question: ")
        if user_question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        sky_response = get_sky_response(user_question, location)
        print("Sky says:")
        print(sky_response)


if __name__ == "__main__":
    print()
