from  fastapi import FastAPI
from models.user_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/user")
def main_get(data: Incoming_Data):
    respond = {
        "endpoint": 'get user',
        "echo_data": data
    }
    return  respond

@app.get("/user/profile")
def main_get(data: Incoming_Data):
    respond = {
        "endpoint": 'get user profile',
        "echo_data": data
    }
    return  respond


@app.post("/user")
def main_post(data: Incoming_Data):
    respond = {
        "endpoint": 'post user',
        "echo_data": data
    }
    return  respond

@app.post("/user/profile")
def main_post(data: Incoming_Data):
    respond = {
        "endpoint": 'post user profile',
        "echo_data": data
    }
    return  respond


@app.put("/user")
def main_put(data: Incoming_Data):
    respond = {
        "endpoint": 'put user',
        "echo_data": data
    }
    return  respond

@app.put("/user/profile")
def main_put(data: Incoming_Data):
    respond = {
        "endpoint": 'put user profile',
        "echo_data": data
    }
    return  respond


@app.delete("/user")
def main_delete(data: Incoming_Data):
    respond = {
        "endpoint": 'delete user',
        "echo_data": data
    }
    return  respond

@app.delete("/user/profile")
def main_delete(data: Incoming_Data):
    respond = {
        "endpoint": 'delete user profile',
        "echo_data": data
    }
    return  respond





















