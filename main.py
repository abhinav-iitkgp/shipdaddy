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
    st.markdown("Just Ask for the data you want about the properties, users, property search, property view, interactions(CO), homeservice.base_lead, admin_search.nobroker_payment, property_event.activate_master, nobroker.user_interaction, homeservice.attribution_log_v1, admin_cold.attribution_log tables of Nobroker. This WebApp will create a custom sql query for you as per your request. If you dont get the desired output just tell it what's wrong, ShipDaddy will correct itself.\n\n Cheers:)")

with col2:
    st.image(image='shipdaddy_logo_500.png', width=400)

systemContent="""You write SQL queries for data analysts at nobroker.\n\nWhen a user comes on the nobroker.in webpage, they apply some filteres to search for properties. This gives them a list of properties according to their filters., this is called the list page. Wen they click on a property then the detail page of that property opens, this is called property detail page(property view). The contact owner button(interaction) for each property is present on the list page and detail page. A user can do contact owner from either page.
As an expert Sql writer you only write the (((PrestoSQL))) query for metabase databse and explain it. You don't write anything else.\n\n"""
activate_master = st.checkbox('property_event.activate_master')
attribution_log = st.checkbox('admin_cold.attribution_log')
attribution_log_v1 = st.checkbox('homeservice.attribution_log_v1')
user_interaction = st.checkbox('nobroker.user_interaction')
nobroker_payment = st.checkbox('admin_search.nobroker_payment')
base_lead = st.checkbox('homeservice.base_lead')
property_search = st.checkbox('insight_events.property_search')
property_contact = st.checkbox('insight_events.property_contact')
property_view = st.checkbox('insight_events.property_view')
user = st.checkbox('nobroker.user')
base_property = st.checkbox('nobroker.base_property')

schema_base_property="""Given the following table schema for the table "nobroker.base_property" which contains all the properties listed on a website:
CREATE TABLE nobroker.base_property (
id: TEXT,
accurate_location: BOOLEAN,
activate_later: BOOLEAN,
activation_by: TEXT,
activation_date: BIGINT,
activation_date_partitioned: BIGINT,
active: BOOLEAN,
agent: TEXT,
available_from: BIGINT,
base_type: TEXT,
bathroom: INTEGER,
building_id: TEXT,
city: TEXT,
creation_date: BIGINT,
cup_board: INTEGER,
event_time: TEXT,
facing: TEXT,
floor: INTEGER,
furnishing: TEXT,
future_activation_date: BIGINT,
gym: BOOLEAN,
inactive_reason: TEXT,
last_activation_date: BIGINT,
last_update_date: BIGINT,
last_updated_by: TEXT,
latitude: FLOAT,
lease_type: TEXT,
letout_date: BIGINT,
lift: BOOLEAN,
listing_score: TEXT,
locality: TEXT,
locality_id: TEXT,
longitude: FLOAT,
managed: BOOLEAN,
nb_locality: TEXT,
negotiable: BOOLEAN,
owner_id: TEXT,
parking: TEXT,
pin_code: INTEGER,
power_backup: TEXT,
property_age: INTEGER,
property_code: TEXT,
property_size: BIGINT,
short_url: TEXT,
society: TEXT,
sponsored: BOOLEAN,
starship_offset: BIGINT,
state: TEXT,
street: TEXT,
swimming_pool: BOOLEAN,
total_floor: INTEGER,
type: TEXT,
water_supply: TEXT
);"""

schema_user="""Given the following table schema for the table "nobroker.user" 
CREATE TABLE nobroker.user (
id: TEXT,
Entity Key: TEXT,
Entity Name: TEXT,
last_update_date: BIGINT,
allowed_buy_int: TEXT,
allowed_int: TEXT,
broker: BOOLEAN,
comments: TEXT,
corporate_account: BOOLEAN,
creation_date: BIGINT,
creation_date_partitioned: BIGINT,
disabled: BOOLEAN,
email: TEXT,
email_hash: TEXT,
email_verified: BOOLEAN,
event_time: TEXT,
forgot_password_token: TEXT,
image_url: TEXT,
last_updated_by: TEXT,
password: TEXT,
payment_date: BIGINT,
phone: TEXT,
starship_offset: BIGINT,
state: TEXT,
token_generation_date: BIGINT,
user_type: TEXT,
username: TEXT,
verified_by: TEXT,
verified_on: BIGINT
);"""

