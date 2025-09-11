from  fastapi import FastAPI
from pydantic import BaseModel
import sqlalchemy
import psycopg2
import requests 
import json


orchestrator_url = 'http://redjungle-00.lab:6010'

app = FastAPI()


data_list = [
    {
        "name": "Im batman",
        "id": 13
    },
    {
        "name": "Kryptonian",
        "id": 43
    },
    {
        "name": "Omniman",
        "id": 15
    },
    {
        "name": "Invinsible",
        "id": 12
    }
]

class Data_structure(BaseModel):
    name: str 
    id: int

@app.get("/")
def read_me():
    return data_list

@app.get("/key")
def read_me():
    reqested_data = requests.get(target_url_acs)
    return reqested_data.json()


@app.post("/")
def avengers_assemble(something: Data_structure):
    data_list.append(something)
    return  {
        "msg": 'data sent succesfully',
        "data_pack": something
    } 


@app.put("/")
def avengers_assemble(new_instance: Data_structure):
    for item in data_list:
        if item['id'] == new_instance.id:
            item['name'] = new_instance.name
            return  {
                "msg": 'data block changed',
                "data_pack": item
            }


@app.delete("/")
def remove_avenger(uuid: Data_structure):
    item_id = uuid.id
    for item in data_list:
        if item['id'] == item_id:
            data_list.remove(item)
            return {
                "msg": "Item was succesfully deleted",
                "Item deleted": item
            }


