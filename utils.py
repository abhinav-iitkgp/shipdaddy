from openai import OpenAI
client = OpenAI()
import streamlit as st

def get_initial_message(systemContent):
    print(systemContent,"bye")
    messages=[
            {"role": "system", "content": systemContent}
        ]
    return messages

def get_chatgpt_response(messages, model="gpt-4-1106-preview"):
    print("model: ", model)
    response = client.chat.completions.create(
    temperature=0,
    model=model,
    messages=messages
    )
    return  response.choices[0].message

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages
