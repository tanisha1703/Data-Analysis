import streamlit as st
import google.generativeai as genai


st.title("welcome to gemini chat")

genai.configure(api_key="AIzaSyA0FzQ-5w5oS3wlu5Agidv7GumIIe2VKq8")

text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat =model.start_chat(history=[])

response = chat.send_message(text) 
st.write(response.text)