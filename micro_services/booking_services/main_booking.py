from  fastapi import FastAPI
from models.booking_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/{param_a}")
def main_get(param_a, data: Incoming_Data):

    if param_a == 'guest':
        respond = {
            "endpoint": 'get guest',
            "echo_data": data
        }
        return  respond

    if param_a == 'booking':
        respond = {
            "endpoint": 'get booking',
            "echo_data": data
        }
        return  respond

    if param_a == 'invoice':
        respond = {
            "endpoint": 'get invoice',
            "echo_data": data
        }
        return  respond


@app.post("/{param_a}")
def main_post(param_a, data: Incoming_Data):

    if param_a == 'guest':
        respond = {
            "endpoint": 'post guest',
            "echo_data": data
        }
        return  respond

    if param_a == 'booking':
        respond = {
            "endpoint": 'post booking',
            "echo_data": data
        }
        return  respond

    if param_a == 'invoice':
        respond = {
            "endpoint": 'post invoice',
            "echo_data": data
        }
        return  respond


@app.delete("/{param_a}")
def main_delete(param_a, data: Incoming_Data):

    if param_a == 'guest':
        respond = {
            "endpoint": 'delete_guest',
            "echo_data": data
        }
        return  respond

    if param_a == 'booking':
        respond = {
            "endpoint": 'delete_booking',
            "echo_data": data
        }
        return  respond

    if param_a == 'invoice':
        respond = {
            "endpoint": 'delete_invoice',
            "echo_data": data
        }
        return  respond












