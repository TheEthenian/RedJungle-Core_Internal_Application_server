from  fastapi import FastAPI
from models import hotel_mgnt_models as structure
import sqlalchemy
import psycopg2
import requests 
import json

#####################################################################

app = FastAPI()

#####################################################################

data_list = [
]

#####################################################################


@app.get("/")
def main_get():
    return data_list


@app.post("/")
def main_post(something: structure.Room_Object):
    data_list.append(something)
    return  {
        "msg": 'data sent succesfully',
        "data_pack": something
    } 


@app.put("/")
def main_put(new_instance: structure.Room_Object):
    for item in data_list:
        if item['id'] == new_instance.id:
            item['name'] = new_instance.name
            return  {
                "msg": 'data block changed',
                "data_pack": item
            }


@app.delete("/")
def main_delete(uuid: structure.Room_Object):
    item_id = uuid.id
    for item in data_list:
        if item['id'] == item_id:
            data_list.remove(item)
            return {
                "msg": "Item was succesfully deleted",
                "Item deleted": item
            }


