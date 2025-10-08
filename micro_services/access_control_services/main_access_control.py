from  fastapi import FastAPI
from models.access_control_models import Authorization_Incoming_Data
from models.access_control_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.post("/get/{param_a}")
def main_get_post(param_a, data: Authorization_Incoming_Data):

    if param_a == 'role':
        respond = {
            "endpoint": 'get role',
            "echo_data": data
        }
        return  respond

    if param_a == 'policy':
        respond = {
            "endpoint": 'get policy',
            "echo_data": data
        }
        return  respond

    if param_a == 'decision-log':
        respond = {
            "endpoint": 'get decision log',
            "echo_data": data
        }
        return  respond



@app.post("/{param_a}")
def main_post(param_a, data: Incoming_Data):

    if param_a == 'role':
        respond = {
            "endpoint": 'post role',
            "echo_data": data
        }
        return  respond

    if param_a == 'policy':
        respond = {
            "endpoint": 'post policy',
            "echo_data": data
        }
        return  respond


@app.put("/{param_a}")
def main_put(param_a, data: Incoming_Data):

    if param_a == 'role':
        respond = {
            "endpoint": 'put role',
            "echo_data": data
        }
        return  respond

    if param_a == 'policy':
        respond = {
            "endpoint": 'put policy',
            "echo_data": data
        }
        return  respond


@app.delete("/{param_a}")
def main_delete(param_a, data: Incoming_Data):

    if param_a == 'role':
        respond = {
            "endpoint": 'delete role',
            "echo_data": data
        }
        return  respond

    if param_a == 'policy':
        respond = {
            "endpoint": 'delete policy',
            "echo_data": data
        }
        return  respond

    if param_a == 'decision-log':
        respond = {
            "endpoint": 'delete decision log',
            "echo_data": data
        }
        return  respond



