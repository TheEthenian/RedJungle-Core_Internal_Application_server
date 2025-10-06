from  fastapi import FastAPI
from models.hotel_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################

app = FastAPI()

#####################################################################


#####################################################################


@app.get("/{param_a}")
def main_get(param_a, data: Incoming_Data):
    
    if param_a == 'hotel':
        respond = {
            "endpoint": 'get hotel',
            "echo_data": data
        }
        return  respond

    if param_a == 'hotel-service':
        respond = {
            "endpoint": 'get hotel service',
            "echo_data": data
        }
        return  respond

    if param_a == 'config':
        respond = {
            "endpoint": 'get config',
            "echo_data": data
        }
        return  respond


@app.post("/{param_a}")
def main_post(param_a, data: Incoming_Data):
    
    if param_a == 'hotel':
        respond = {
            "endpoint": 'post hotel',
            "echo_data": data
        }
        return  respond

    if param_a == 'hotel-service':
        respond = {
            "endpoint": 'post hotel-service',
            "echo_data": data
        }
        return  respond

    if param_a == 'config':
        respond = {
            "endpoint": 'post config',
            "echo_data": data
        }
        return  respond


@app.put("/{param_a}")
def main_put(param_a, data: Incoming_Data):
    
    if param_a == 'hotel':
        respond = {
            "endpoint": 'put hotel',
            "echo_data": data
        }
        return  respond

    if param_a == 'hotel-service':
        respond = {
            "endpoint": 'put hotel service',
            "echo_data": data
        }
        return  respond

    if param_a == 'config':
        respond = {
            "endpoint": 'put config',
            "echo_data": data
        }
        return  respond


@app.delete("/{param_a}")
def main_delete(param_a, data: Incoming_Data):
    
    if param_a == 'hotel':
        respond = {
            "endpoint": 'delete hotel',
            "echo_data": data
        }
        return  respond

    if param_a == 'hotel-service':
        respond = {
            "endpoint": 'delete hotel service',
            "echo_data": data
        }
        return  respond

    if param_a == 'config':
        respond = {
            "endpoint": 'delete config',
            "echo_data": data
        }
        return  respond














