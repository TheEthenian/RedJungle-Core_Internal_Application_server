from fastapi.middleware.cors import CORSMiddleware
from  fastapi import FastAPI
from pydantic import BaseModel
import sqlalchemy
import psycopg2
import requests 
import json


############### Micro-services addresses ##########################

orchestrator_services_url = 'http://redjungle-00.lab:7001'
review_services_url = 'http://redjungle-00.lab:7005'
auth_services_url = 'http://redjungle-00.lab:7010'
access_control_services_url = 'http://redjungle-00.lab:7020'
super_admin_services_url = 'http://redjungle-00.lab:7030'
admin_services_url = 'http://redjungle-00.lab:7040'
hotel_management_services_url = 'http://redjungle-00.lab:7050'
payment_gateway_services_url = 'http://redjungle-00.lab:7060'
booking_services_url = 'http://redjungle-00.lab:7070'
user_info_services_url = 'http://redjungle-00.lab:7080'
analytics_services_url = 'http://redjungle-00.lab:7090'
audit_logging_services_url = 'http://redjungle-00.lab:7095'

###################################################################


app = FastAPI()

origins = [
    "http://redjungle-00.lab:5090",  
    "http://localhost:5090",  
    "http://127.0.0.1:5090",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

###################################################################

@app.get("/")
def read_me():
    return  'black shirt manager' 


@app.get("/v2")
def read_me():
    reqested_data = requests.get(access_control_services_url)
    return reqested_data.json()


@app.get("/v1")
def read_me():
    reqested_data = requests.get(auth_services_url)
    return reqested_data.json()


@app.get("/v7")
def read_me():
    reqested_data = requests.get(booking_services_url)
    return reqested_data.json()


@app.get("/v5")
def read_me():
    reqested_data = requests.get(hotel_management_services_url)
    return reqested_data.json()


@app.get("/v3")
def read_me():
    reqested_data = requests.get(super_admin_services_url)
    return reqested_data.json()


@app.get("/v4")
def read_me():
    reqested_data = requests.get(admin_services_url)
    return reqested_data.json()


@app.get("/v8")
def read_me():
    reqested_data = requests.get(user_info_services_url)
    return reqested_data.json()


@app.get("/v9")
def read_me():
    reqested_data = requests.get(analytics_services_url)
    return reqested_data.json()


###################################################################

@app.post("/")
def avengers_assemble(something):
    data_list.append(something)
    return  {
        "msg": 'data sent succesfully',
        "data_pack": something
    } 


###################################################################

@app.put("/")
def avengers_assemble(new_instance):
    for item in data_list:
        if item['id'] == new_instance.id:
            item['name'] = new_instance.name
            return  {
                "msg": 'data block changed',
                "data_pack": item
            }


###################################################################

@app.delete("/")
def remove_avenger(uuid):
    item_id = uuid.id
    for item in data_list:
        if item['id'] == item_id:
            data_list.remove(item)
            return {
                "msg": "Item was succesfully deleted",
                "Item deleted": item
            }


#######################################################################


