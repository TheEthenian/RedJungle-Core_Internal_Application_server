from  fastapi import FastAPI
import sqlalchemy
import psycopg2
from fastapi.middleware.cors import CORSMiddleware
from functions.main_function import load_yaml_config
from models.orch_models import Incoming_Data
import json



##################### CONFIG INFO ################################
config_general = load_yaml_config('../config_general.yaml')
base_url = config_general['api_network_base_url']

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
def main_function(data: Incoming_Data):

    pass



#######################################################################


