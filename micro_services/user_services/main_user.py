from  fastapi import FastAPI
from models.user_info_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/user/{param_a}")
def main_get(param_a, data: Incoming_Data):

    if  param_a == 'info':
        return 'get user info'

    if  param_a == 'profile':
        return 'get user profile'


@app.post("/user/{param_a}")
def main_post(param_a, data: Incoming_Data):

    if  param_a == 'info':
        return 'post user info'

    if  param_a == 'profile':
        return 'post user profile'


@app.put("/user/{param_a}")
def main_put(param_a, data: Incoming_Data):

    if  param_a == 'info':
        return 'put user info'

    if  param_a == 'profile':
        return 'put user profile'


@app.delete("/user/{param_a}")
def main_delete(param_a, data: Incoming_Data):

    if  param_a == 'info':
        return 'delete user info'

    if  param_a == 'profile':
        return 'delete user profile'




















