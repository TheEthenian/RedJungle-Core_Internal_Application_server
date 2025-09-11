from  fastapi import FastAPI
from pydantic import BaseModel
import sqlalchemy
import psycopg2
import requests 
import json


app = FastAPI()


data_list = [
    {
        'booking_id': '475dgfdf89',
        'hotel_id':'zdf125',
        'guest_id': '5141dsdf1',
        'room_id': '54sdsdffsd',
        'payment_id': '8adfadf5',
        'duration': 18
    },
    {
        'booking_id': 'ry3u4',
        'hotel_id':'zdd656',
        'guest_id': '1adfadf',
        'room_id': 'ehncnje',
        'payment_id': 'eijcim',
        'duration': 4
    },
    {
        'booking_id': 'zsd345',
        'hotel_id':'ri478438',
        'guest_id': '88fvfddf',
        'room_id': '9o8fr74',
        'payment_id': '84j5768vg',
        'duration': 12
    },
    {
        'booking_id': '7rtqmne',
        'hotel_id':'rurir784',
        'guest_id': '78fdfs966',
        'room_id': '31225354ds',
        'payment_id': '3024dfgdgd',
        'duration': 8
    }
]

class Data_structure(BaseModel):
    hotel_id: str
    guest_id: str
    room_id: str
    payment_id: str
    duration: int



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
        if item['booking_id'] == new_instance.booking_id:
            item['duration'] = new_instance.duration
            return  {
                "msg": 'data block changed',
                "data_pack": item
            }


@app.delete("/")
def remove_avenger(target: Data_structure):
    booking_id = target.booking_id
    for item in data_list:
        if item['booking_id'] == booking_id:
            data_list.remove(item)
            return {
                "msg": "Item was succesfully deleted",
                "Item deleted": item
            }


