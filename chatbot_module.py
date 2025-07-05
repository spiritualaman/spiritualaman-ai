from transformers import pipeline
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

def chat_response(text):
    return chatbot(text)[0]['generated_text']