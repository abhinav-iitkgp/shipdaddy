import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """   
Here's the database schema for the table "base_property":
Field Name: id
Field Type: Entity Key
Data Type: Text
Field Name: accurate_location
Field Type: Category
Data Type: Boolean
Field Name: activate_later
Field Type: Category
Data Type: Boolean
Field Name: activation_by
Field Type: Email
Data Type: Text
Field Name: activation_date
Field Type: No field type
Data Type: BigInteger
Field Name: activation_date_partitioned
Field Type: Quantity
Data Type: BigInteger
Field Name: active
Field Type: Category
Data Type: Boolean
Field Name: agent
Field Type: No field type
Data Type: Text
Field Name: available_from
Field Type: No field type
Data Type: BigInteger
Field Name: base_type
Field Type: Category
Data Type: Text
Field Name: bathroom
Field Type: Category
Data Type: Integer
Field Name: building_id
Field Type: No field type
Data Type: Text
Field Name: city
Field Type: City
Data Type: Text
Field Name: creation_date
Field Type: No field type
Data Type: BigInteger
Field Name: cup_board
Field Type: Category
Data Type: Integer
Field Name: event_time
Field Type: No field type
Data Type: Text
Field Name: facing
Field Type: Category
Data Type: Text
Field Name: floor
Field Type: No field type
Data Type: Integer
Field Name: furnishing
Field Type: Category
Data Type: Text
Field Name: future_activation_date
Field Type: No field type
Data Type: BigInteger
Field Name: gym
Field Type: Category
Data Type: Boolean
Field Name: inactive_reason
Field Type: Category
Data Type: Text
Field Name: last_activation_date
Field Type: No field type
Data Type: BigInteger
Field Name: last_update_date
Field Type: No field type
Data Type: BigInteger
Field Name: last_updated_by
Field Type: No field type
Data Type: Text
Field Name: latitude
Field Type: Latitude
Data Type: Float
Field Name: lease_type
Field Type: Category
Data Type: Text
Field Name: letout_date
Field Type: No field type
Data Type: BigInteger
Field Name: lift
Field Type: Category
Data Type: Boolean
Field Name: listing_score
Field Type: Category
Data Type: Text
Field Name: locality
Field Type: No field type
Data Type: Text
Field Name: locality_id
Field Type: No field type
Data Type: Text
Field Name: longitude
Field Type: Longitude
Data Type: Float
Field Name: managed
Field Type: Category
Data Type: Boolean
Field Name: nb_locality
Field Type: No field type
Data Type: Text
Field Name: negotiable
Field Type: Category
Data Type: Boolean
Field Name: owner_id
Field Type: Foreign Key
Data Type: Text
Field Name: parking
Field Type: Category
Data Type: Text
Field Name: pin_code
Field Type: No field type
Data Type: Integer
Field Name: power_backup
Field Type: Category
Data Type: Text
Field Name: property_age
Field Type: No field type
Data Type: Integer
Field Name: property_code
Field Type: Category
Data Type: Text
Field Name: property_size
Field Type: No field type
Data Type: BigInteger
Field Name: short_url
Field Type: URL
Data Type: Text
Field Name: society
Field Type: No field type
Data Type: Text
Field Name: sponsored
Field Type: Category
Data Type: Boolean
Field Name: starship_offset
Field Type: Score
Data Type: BigInteger
Field Name: state
Field Type: Category
Data Type: Text
Field Name: street
Field Type: No field type
Data Type: Text
Field Name: swimming_pool
Field Type: Category
Data Type: Boolean
Field Name: total_floor
Field Type: No field type
Data Type: Integer
Field Name: type
Field Type: Category
Data Type: Text
Field Name: water_supply
Field Type: Category
Data Type: Text
    
Write a PostgreSQL query for the following:
{question}
    
YOUR SQL QUERY:
"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=template,
)

def load_LLM():
    """Logic for loading the chain you want to use should go here."""
    # Make sure your openai_api_key is set as an environment variable
    llm = OpenAI(temperature=0.7, openai_api_key="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")
    return llm

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

if data_input:
    

    llm = load_LLM()

    prompt_with_question = prompt.format(question=data_input)

    sql_query = llm(prompt_with_question)

    st.write(sql_query)