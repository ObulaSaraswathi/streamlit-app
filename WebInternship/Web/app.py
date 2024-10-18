import openai
import streamlit as st
import os

# You can set the key via environment variables or directly in the code (not recommended for security reasons)
api_key = '22ec84421ec24230a3638d1b51e3a7dc'
endpoint_url = 'https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview'

# Set up the OpenAI API with the API key
openai.api_key = api_key
openai.api_base = endpoint_url
# Streamlit Title
st.title("Azure OpenAI Chatbot")

# User input text box
user_input = st.text_input("Enter your question:", "")

# Button to submit input
if st.button("Submit"):
    if user_input:
        try:
            # Make an API call to OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )

            # Extract the assistant's reply
            assistant_response = response['choices'][0]['message']['content']

            # Display the assistant's reply
            st.write("Response: ", assistant_response)
        except Exception as e:
            st.write(f"An error occurred: {str(e)}")
    else:
        st.write("Please enter a valid question.")
