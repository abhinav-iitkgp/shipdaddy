import streamlit as st
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
from dotenv import load_dotenv
load_dotenv()
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

st.set_page_config(page_title="Ship Daddy", page_icon=":robot:")
st.header("SHIP DADDY V3")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Just Ask for the data you want about the properties, users, property search, property view, interactions(CO) tables of Nobroker. This WebApp will create a custom sql query for you as per your request. If you dont get the desired output just tell it what's wrong, ShipDaddy will correct itself.\n\n Cheers:)")

with col2:
    st.image(image='shipdaddy_logo_500.png', width=400)

st.markdown("## Tipi-Tipi-Top What data do you want?")

model = "gpt-3.5-turbo"

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# st.session_state["input"] = 

query = st.text_input("Ask Me: 🤗 ", key="input")

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()


if query:
    
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(messages, model)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)
        


if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))

    with st.expander("Show Messages"):
        st.write(messages)