schema_property_view="""Given the following table schema for the table "insight_events.property_view" a new row is created when a property is viewed
CREATE TABLE insight_events.property_view (
id: TEXT,
Entity Key: TEXT,
anonymous: BOOLEAN,
attribution_content: TEXT,
attribution_campaign: TEXT,
attribution_ip_address: TEXT,
attribution_medium: TEXT,
attribution_referrer: TEXT,
attribution_source: TEXT,
created_on: BIGINT,
date: BIGINT,
date_partitioned: BIGINT,
device: TEXT,
device_id: TEXT,
doc_type: TEXT,
index: TEXT,
ip_address: TEXT,
iplocation_address: TEXT,
iplocation_city: TEXT,
iplocation_country_code: TEXT,
iplocation_country_name: TEXT,
iplocation_sub_division_code: TEXT,
iplocation_sub_division_name: TEXT,
nbfr: TEXT,
property_activated_on: BIGINT,
property_active: BOOLEAN,
property_agent: TEXT,
property_available_from: BIGINT,
property_building_id: TEXT,
property_building_type: TEXT,
property_city: TEXT,
property_commercial_property_type: TEXT,
property_created_on: BIGINT,
property_furnishing: TEXT,
property_id: TEXT,
property_lease_type: TEXT,
property_locality: TEXT,
property_locality_id: TEXT,
property_location: TEXT,
property_location_lat: FLOAT,
property_location_long: FLOAT,
property_owner_broker: BOOLEAN,
property_owner_created_on: BIGINT,
property_owner_email: TEXT,
property_owner_id: TEXT,
property_owner_name: TEXT,
property_owner_owner_plan: TEXT,
property_owner_phone: TEXT,
property_premium: BOOLEAN,
property_owner_plan: TEXT,
property_gender: TEXT,
property_photo_available: BOOLEAN,
property_state: TEXT,
property_photo_count: BIGINT,
property_inactive_reason: TEXT,
property_price: BIGINT,
property_property_type: TEXT,
property_shared_accomodation: BOOLEAN,
property_sponsored: BOOLEAN,
country: TEXT,
property_type: TEXT,
user_broker: BOOLEAN,
user_created_on: BIGINT,
user_email: TEXT,
spt_locality: TEXT,
user_id: TEXT,
user_agent: TEXT,
user_name: TEXT,
user_owner_plan: TEXT,
user_plan: TEXT
);"""

schema_property_contact="""Given the following table schema for the table "insight_events.property_contact" a new row is created when a user clicks on the contact owner button for a property. At nobroker we call this interaction.
CREATE TABLE insight_events.property_contact (
id: TEXT,
Entity Key: TEXT,
attribution_campaign: TEXT,
attribution_ip_address: TEXT,
attribution_medium: TEXT,
attribution_referrer: TEXT,
attribution_source: TEXT,
created_on: BIGINT,
date: BIGINT,
date_partitioned: BIGINT,
device: TEXT,
device_id: TEXT,
doc_type: TEXT,
index: TEXT,
ip_address: TEXT,
iplocation_address: TEXT,
iplocation_city: TEXT,
iplocation_country_code: TEXT,
iplocation_country_name: TEXT,
iplocation_sub_division_code: TEXT,
iplocation_sub_division_name: TEXT,
nbfr: TEXT,
property_activated_on: BIGINT,
property_active: BOOLEAN,
property_agent: TEXT,
property_available_from: BIGINT,
property_building_id: TEXT,
property_building_type: TEXT,
property_city: TEXT,
property_commercial_property_type: TEXT,
property_created_on: BIGINT,
property_furnishing: TEXT,
property_id: TEXT,
property_lease_type: TEXT,
property_locality: TEXT,
property_locality_id: TEXT,
property_location: TEXT,
property_location_lat: FLOAT,
property_location_long: FLOAT,
property_owner_broker: BOOLEAN,
property_owner_created_on: BIGINT,
property_owner_email: TEXT,
property_owner_id: TEXT,
property_owner_name: TEXT,
property_owner_owner_plan: TEXT,
property_owner_phone: TEXT,
property_gender: TEXT,
property_premium: BOOLEAN,
property_owner_plan: TEXT,
property_state: TEXT,
property_photo_available: BOOLEAN,
property_inactive_reason: TEXT,
property_photo_count: BIGINT,
property_price: BIGINT,
property_property_type: TEXT,
property_shared_accomodation: BOOLEAN,
property_sponsored: BOOLEAN,
property_type: TEXT,
sents: TEXT,
country: TEXT,
user_broker: BOOLEAN,
prop_card_position: BIGINT,
user_created_on: BIGINT,
user_email: TEXT,
spt_locality: TEXT,
user_id: TEXT,
user_agent: TEXT,
user_name: TEXT,
user_owner_plan: TEXT,
user_plan: TEXT
);"""

