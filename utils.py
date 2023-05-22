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

Given the following table schema for the table "nobroker.user" 
Field name                   Data type
--------------------------------------
id                           Text
Entity Key                   Text
Entity Name                  Text
last_update_date             BigInteger
allowed_buy_int              Text
allowed_int                  Text
broker                       Boolean
comments                     Text
corporate_account            Boolean
creation_date                BigInteger
creation_date_partitioned    BigInteger
disabled                     Boolean
email                        Text
email_hash                   Text
email_verified               Boolean
event_time                   Text
forgot_password_token        Text
image_url                    Text
last_updated_by              Text
password                     Text
payment_date                 BigInteger
phone                        Text
starship_offset              BigInteger
state                        Text
token_generation_date        BigInteger
user_type                    Text
username                     Text
verified_by                  Text
verified_on                  BigInteger

Given the following table schema for the table "insight_events.property_view" a new row is created when a property is viewed
Field name                        Data type
----------------------------------------------
id                               Text
Entity Key                       Text
anonymous                        Boolean
attribution_content              Text
attribution_campaign             Text
attribution_ip_address           Text
attribution_medium               Text
attribution_referrer             Text
attribution_source               Text
created_on                       BigInteger
date                             BigInteger
date_partitioned                 BigInteger
device                           Text
device_id                        Text
doc_type                         Text
index                            Text
ip_address                       Text
iplocation_address               Text
iplocation_city                  Text
iplocation_country_code          Text
iplocation_country_name          Text
iplocation_sub_division_code     Text
iplocation_sub_division_name     Text
nbfr                             Text
property_activated_on            BigInteger
property_active                  Boolean
property_agent                   Text
property_available_from          BigInteger
property_building_id             Text
property_building_type           Text
property_city                    Text
property_commercial_property_type Text
property_created_on              BigInteger
property_furnishing              Text
property_id                      Text
property_lease_type              Text
property_locality                Text
property_locality_id             Text
property_location                Text
property_location_lat            Float
property_location_long           Float
property_owner_broker            Boolean
property_owner_created_on        BigInteger
property_owner_email             Text
property_owner_id                Text
property_owner_name              Text
property_owner_owner_plan        Text
property_owner_phone             Text
property_premium                 Boolean
property_owner_plan              Text
property_gender                  Text
property_photo_available         Boolean
property_state                   Text
property_photo_count             BigInteger
property_inactive_reason         Text
property_price                   BigInteger
property_property_type           Text
property_shared_accomodation     Boolean
property_sponsored               Boolean
country                          Text
property_type                    Text
user_broker                      Boolean
user_created_on                  BigInteger
user_email                       Text
spt_locality                     Text
user_id                          Text
user_agent                       Text
user_name                        Text
user_owner_plan                  Text
user_plan                        Text

Given the following table schema for the table "insight_events.property_contact" a new row is created when a user clicks on the contact owner button for a property. At nobroker we call this interaction.
Field name                        Data type
----------------------------------------------
id                               Text
Entity Key                       Text
attribution_campaign             Text
attribution_ip_address           Text
attribution_medium               Text
attribution_referrer             Text
attribution_source               Text
created_on                       BigInteger
date                             BigInteger
date_partitioned                 BigInteger
device                           Text
device_id                        Text
doc_type                         Text
index                            Text
ip_address                       Text
iplocation_address               Text
iplocation_city                  Text
iplocation_country_code          Text
iplocation_country_name          Text
iplocation_sub_division_code     Text
iplocation_sub_division_name     Text
nbfr                             Text
property_activated_on            BigInteger
property_active                  Boolean
property_agent                   Text
property_available_from          BigInteger
property_building_id             Text
property_building_type           Text
property_city                    Text
property_commercial_property_type Text
property_created_on              BigInteger
property_furnishing              Text
property_id                      Text
property_lease_type              Text
property_locality                Text
property_locality_id             Text
property_location                Text
property_location_lat            Float
property_location_long           Float
property_owner_broker            Boolean
property_owner_created_on        BigInteger
property_owner_email             Text
property_owner_id                Text
property_owner_name              Text
property_owner_owner_plan        Text
property_owner_phone             Text
property_gender                  Text
property_premium                 Boolean
property_owner_plan              Text
property_state                   Text
property_photo_available         Boolean
property_inactive_reason         Text
property_photo_count             BigInteger
property_price                   BigInteger
property_property_type           Text
property_shared_accomodation     Boolean
property_sponsored               Boolean
property_type                    Text
sents                            Text
country                          Text
user_broker                      Boolean
prop_card_position               BigInteger
user_created_on                  BigInteger
user_email                       Text
spt_locality                     Text
user_id                          Text
user_agent                       Text
user_name                        Text
user_owner_plan                  Text
user_plan                        Text

Given the following table schema for the table "insight_events.property_search" a new row is created when a user searches for properties.


