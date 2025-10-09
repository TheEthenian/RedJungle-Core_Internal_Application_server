from  fastapi import FastAPI
from models.payment_gateway_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.post("/get/{param_a}")
def main_get_post(param_a, data: Incoming_Data):

    if param_a == 'transaction':
        respond = {
            "endpoint": 'get transaction',
            "echo_data": data
        }
        return  respond

    if param_a == 'bank':
        respond = {
            "endpoint": 'get bank',
            "echo_data": data
        }
        return  respond


@app.post("/{param_a}")
def main_post(param_a, data: Incoming_Data):

    if param_a == 'transaction':
        respond = {
            "endpoint": 'post transaction',
            "echo_data": data
        }
        return  respond

    if param_a == 'bank':
        respond = {
            "endpoint": 'post bank',
            "echo_data": data
        }
        return  respond


@app.put("/bank")
def main_put(data: Incoming_Data):
    respond = {
        "endpoint": 'put bank',
        "echo_data": data
    }
    return  respond


@app.delete("/{param_a}")
def main_get(param_a, data: Incoming_Data):

    if param_a == 'transaction':
        respond = {
            "endpoint": 'delete transaction',
            "echo_data": data
        }
        return  respond

    if param_a == 'bank':
        respond = {
            "endpoint": 'delete bank',
            "echo_data": data
        }
        return  respond


