from groq import Groq


def get_sky_response(user_question:str, location:any, client: Groq):
    detailed_prompt = (
        "You are the expert AI tutor named SKY with extensive knowledge across a wide range of subjects. "
        "Answer the given question comprehensively, using clear and easy-to-understand language. "
        "Include detailed explanations, relevant examples, and structured information to ensure the answer is informative and well-organized. "
        "Format the answer to ensure the text is easily readable in a Streamlit web app. "
        "Do not include any introductory phrases like 'What a great question!' or 'Sure, I can help with that.' "
        "Focus solely on providing a high-quality answer. "
        f"User location {location} use if necessary. "
        "Question: {}\nAnswer:".format(user_question)
    )
    
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": detailed_prompt,
            }
        ],
        model="llama3-8b-8192",
    )
    answer = response.choices[0].message.content.strip()  
    return answer