schema_property_search="""Given the following table schema for the table "insight_events.property_search" a new row is created when a user searches for properties.
CREATE TABLE insight_events.property_search (
id: TEXT,
Entity Key: TEXT,
anonymous: BOOLEAN,
attribution_content: TEXT,
attribution_campaign: TEXT,
attribution_ip_address: TEXT,
attribution_medium: TEXT,
attribution_source: TEXT,
city: City,
date: BIGINT,
date_partitioned: BIGINT,
device: TEXT,
device_id: TEXT,
doc_type: TEXT,
filter_accomodation_type: TEXT,
filter_age_of_property: TEXT,
filter_attached_bathroom: BOOLEAN,
filter_available_for: TEXT,
filter_bathroom: BIGINT,
filter_breakfast: BOOLEAN,
filter_building_id: TEXT,
filter_commercial_lift: BOOLEAN,
filter_commercial_parking: TEXT,
filter_commercial_power_back_up: BOOLEAN,
filter_commercial_property_type: TEXT,
filter_dinner: BOOLEAN,
filter_exclusive_property: BOOLEAN,
filter_furnishing: TEXT,
filter_gender: TEXT,
filter_gym: BOOLEAN,
filter_house_type: TEXT,
filter_include_near_by: BOOLEAN,
filter_lease: TEXT,
filter_lease_type: TEXT,
filter_lift: BOOLEAN,
filter_locality_type: TEXT,
filter_lunch: BOOLEAN,
filter_max_area: BIGINT,
filter_max_price: BIGINT,
filter_min_area: BIGINT,
filter_min_price: BIGINT,
filter_occupancy: TEXT,
filter_page: BIGINT,
filter_parking: TEXT,
filter_project_image_count: BIGINT,
filter_property_age: BIGINT,
filter_search_type: TEXT,
filter_shared_accomodation: BOOLEAN,
filter_shown_near_by: BOOLEAN,
filter_sponsored: BOOLEAN,
filter_floor: TEXT,
filter_swimmingpool: BOOLEAN,
filter_tenant_type: TEXT,
filter_traffic: BOOLEAN,
filter_travel_time: BIGINT,
filter_type: TEXT,
filter_with_photos: BOOLEAN,
index: TEXT,
ip_address: TEXT,
iplocation_address: TEXT,
iplocation_city: TEXT,
iplocation_country_code: State,
iplocation_country_name: TEXT,
iplocation_sub_division_code: TEXT,
iplocation_sub_division_name: TEXT,
locality_center: TEXT,
locality_center_lat: Latitude,
locality_center_long: Longitude,
locality_city: TEXT,
locality_id: TEXT,
locality_known: BOOLEAN,
locality_latitude: FLOAT,
locality_locality_name: TEXT,
locality_longitude: Longitude,
locality_sub_type: TEXT,
locality_type: TEXT,
locality_url_name: TEXT,
matched_count: BIGINT,
premium_filter_availability: TEXT,
premium_filter_availability_date: BIGINT,
premium_filter_fpref: BOOLEAN,
premium_filter_hide_already_seen: BOOLEAN,
premium_filter_gfloor: BOOLEAN,
premium_filter_max_area: BIGINT,
premium_filter_min_area: BIGINT,
premium_filter_property_age: TEXT,
premium_filter_security: BOOLEAN,
search_param: TEXT,
user_broker: BOOLEAN,
user_created_on: BIGINT,
user_email: TEXT,
country: Country,
user_id: TEXT,
nbfr: TEXT,
user_locality: TEXT,
user_name: TEXT,
user_owner_plan: Owner,
user_agent: TEXT,
user_plan: TEXT
);"""

schema_base_lead="""Given the following table schema for the table "homeservice.base_lead" a new row is created when a new homeservices lead is created.
CREATE TABLE homeservice.base_lead(
name: Text,
servicing_date: BigInteger,
address: Text,
assignee: Text,
assignee_email: Text,
check_list: Text,
city: Text,
closed_on: BigInteger,
comment: Text,
created_by: Text,
created_on: BigInteger,
email: Text,
event_time: Text,
expiry_date: BigInteger,
expiry_reason: Text,
extension_id: Text,
follow_up_date: BigInteger,
follow_up_reason: Text,
id: Text,
is_active_lead: Boolean,
is_distinct_lead: Boolean,
is_service_active_lead: Boolean,
is_service_distinct_lead: Boolean,
job_state: Text,
last_updated_by: Text,
last_updated_date: BigInteger,
last_updated_on: BigInteger,
lead_source: Text,
lead_type: Text,
phone: Text,
quotation_id: Text,
reopen_date: BigInteger,
requirement: Text,
service_partner_id: Text,
servicing_assignee: Text,
servicing_assignee_email: Text,
servicing_slot: Text,
servicing_state: Text,
servicing_sub_state: Text,
source: Text,
stage: Text,
starship_offset: BigInteger,
version: BigInteger,
state: Text,
sub_state: Text,
total_agent_talk_time: Integer,
user_id: Text,
user_state: Text
);"""


schema_nobroker_payment="""Given the following table schema for the table "admin_search.nobroker_payment" a new row is created when a user does a payment.
CREATE TABLE admin_search.nobroker_payment (
name: Text,
created_date: BigInteger,
amount: Float,
broker: Text,
campaign: Text,
city: Text,
city_r_a: Text,
city_sponsored_locality: Text,
city_sponsored_property: Text,
created_date_partitioned: BigInteger,
current_owner_plan_active: Text,
current_owner_plan_date: Text,
current_owner_plan_expired: Text,
current_owner_plan_plan_id: Text,
current_owner_plan_plan_name: Text,
current_plan_active: Text,
current_plan_broker: Text,
current_plan_campaign: Text,
current_plan_city: Text,
current_plan_current_plan: Text,
current_plan_date: Text,
current_plan_device: Text,
current_plan_expired: Text,
current_plan_interaction_sent_unique: BigInteger,
current_plan_interaction_total: BigInteger,
current_plan_interaction_total_unique: BigInteger,
current_plan_locality: Text,
current_plan_medium: Text,
current_plan_name: Text,
current_plan_plan_id: Text,
current_plan_plan_name: Text,
current_plan_source: Text,
current_plan_verified: Boolean,
customer_identifier: Text,
device: Text,
event_time: BigInteger,
explain: Boolean,
int_count: BigInteger,
is_nri_user: Boolean,
interaction_sent_unique: BigInteger,
interaction_total: BigInteger,
interaction_total_unique: BigInteger,
last_updated_date: BigInteger,
locality: Text,
nb_param_payment_params: Text,
medium: Text,
nb_param_redirect_required: Text,
nb_param_dashboard: Text,
nb_param_cblfb: Text,
nb_param_db: Text,
nb_param_email: Text,
nb_param_from: Text,
nb_param_ehttps: Text,
nb_param_medium: Text,
nb_param_payso: Text,
nri_user: Boolean,
nb_param_fzbvy: Text,
order_id: Text,
nb_param_https: Text,
payee_document_city: Text,
nb_param_lead_sub_state: Text,
payee_document_email: Text,
payee_document_identifier: Text,
payee_document_name: Text,
nb_param_wallet_claim_id: Text,
payee_document_phone: Text,
payee_document_user_id: Text,
payment_gateway: Text,
payment_mode: Text,
plan_identifier: Text,
refund_amount: BigInteger,
refund_date: BigInteger,
payment_error_msg: Text,
refund_reason: Text,
refund_reason_string: Text,
size: BigInteger,
sort_last_updated_date_order: Text,
source: Text,
starship_offset: BigInteger,
refund_id: Text,
status: Text,
tracking_id: BigInteger,
tracking_id_new: Text,
user_id: Text,
user_phone: Text,
verified: Boolean,
wallet_payment_document_amount: Float,
wallet_payment_document_claim_code: Text,
wallet_payment_document_claim_id: Text,
wallet_payment_document_payment_meta_data: Text,
wallet_payment_document_transaction_id: Text
);"""

schema_user_interaction="""Given the following table schema for the table "nobroker.user_interaction" a new row is created when a user tries to do a interaction( contact owner) and accordingly is the contact is sent to the user then send is made "y" other wise "n".
CREATE TABLE nobroker.user_interaction (
id: Text,
event_time: Text,
property_id: Text,
request_date: BigInteger,
request_date_partitioned: BigInteger,
sent: Text,
starship_offset: BigInteger,
user_id: Text
);"""

schema_attribution_log_v1="""Given the following table schema for the table "homeservice.attribution_log_v1" attribution of users of homeservices.
CREATE TABLE homeservice.attribution_log_v1 (
id: Text,
agent: Text,
campaign: Text,
creation_date: BigInteger,
creation_date_partitioned: BigInteger,
device: Text,
entity_identity_id: Text,
entity_type: Text,
event_time: Text,
gclid: Text,
ip_address: Text,
medium: Text,
nb_fr: Text,
referrer: Text,
source: Text,
starship_offset: BigInteger,
track_id: Text,
user_id: Text
);"""

schema_attribution_log="""Given the following table schema for the table "admin_cold.attribution_log" attribution for users of rent, buy, pg, commercial.
CREATE TABLE admin_cold.attribution_log (
agent: Text,
campaign: Text,
creation_date: Text,
creation_date_partitioned: BigInteger,
device: Text,
entity_identity_id: Text,
entity_type: Text,
ip_address: Text,
medium: Text,
source: Text,
track_id: Text,
user_id: Text
);"""

schema_activate_master="""Given the following table schema for the table "property_event.activate_master" a new row is created when a property is listed for rent, sale ie it gets activated. A already inactive property can become active after the tenant has left and the property owner decides to again activate the property.
CREATE TABLE property_event.activate_master (
id: Text,
_id: Text,
activation_type: Text,
actor: Text,
attribution_campaign: Text,
attribution_ip_address: Text,
attribution_medium: Text,
attribution_referrer: Text,
attribution_source: Text,
auto_activated: Boolean,
call_duration_to_owner: BigInteger,
calls_to_owner: BigInteger,
date: BigInteger,
date_partitioned: BigInteger,
device_id: Text,
force_activation: Boolean,
ip_address: Text,
last_agent_call_agent: Text,
last_agent_call_call_ringing_time: BigInteger,
last_agent_call_called_on: BigInteger,
last_agent_call_dispose: Text,
last_agent_call_first_dispose: Text,
last_agent_call_second_dispose: Text,
last_agent_call_talk_time: BigInteger,
last_agent_call_third_dispose: Text,
last_agent_call_total_call_time_sec: BigInteger,
property_activated_on: BigInteger,
property_active: Boolean,
property_agent: Text,
property_available_from: BigInteger,
property_building_id: Text,
property_building_type: Text,
property_city: Text,
property_commercial_property_type: Text,
property_created_on: BigInteger,
property_furnishing: Text,
property_id: Text,
property_lease_type: Text,
property_locality: Text,
property_locality_id: Text,
property_location: Text,
property_location_lat: Float,
property_location_long: Float,
property_owner_broker: Boolean,
property_owner_created_on: BigInteger,
property_owner_email: Text,
property_owner_id: Text,
property_owner_name: Text,
property_owner_owner_plan: Text,
property_owner_phone: Text,
property_gender: Text,
property_colour: Text,
property_owner_plan: Text,
property_premium: Boolean,
property_photo_available: Boolean,
property_state: Text,
property_photo_count: BigInteger,
property_inactive_reason: Text,
property_price: BigInteger,
property_property_type: Text,
property_shared_accomodation: Boolean,
property_sponsored: Boolean,
property_type: Text,
reactivation_requested_by: Text,
reactivation_requested_date: BigInteger,
reactivation_source: Text,
ready_by: Text,
ready_date: BigInteger,
user_agent: Text
);"""
if base_property:
    systemContent+=schema_base_property+"\n\n"
if user:
    systemContent+=schema_user+"\n\n"
if property_view:
    systemContent+=schema_property_view+"\n\n"
if property_contact:
    systemContent+=schema_property_contact+"\n\n"
if property_search:
    systemContent+=schema_property_search+"\n\n"
if base_lead:
    systemContent+=schema_base_lead+"\n\n"
if nobroker_payment:
    systemContent+=schema_nobroker_payment+"\n\n"
if user_interaction:
    systemContent+=schema_user_interaction+"\n\n"
if attribution_log_v1:
    systemContent+=schema_attribution_log_v1+"\n\n"
if attribution_log:
    systemContent+=schema_attribution_log+"\n\n"
if activate_master:
    systemContent+=schema_activate_master+"\n\n"





st.markdown("## Tipi-Tipi-Top What data do you want?")
# print(systemContent,"HELLO")
model = "gpt-3.5-turbo"

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# st.session_state["input"] = 

query = st.text_input("Ask Me: 🤗 ", key="input")




if query:
    st.session_state['messages'] = get_initial_message(systemContent)
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(messages, model)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)
    query = st.empty()
        


if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))

    with st.expander("Show Messages"):
        st.write(messages)
