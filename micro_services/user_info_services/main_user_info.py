from  fastapi import FastAPI
from pydantic import BaseModel
import sqlalchemy
import psycopg2
import requests 
import json


app = FastAPI()


data_list = [
    {
        'guest_id': '47dmfrj',
        'user_name': '86ewre',
        'email': '32sdf5y',
        'bookings_id':['sfsdkfsdkf','4ddfadfsd','6dfadf7','d5adfasdfa7']
    },
    {
        'hotel_chain_id': '12sfsd',
        'hotel_id': 'sdfads12',
        'rooms_available': '54asdfasdf89',
        'bookings_id':['sfsdkfsdkf','4ddfadfsd','6dfadf7','d5adfasdfa7']
    },
    {
        'hotel_chain_id': '11adfsdfs00',
        'hotel_id': '22sdfasdfa1',
        'rooms_available': 'sdfa54adfa',
        'bookings_id':['sfsdkfsdkf','4ddfadfsd','6dfadf7','d5adfasdfa7']
    }
]

class Data_structure(BaseModel):
    hotel_chain_id: str
    hotel_id: str
    rooms_available: str
    booking_id: list


@app.get("/")
def read_me():
    return data_list


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

