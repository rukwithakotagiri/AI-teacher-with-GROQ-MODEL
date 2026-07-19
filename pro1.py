#GEN AI- AI teacher with groq
import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Teacher",
    page_icon=":teacher:",
    layout="wide"
)
st.title("AI Teacher with GROQ MODEL")
#set Groq API key
API_KEY = "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"
#create the client for GROQ
Client = Groq(api_key=API_KEY)

#controller for the AI Teacher
Subject = st.sidebar.selectbox(
    "Choose the Subjects",
    ["ML","AI","Data Science","Python","Java","C++","web development","CYBER SECURITY","Cloud Computing","Networking","Database Management",
    "Mathematics", "Science", "History"]
)
#topic input
Topics = st.sidebar.text_input(
    "Topics",
    "Neural Networks"
)
#difficulty level
difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Beginner","Intermediate","Advanced"]
)
#prompt for the AI teacher
Prompt = f"""

You are an expert AI teacher.
Subject:
{Subject}
Topic:
{Topics}
Difficulty:
{difficulty}
Explain in simple language.
Then generate
-notes
-Examples
-practice questions
-MCQS
-coding exercises
-ouiz
-final summary
"""
#generate the button
if st.button("Generate Content"):
    with st.spinner("Generate Content"):
        prompt_data=[]
        prompt_data.append(
            {
                "role":"user",
                "content": Prompt
            }
        )
        prompt_data.append(
            {
                "role":"assistant",
                "content":"You are an expert AI Teacher and university professor."
            }
        )
        stream_response = Client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=1.0,
            max_tokens=4096,
            messages=prompt_data
        )
        response_data=stream_response.choices[0].message.content
        #Display the response
        st.markdown(response_data)