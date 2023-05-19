import streamlit as st
# from langchain import PromptTemplate
# from langchain.llms import OpenAI
import os
from dotenv import load_dotenv
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

load_dotenv()
def promptMaker(question):
    return f"""   
    Given the following table schema for the table "base_property" which contains all the properties listed on a website:

    Field name         Data type
    --------------------------------
    id                  Text
    accurate_location    Boolean
    activate_later       Boolean
    activation_by        Text
    activation_date      BigInteger
    activation_date_partitioned  BigInteger
    active               Boolean
    agent                Text
    available_from       BigInteger
    base_type            Text
    bathroom             Integer
    building_id          Text
    city                 Text
    creation_date        BigInteger
    cup_board            Integer
    event_time           Text
    facing               Text
    floor                Integer
    furnishing           Text
    future_activation_date     BigInteger
    gym                  Boolean
    inactive_reason      Text
    last_activation_date BigInteger
    last_update_date     BigInteger
    last_updated_by      Text
    latitude             Float
    lease_type           Text
    letout_date          BigInteger
    lift                 Boolean
    listing_score        Text
    locality             Text
    locality_id          Text
    longitude            Float
    managed              Boolean
    nb_locality          Text
    negotiable           Boolean
    owner_id             Text
    parking              Text
    pin_code             Integer
    power_backup         Text
    property_age         Integer
    property_code        Text
    property_size        BigInteger
    short_url            Text
    society              Text
    sponsored            Boolean
    starship_offset      BigInteger
    state                Text
    street               Text
    swimming_pool        Boolean
    total_floor          Integer
    type                 Text
    water_supply         Text

    Write a PostgreSQL query for the question="{question}"

    YOUR SQL QUERY:

    """


# def load_LLM():
#     """Logic for loading the chain you want to use should go here."""
#     # Make sure your openai_api_key is set as an environment variable
#     llm = OpenAI(temperature=1, openai_api_key=os.environ["OPENAI_API_KEY"])
#     return llm

st.set_page_config(page_title="Ship Daddy", page_icon=":robot:")
st.header("SHIP DADDY V1")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Just Ask for the data you want about the properties table of Nobroker. This WebApp will create a custom sql query for you as per your request. Cheers:)")

with col2:
    st.image(image='shipdaddy_logo_500.png', width=500)

st.markdown("## What data do you want from property table?")


    

def get_text():
    input_text = st.text_area(label="JUST ASK ME", label_visibility='collapsed', placeholder="Ask for the data you want...", key="data_input")
    return input_text

data_input = get_text()


# def update_text_with_example():
#     print ("in updated")
#     st.session_state.email_input = "Select top 5 cities with the most listings in May 2023"

# st.button("*See An Example*", type='secondary', help="Click to see an example of the WebApp", on_click=update_text_with_example)

st.markdown("### Your SQL Query:")
sql_query=""
if data_input:
    prompt_with_question = promptMaker(question=data_input)
    sql_query = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt_with_question,
            temperature=1,
        )

st.write(sql_query)