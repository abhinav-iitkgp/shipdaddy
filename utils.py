import openai
import streamlit as st

def get_initial_message(systemContent):
    print(systemContent,"bye")
    messages=[
            {"role": "system", "content": systemContent}
        ]
    return messages

def get_chatgpt_response(messages, model="gpt-4"):
    print("model: ", model)
    response = openai.ChatCompletion.create(
    temperature=0,
    model=model,
    messages=messages
    )
    return  response['choices'][0]['message']['content']

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages
