from fastapi.middleware.cors import CORSMiddleware
from  fastapi import FastAPI
from models.orch_models import Data_Zero
from functions.main_function import load_yaml_config
from functions.main_function import workflow_complete_enumeration_order
import sqlalchemy
import psycopg2
import httpx 
import json



##################### CONFIG INFO ################################

config_general = load_yaml_config('../config_general.yaml')

base_url = config_general['api_network_base_url']

v1 = config_general['orchestration_service_port']
v2 = config_general['review_service_port']
v3 = config_general['auth_service_port']
v4 = config_general['access_control_service_port']
v5 = config_general['super_admin_service_port']
v6 = config_general['admin_service_port']
v7 = config_general['hotel_management_service_port']
v8 = config_general['payment_gateway_service_port']
v9 = config_general['booking_service_port']
v10 = config_general['user_info_service_port']
v11 = config_general['analytics_service_port']
v12 = config_general['audit_logging_service_port']


############### Micro-services full addresses #####################

orchestrator_services_url = f'{base_url}:{v1}'
review_services_url = f'{base_url}:{v2}'
auth_services_url = f'{base_url}:{v3}'
access_control_services_url = f'{base_url}:{v4}'
super_admin_services_url = f'{base_url}:{v5}'
admin_services_url = f'{base_url}:{v6}'
hotel_management_services_url = f'{base_url}:{v7}'
payment_gateway_services_url = f'{base_url}:{v8}'
booking_services_url = f'{base_url}:{v9}'
user_info_services_url = f'{base_url}:{v10}'
analytics_services_url = f'{base_url}:{v11}'
audit_logging_services_url = f'{base_url}:{v12}'

#####################################################################


app = FastAPI()

origins = [
    f"{base_url}:5090", 
    "http://localhost:5090",  
    "http://127.0.0.1:5090"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

###################################################################

@app.post("/")
def main_function(incoming_data: Data_Zero):

    pass



#######################################################################


