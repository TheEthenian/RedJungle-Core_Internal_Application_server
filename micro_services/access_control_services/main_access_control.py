from  fastapi import FastAPI
from pydantic import BaseModel
import sqlalchemy
import psycopg2
import requests
import json

app = FastAPI()

data_list = [
    {
        'Authorization': True,
        'acccess_level': 3,
        'ttl_seconds': 35,
        'auth_servers': [
            {"server_1","xxyz4"},
            {"server_2","xsdfs"},
            {"server_3","sdfsde"}
        ]
    },
    {
        'access_token': 'sdfsodfnsdfsd',
        'acccess_level': 5,
        'ttl_seconds': 10,
        'auth_servers': [
            {"server_1","ddjndjd"},
            {"server_2","zlfmfk"},
            {"server_3","rujjk"}
        ]
    }
]

class Data_structure(BaseModel):
    access_token: str
    Authorization: bool = False
    acccess_level: int = 10
    ttl_seconds: int = 30
    auth_servers: list


@app.get("/")
def read_me():
    return data_list


@app.post("/")
def read_me():
    response = requests.post(target_url_ahs)
    return response.json()


@app.put("/")
def read_me():
    return 'Nothing to put here'

@app.delete("/")
def remove_avenger(uuid: Data_structure):
    item_id = uuid.access_token
    for item in data_list:
        if item['access_token'] == item_id:
            data_list.remove(item)
            return {
                "msg": "Item was succesfully deleted",
                "Item deleted": item
            }



