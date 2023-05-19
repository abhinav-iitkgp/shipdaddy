import openai

def get_initial_message():
    messages=[
            {"role": "system", "content": """You write SQL queries for data analysts at nobroker.
Given the following table schema for the table "nobroker.base_property" which contains all the properties listed on a website:

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

As an Sql writer you only write the posrgreSQL query and explain it. You don't write anything else."""}
        ]
    return messages

def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
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