Field name                               Data type
--------------------------------------------------------
id                                      Text
Entity Key                              Text
anonymous                               Boolean
attribution_content                     Text
attribution_campaign                    Text
attribution_ip_address                  Text
attribution_medium                      Text
attribution_source                      Text
city                                    City
date                                    BigInteger
date_partitioned                        BigInteger
device                                  Text
device_id                               Text
doc_type                                Text
filter_accomodation_type                Text
filter_age_of_property                  Text
filter_attached_bathroom                Boolean
filter_available_for                    Text
filter_bathroom                         BigInteger
filter_breakfast                        Boolean
filter_building_id                      Text
filter_commercial_lift                  Boolean
filter_commercial_parking               Text
filter_commercial_power_back_up         Boolean
filter_commercial_property_type         Text
filter_dinner                           Boolean
filter_exclusive_property               Boolean
filter_furnishing                       Text
filter_gender                           Text
filter_gym                              Boolean
filter_house_type                       Text
filter_include_near_by                  Boolean
filter_lease                            Text
filter_lease_type                       Text
filter_lift                             Boolean
filter_locality_type                    Text
filter_lunch                            Boolean
filter_max_area                         BigInteger
filter_max_price                        BigInteger
filter_min_area                         BigInteger
filter_min_price                        BigInteger
filter_occupancy                        Text
filter_page                             BigInteger
filter_parking                          Text
filter_project_image_count              BigInteger
filter_property_age                     BigInteger
filter_search_type                      Text
filter_shared_accomodation              Boolean
filter_shown_near_by                    Boolean
filter_sponsored                        Boolean
filter_floor                            Text
filter_swimmingpool                     Boolean
filter_tenant_type                      Text
filter_traffic                          Boolean
filter_travel_time                      BigInteger
filter_type                             Text
filter_with_photos                      Boolean
index                                   Text
ip_address                              Text
iplocation_address                      Text
iplocation_city                         Text
iplocation_country_code                 State
iplocation_country_name                 Text
iplocation_sub_division_code            Text
iplocation_sub_division_name            Text
locality_center                         Text
locality_center_lat                     Latitude
locality_center_long                    Longitude
locality_city                           Text
locality_id                             Text
locality_known                          Boolean
locality_latitude                       Float
locality_locality_name                   Text
locality_longitude                      Longitude
locality_sub_type                       Text
locality_type                           Text
locality_url_name                       Text
matched_count                           BigInteger
premium_filter_availability             Text
premium_filter_availability_date        BigInteger
premium_filter_fpref                    Boolean
premium_filter_hide_already_seen        Boolean
premium_filter_gfloor                   Boolean
premium_filter_max_area                 BigInteger
premium_filter_min_area                 BigInteger
premium_filter_property_age             Text
premium_filter_security                 Boolean
search_param                            Text
user_broker                             Boolean
user_created_on                         BigInteger
user_email                              Text
country                                 Country
user_id                                 Text
nbfr                                    Text
user_locality                           Text
user_name                               Text
user_owner_plan                         Owner
user_agent                              Text
user_plan                               Text

Given the following table schema for the table "insight_events.builder_lead_event" which contains all the builder properties details:

Field name                          Data type
---------------------------------------------------------
id                                  Text
assignee_crm_email                  Text
assignee_crm_user_id                Text
assignee_frm_email                  Text
assignee_frm_user_id                Text
building_api_enabled                Boolean
building_brochure_active            Boolean
building_builder_email              Text
building_builder_name               Text
building_builder_phone              Text
building_building_model             Text
building_city                       Text
building_created_by                 Text
building_created_on                 BigInteger
building_email                      Text
building_id                         Text
building_last_updated_by            Text
building_last_updated_on            BigInteger
building_locality                   Text
building_name                       Text
building_phone                      Text
building_priority                   Text
building_type                       Text
created_by                          Text
created_on                          BigInteger
created_on_partitioned              BigInteger
current_state                       Text
doc_type                            Text
feedback                            Text
follow_up_reason                    Text
follow_up_time                      BigInteger
frm_feedback                        Text
gender_preferred                    Text
hwc_state                           Text
index                               Text
last_updated_by                     Text
last_updated_on                     BigInteger
lead_assignee                       Text
lead_event_type                     Text
lead_id                             Text
meeting_type                        Text
nri                                 Boolean
old_hwc_state                       Text
old_state                           Text
old_sub_state                       Text
product_type                        Text
requirement_bhk                     Text
requirement_builder_notes           Text
requirement_city                    Text
requirement_max_budget               Float
requirement_min_budget               Float
requirement_rm_notes                 Text
requirement_selected_locality        Text
site_visit_time                     BigInteger
society_url                         Text
source                              Text
source_type                         Text
country                             Text
sub_state                           Text
user_broker                         Boolean
user_created_on                     BigInteger
user_email                          Text
user_id                             Text
user_name                           Text
user_owner_plan                     Text
user_plan                           Text

As an Sql writer you only write the PrestoSQL query for metabase databse and explain it. You don't write anything else."""}
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
