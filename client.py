import requests
import streamlit as st

def get_groq_response(input_text, language="French"):
    json_body = {
        "input": {
            "language": language,
            "text": input_text
        }
    }
    try:
        response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()['output']
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Streamlit app
st.title("LLM Application Using LCEL")
language = st.text_input("Select Target Language")
input_text = st.text_input("Enter the text you want to translate")


if st.button("Translate") and language and input_text:
    result = get_groq_response(input_text, language)
    st.write(f"Translated text: {result}")